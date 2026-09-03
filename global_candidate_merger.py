"""Simplified global candidate merger for the view extraction pipeline."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
import re
from typing import Any, Dict, List, Optional, Set, Tuple

from sqlglot import exp, parse_one


MAX_FILTER_VALUES_IN = 6


@dataclass
class MergeResult:
    merged_candidates: List[Dict[str, Any]]
    stats: Dict[str, Any]


def _normalize_table_name(value: str) -> str:
    if not value:
        return ""
    text = value.strip().lower().strip('"`')
    text = text.split(":", 1)[0]
    return text.split()[0] if text else ""


def _normalize_filter_predicates(filters: Optional[Dict[str, List[str]]]) -> Dict[str, List[str]]:
    normalized: Dict[str, List[str]] = {}
    for table_name, preds in (filters or {}).items():
        cleaned = []
        for pred in preds:
            if pred and pred not in cleaned:
                cleaned.append(pred)
        normalized[table_name] = cleaned
    return normalized


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return tuple(sorted((key, _freeze(val)) for key, val in value.items()))
    if isinstance(value, (list, tuple)):
        return tuple(_freeze(item) for item in value)
    if isinstance(value, set):
        return tuple(sorted(_freeze(item) for item in value))
    return value


def _structural_signature(candidate: Dict[str, Any]) -> Tuple[Any, ...]:
    table_names = [_normalize_table_name(t) for t in candidate.get("tables", []) if _normalize_table_name(t)]
    tables = tuple(sorted(table_names))
    joins = _freeze(candidate.get("join_pairs", []))
    filter_tables = tuple(sorted((candidate.get("filters") or {}).keys()))
    aggregates = _freeze(candidate.get("aggregates", []))
    groupby_cols = _freeze(candidate.get("groupby_cols", []))
    level = candidate.get("level", 0)
    return (level, tables, joins, filter_tables, aggregates, groupby_cols)


def _merge_ordered_unique(left: Any, right: Any) -> List[Any]:
    merged: List[Any] = []
    for item in list(left or []) + list(right or []):
        if item not in merged:
            merged.append(item)
    return merged


def _merge_filters(filters: Dict[str, List[str]]) -> Dict[str, List[str]]:
    merged: Dict[str, List[str]] = {}
    for table_name, preds in filters.items():
        normalized_preds: List[str] = []
        for pred in preds:
            if pred and pred not in normalized_preds:
                normalized_preds.append(pred)
        if normalized_preds:
            merged[table_name] = normalized_preds
    return merged


def _parse_predicate(predicate_sql: str):
    """Parse one predicate without allowing a bad predicate to fail merging."""
    try:
        return parse_one(f"SELECT 1 WHERE {predicate_sql}").args["where"].this
    except Exception:
        return None


def _is_date_expression(expr_node) -> bool:
    if isinstance(expr_node, exp.Cast):
        to_type = expr_node.args.get("to")
        return to_type is not None and "DATE" in to_type.sql().upper()
    if isinstance(expr_node, exp.Literal) and expr_node.is_string:
        return bool(__import__("re").fullmatch(r"\d{4}-\d{2}-\d{2}(?:[ T].*)?", expr_node.this))
    return "DATE" in expr_node.sql().upper()


def _date_sort_key(value_sql: str):
    """Evaluate common DATE +/- INTERVAL day expressions for ordering."""
    match = re.search(
        r"(?:DATE\s*)?'(\d{4}-\d{2}-\d{2})'\s*([+-])?\s*(?:INTERVAL\s*'?(\d+)'?\s*DAY)?",
        value_sql,
        re.IGNORECASE,
    )
    if not match:
        return value_sql
    date_value = datetime.strptime(match.group(1), "%Y-%m-%d").date()
    interval_days = int(match.group(3) or 0)
    if match.group(2) == "+":
        date_value += timedelta(days=interval_days)
    elif match.group(2) == "-":
        date_value -= timedelta(days=interval_days)
    return date_value


def _predicate_parts(predicate_sql: str):
    """Return (column, operator, value, is_date), or None for complex predicates."""
    predicate = _parse_predicate(predicate_sql)
    if not isinstance(predicate, (exp.EQ, exp.Like, exp.LT, exp.LTE, exp.GT, exp.GTE)):
        return None
    left = predicate.left
    right = predicate.right
    if not isinstance(left, exp.Column):
        return None
    if isinstance(right, exp.Column) or isinstance(right, exp.Subquery):
        return None
    return left.sql(), predicate.key.upper(), right, _is_date_expression(right)


def _flatten_and_conditions(expression) -> List[Any]:
    if isinstance(expression, exp.And):
        return _flatten_and_conditions(expression.left) + _flatten_and_conditions(expression.right)
    return [expression] if expression is not None else []


def _filter_column_values(expression) -> List[Tuple[str, str, str, bool]]:
    """Return scalar values associated with every filtered column in a WHERE tree."""
    values: List[Tuple[str, str, str, bool]] = []
    for predicate in expression.walk():
        if not isinstance(predicate, (exp.EQ, exp.Like, exp.LT, exp.LTE, exp.GT, exp.GTE)):
            continue
        if not isinstance(predicate.left, exp.Column):
            continue
        if isinstance(predicate.right, (exp.Column, exp.Subquery)):
            continue
        values.append((
            predicate.left.sql(),
            predicate.key.upper(),
            predicate.right.sql(),
            _is_date_expression(predicate.right),
        ))
    return values


def _group_filter_values(candidates: List[Dict[str, Any]]) -> Dict[Tuple[str, str, bool], List[str]]:
    """Collect all scalar WHERE-filter values by column across similar views."""
    values_by_column: Dict[Tuple[str, str, bool], List[str]] = defaultdict(list)
    for candidate in candidates:
        try:
            tree = parse_one(candidate.get("sql", ""))
        except Exception:
            continue
        for where in tree.find_all(exp.Where):
            for column_sql, operator, value_sql, is_date in _filter_column_values(where.this):
                key = (column_sql, operator, is_date)
                if value_sql not in values_by_column[key]:
                    values_by_column[key].append(value_sql)
    return values_by_column


def _merge_group_filters(sql: str, values_by_column: Dict[Tuple[str, str, bool], List[str]]) -> str:
    """Rewrite every WHERE scope using the workload-wide filter values.

    A column with at most six values becomes ``column IN (...)``. A column
    with more values is removed from WHERE, while its SELECT projection is
    left untouched. Join predicates are never altered.
    """
    if not values_by_column:
        return sql
    try:
        tree = parse_one(sql)
    except Exception:
        return sql

    def rewrite(expression):
        if expression is None:
            return None
        if isinstance(expression, exp.Paren):
            retained = rewrite(expression.this)
            return exp.Paren(this=retained) if retained is not None else None
        if isinstance(expression, (exp.And, exp.Or)):
            left = rewrite(expression.left)
            right = rewrite(expression.right)
            if isinstance(expression, exp.And):
                if left is None:
                    return right
                if right is None:
                    return left
                return exp.and_(left, right)
            if left is None or right is None:
                # Dropping one branch of an OR broadens the predicate; drop
                # the entire OR block instead of retaining a partial branch.
                return None
            return exp.or_(left, right)
        if not isinstance(expression, (exp.EQ, exp.Like, exp.LT, exp.LTE, exp.GT, exp.GTE)):
            return expression
        if not isinstance(expression.left, exp.Column):
            return expression
        if isinstance(expression.right, (exp.Column, exp.Subquery)):
            return expression
        is_date = _is_date_expression(expression.right)
        operator = expression.key.upper()
        values = values_by_column.get((expression.left.sql(), operator, is_date))
        if values is None:
            return expression
        if is_date and operator in {"LT", "LTE", "GT", "GTE"}:
            selected = (
                min(values, key=_date_sort_key)
                if operator in {"GT", "GTE"}
                else max(values, key=_date_sort_key)
            )
            rewritten = expression.copy()
            rewritten.set("expression", parse_one(selected))
            return rewritten
        if len(values) > MAX_FILTER_VALUES_IN:
            return None
        value_nodes = [parse_one(value) for value in values]
        return exp.In(this=expression.left.copy(), expressions=value_nodes)

    for where in list(tree.find_all(exp.Where)):
        retained = rewrite(where.this)
        if retained is None:
            where.parent.set("where", None)
        else:
            where.set("this", retained)
    return tree.sql().rstrip(";")


def _combine_filters(filters: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Merge compatible filter values according to the candidate-view rules."""
    result: Dict[str, List[str]] = {}
    for table_name, predicates in filters.items():
        grouped: Dict[Tuple[str, str, bool], List[Any]] = defaultdict(list)
        unmergeable: Dict[str, int] = defaultdict(int)

        for predicate_sql in predicates:
            parts = _predicate_parts(predicate_sql)
            if parts is None:
                unmergeable[predicate_sql] += 1
                continue
            column_sql, operator, value, is_date = parts
            grouped[(column_sql, operator, is_date)].append(value)

        merged_predicates: List[str] = []
        for (column_sql, operator, is_date), values in grouped.items():
            unique_values = _merge_ordered_unique([], [value.sql() for value in values])
            if is_date and operator in {"LT", "LTE", "GT", "GTE"}:
                # A lower bound uses the earliest date and an upper bound uses
                # the latest date, yielding one inclusive workload interval.
                selected = (
                    min(unique_values, key=_date_sort_key)
                    if operator in {"GT", "GTE"}
                    else max(unique_values, key=_date_sort_key)
                )
                sql_operator = {"LT": "<", "LTE": "<=", "GT": ">", "GTE": ">="}[operator]
                merged_predicates.append(f"{column_sql} {sql_operator} {selected}")
            elif operator in {"EQ", "LIKE"}:
                if len(unique_values) <= MAX_FILTER_VALUES_IN:
                    merged_predicates.append(f"{column_sql} IN ({', '.join(unique_values)})")
                # More than six values are intentionally broadened by dropping
                # the filter, as requested for materialized-view candidates.
            else:
                # Non-date inequality filters are retained only when every
                # candidate supplied the same predicate.
                merged_predicates.append(f"{column_sql} {operator} {unique_values[0]}")

        # Keep non-simple predicates only when they are identical. Different
        # values cannot be merged safely and are broadened by omission.
        merged_predicates.extend(predicate for predicate, count in unmergeable.items() if count == len(predicates))
        if merged_predicates:
            result[table_name] = merged_predicates
    return result


def _replace_outer_filters(sql: str, filters: Dict[str, List[str]], join_predicates: List[str]) -> str:
    """Rewrite only the outer WHERE clause; SELECT aggregates and CTEs remain intact."""
    try:
        tree = parse_one(sql)
    except Exception:
        return sql
    if not isinstance(tree, exp.Select):
        return sql

    conditions = []
    for predicate_sql in join_predicates:
        predicate = _parse_predicate(predicate_sql)
        if predicate is not None:
            conditions.append(predicate)
    for predicates in filters.values():
        for predicate_sql in predicates:
            predicate = _parse_predicate(predicate_sql)
            if predicate is not None:
                conditions.append(predicate)

    where_expression = None
    for condition in conditions:
        where_expression = condition if where_expression is None else exp.and_(where_expression, condition)
    tree.set("where", exp.Where(this=where_expression) if where_expression is not None else None)
    return tree.sql().rstrip(";")


def _candidate_sql_from_fields(candidate: Dict[str, Any]) -> str:
    tables = sorted({_normalize_table_name(t) for t in candidate.get("tables", [])})
    if not tables:
        tables = ["dual"]
    select_columns = candidate.get("select_sql") or candidate.get("select_columns") or "*"
    if isinstance(select_columns, (list, set, tuple)):
        select_columns = ", ".join(select_columns)
    if not select_columns:
        select_columns = "*"
    sql = f"SELECT {select_columns} FROM {', '.join(tables)}"
    filters = _merge_filters(candidate.get("filters") or {})
    if filters:
        where_clauses = []
        for _, preds in sorted(filters.items()):
            where_clauses.extend(preds)
        if where_clauses:
            sql += " WHERE " + " AND ".join(where_clauses)
    groupby = candidate.get("groupby_cols") or []
    if groupby:
        sql += " GROUP BY " + ", ".join(sorted(str(col) for col in groupby))
    return sql.rstrip(";")


def merge_candidates(all_candidates: List[Dict[str, Any]]) -> MergeResult:
    normalized_candidates: List[Dict[str, Any]] = []
    for cand in all_candidates:
        if isinstance(cand, dict):
            normalized_candidates.append(cand)

    grouped: Dict[Tuple[Any, ...], List[Dict[str, Any]]] = defaultdict(list)
    for cand in normalized_candidates:
        grouped[_structural_signature(cand)].append(cand)

    merged: List[Dict[str, Any]] = []
    stats = {
        "input_count": len(normalized_candidates),
        "perfect_duplicates_removed": 0,
        "select_merges": 0,
        "filter_merges": 0,
        "output_count": 0,
    }

    for _, group in grouped.items():
        if not group:
            continue
        base = dict(group[0])
        base["tables"] = list(base.get("tables", []))
        base["filters"] = _normalize_filter_predicates(base.get("filters"))
        base["aggregates"] = set(base.get("aggregates", []))
        base["groupby_cols"] = set(base.get("groupby_cols", []))
        base["join_pairs"] = {_freeze(pair) for pair in base.get("join_pairs", [])}
        base["join_predicates"] = list(base.get("join_predicates", []))
        for candidate in group[1:]:
            if candidate.get("sql") and base.get("sql") and candidate.get("sql") == base.get("sql"):
                stats["perfect_duplicates_removed"] += 1
                continue
            if candidate.get("select_columns") or candidate.get("select_sql"):
                stats["select_merges"] += 1
            if candidate.get("filters"):
                stats["filter_merges"] += 1
            base["tables"] = _merge_ordered_unique(base.get("tables", []), candidate.get("tables", []))
            base["join_pairs"].update({_freeze(pair) for pair in candidate.get("join_pairs", [])})
            base["aggregates"].update(set(candidate.get("aggregates", [])))
            base["groupby_cols"].update(set(candidate.get("groupby_cols", [])))
            base["join_predicates"] = _merge_ordered_unique(base.get("join_predicates", []), candidate.get("join_predicates", []))
            for table_name, predicates in _normalize_filter_predicates(candidate.get("filters")).items():
                base["filters"][table_name] = _merge_ordered_unique(base["filters"].get(table_name, []), predicates)
        base["filters"] = _combine_filters(base["filters"])
        if base.get("sql"):
            base["sql"] = _merge_group_filters(base["sql"], _group_filter_values(group))
        else:
            base["sql"] = _candidate_sql_from_fields(base)
        base["label"] = base.get("label") or f"L{base.get('level', 0)}-MERGED"
        merged.append(base)

    stats["output_count"] = len(merged)
    return MergeResult(merged_candidates=merged, stats=stats)


def run_merge_pipeline(candidates_per_query: Dict[str, List[Dict[str, Any]]]) -> MergeResult:
    flat: List[Dict[str, Any]] = []
    for candidates in candidates_per_query.values():
        flat.extend(candidates)
    return merge_candidates(flat)
