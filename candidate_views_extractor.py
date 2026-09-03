"""
Layered Pattern Extraction (L0–L7)
====================================

SQL-aware candidate extraction with strict fidelity guarantees:
  - preserve self-join aliases in FROM/JOIN clauses
  - keep CTE text exactly as written and only rewrite outer query
  - detect join predicates from WHERE equality conditions (col = col)
  - keep join predicates when generating extracted views
  - project query columns (excluding join key columns)
  - safely handle UNION / set-operation queries by preserving full SQL
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

try:
    from sqlglot import exp, parse_one
except ImportError:  # pragma: no cover
    exp = None
    parse_one = None


@dataclass
class TableStats:
    row_count: int
    is_fact: bool
    join_count: int = 0


@dataclass
class CandidateView:
    sql: str
    level: int
    source_sql: str
    tables: List[str] = field(default_factory=list)
    join_pairs: Set[Tuple[str, str]] = field(default_factory=set)
    filters: Dict[str, List[str]] = field(default_factory=dict)
    aggregates: Set[str] = field(default_factory=set)
    label: str = ""
    groupby_cols: Set[str] = field(default_factory=set)
    join_predicates: List[str] = field(default_factory=list)
    select_columns: Set[str] = field(default_factory=set)


def _normalize_name(value: str) -> str:
    if not value:
        return ""
    return value.strip().lower().strip('"`')


def _split_cte_prefix(sql: str) -> Tuple[str, str]:
    """Split raw SQL into (cte_prefix, outer_query_sql) while preserving text."""
    if not sql or not re.match(r"\s*with\b", sql, re.IGNORECASE):
        return "", sql.strip().rstrip(";")

    n = len(sql)
    i = 0

    def _skip_ws(pos: int) -> int:
        while pos < n and sql[pos].isspace():
            pos += 1
        return pos

    def _match_word(pos: int, word: str) -> bool:
        return sql[pos:pos + len(word)].lower() == word

    def _consume_identifier(pos: int) -> int:
        if pos >= n:
            return pos
        if sql[pos] in ('"', '`'):
            quote = sql[pos]
            pos += 1
            while pos < n:
                if sql[pos] == quote:
                    return pos + 1
                pos += 1
            return pos
        while pos < n and (sql[pos].isalnum() or sql[pos] in "_$."):
            pos += 1
        return pos

    def _consume_balanced_parens(pos: int) -> int:
        if pos >= n or sql[pos] != "(":
            return pos
        depth = 0
        in_single = False
        in_double = False
        while pos < n:
            ch = sql[pos]
            if in_single:
                if ch == "'":
                    if pos + 1 < n and sql[pos + 1] == "'":
                        pos += 2
                        continue
                    in_single = False
                pos += 1
                continue
            if in_double:
                if ch == '"':
                    in_double = False
                pos += 1
                continue
            if ch == "'":
                in_single = True
                pos += 1
                continue
            if ch == '"':
                in_double = True
                pos += 1
                continue
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    return pos + 1
            pos += 1
        return pos

    i = _skip_ws(i)
    if not _match_word(i, "with"):
        return "", sql.strip().rstrip(";")
    i += 4
    i = _skip_ws(i)
    if _match_word(i, "recursive"):
        i += 9

    while i < n:
        i = _skip_ws(i)
        i = _consume_identifier(i)
        i = _skip_ws(i)
        if i < n and sql[i] == "(":
            i = _consume_balanced_parens(i)
            i = _skip_ws(i)
        if i + 1 >= n or not _match_word(i, "as"):
            return "", sql.strip().rstrip(";")
        i += 2
        i = _skip_ws(i)
        i = _consume_balanced_parens(i)
        i = _skip_ws(i)
        if i < n and sql[i] == ",":
            i += 1
            continue
        break

    return sql[:i].strip(), sql[i:].strip().rstrip(";")


def _is_set_operation(tree) -> bool:
    return isinstance(tree, (exp.Union, exp.Intersect, exp.Except))


def _base_table_id(table_id: str) -> str:
    table_id = _normalize_name(table_id)
    return table_id.split(":", 1)[0] if table_id else ""


def _flatten_and(expr_node) -> List:
    if expr_node is None:
        return []
    if isinstance(expr_node, exp.And):
        return _flatten_and(expr_node.left) + _flatten_and(expr_node.right)
    return [expr_node]


def _is_equi_join_condition(cond_node) -> bool:
    if not isinstance(cond_node, exp.EQ):
        return False
    if not isinstance(cond_node.left, exp.Column) or not isinstance(cond_node.right, exp.Column):
        return False
    left_table = _normalize_name(cond_node.left.table)
    right_table = _normalize_name(cond_node.right.table)
    # Unqualified col = col patterns are treated as joins to avoid dropping
    # join predicates from filter-style SQL.
    if not left_table and not right_table:
        return True
    if (left_table and not right_table) or (right_table and not left_table):
        return True
    return left_table != right_table


def _column_key(col: exp.Column) -> str:
    table = _normalize_name(col.table)
    name = _normalize_name(col.name)
    return f"{table}.{name}" if table else name


def _extract_outer_tree(sql: str):
    tree = parse_one(sql)
    outer = tree.copy()
    outer.set("with", None)
    return outer


def _extract_from_and_tables(outer_tree) -> Tuple[str, List[str]]:
    if not isinstance(outer_tree, exp.Select):
        return "", []
    from_expr = outer_tree.args.get("from_")
    joins = outer_tree.args.get("joins") or []
    if from_expr is None:
        return "", []

    from_sql = from_expr.sql()
    if joins:
        from_sql += " " + " ".join(j.sql() for j in joins)

    table_ids: List[str] = []

    def _append_table_id(tbl_node):
        if not isinstance(tbl_node, exp.Table):
            return
        name = _normalize_name(tbl_node.name)
        alias = _normalize_name(tbl_node.alias)
        table_id = f"{name}:{alias}" if alias and alias != name else name
        if table_id:
            table_ids.append(table_id)

    # ``FROM (SELECT ...)`` has no outer Table node, but its base tables are
    # still part of the materialized view's dependency and coverage metadata.
    for table_node in outer_tree.find_all(exp.Table):
        _append_table_id(table_node)

    return from_sql, table_ids


def _extract_join_and_filter_predicates(outer_tree) -> Tuple[List[str], List[str]]:
    if not isinstance(outer_tree, exp.Select):
        return [], []
    where_node = outer_tree.args.get("where")
    if where_node is None:
        return [], []
    predicates = _flatten_and(where_node.this)
    join_preds: List[str] = []
    filter_preds: List[str] = []
    for cond in predicates:
        if _is_equi_join_condition(cond):
            join_preds.append(cond.sql())
        else:
            filter_preds.append(cond.sql())
    return join_preds, filter_preds


def _extract_projection_columns(outer_tree, join_predicates: List[str]) -> List[str]:
    if not isinstance(outer_tree, exp.Select):
        return ["*"]

    if any(isinstance(expr_node, exp.Star) for expr_node in outer_tree.expressions):
        return ["*"]

    join_col_keys: Set[str] = set()
    for pred_sql in join_predicates:
        try:
            pred = parse_one(f"SELECT 1 WHERE {pred_sql}").args["where"].this
            if isinstance(pred, exp.EQ) and isinstance(pred.left, exp.Column) and isinstance(pred.right, exp.Column):
                join_col_keys.add(_column_key(pred.left))
                join_col_keys.add(_column_key(pred.right))
        except Exception:
            continue

    ordered: List[str] = []
    seen: Set[str] = set()

    # Preserve original SELECT expressions verbatim. In particular, aggregate
    # expressions must remain aggregates instead of being flattened to their
    # source columns.
    for expr_node in outer_tree.expressions:
        if isinstance(expr_node, exp.Column) and _column_key(expr_node) in join_col_keys:
            continue
        expr_sql = expr_node.sql()
        if expr_sql not in seen:
            seen.add(expr_sql)
            ordered.append(expr_sql)

    # Non-aggregate views also expose filter/group/order columns needed by a
    # rewritten workload query. Adding them to aggregate views would require
    # changing grouping semantics, so preserve their original SELECT only.
    has_aggregate = any(expr_node.find(exp.AggFunc) is not None for expr_node in outer_tree.expressions)
    if has_aggregate:
        return ordered or ["*"]

    for scope in (
        [outer_tree.args.get("where")] if outer_tree.args.get("where") else [],
        (outer_tree.args.get("group").expressions if outer_tree.args.get("group") else []),
        [outer_tree.args.get("having")] if outer_tree.args.get("having") else [],
        (outer_tree.args.get("order").expressions if outer_tree.args.get("order") else []),
    ):
        for expr_node in scope:
            if expr_node is None:
                continue
            for col in expr_node.find_all(exp.Column):
                key = _column_key(col)
                if key in join_col_keys:
                    continue
                if key in seen:
                    continue
                seen.add(key)
                ordered.append(col.sql())

    return ordered or ["*"]


def _extract_aggregates(outer_tree) -> Set[str]:
    if not isinstance(outer_tree, exp.Select):
        return set()
    aggs: Set[str] = set()
    for expr_node in outer_tree.expressions:
        for agg in expr_node.find_all(exp.AggFunc):
            aggs.add(agg.sql())
    return aggs


def _extract_groupby(outer_tree) -> Set[str]:
    if not isinstance(outer_tree, exp.Select):
        return set()
    group = outer_tree.args.get("group")
    if not group:
        return set()
    return {g.sql() for g in group.expressions}


def _join_pairs_from_predicates(join_predicates: List[str]) -> Set[Tuple[str, str]]:
    pairs: Set[Tuple[str, str]] = set()
    for pred_sql in join_predicates:
        try:
            pred = parse_one(f"SELECT 1 WHERE {pred_sql}").args["where"].this
        except Exception:
            continue
        if not isinstance(pred, exp.EQ):
            continue
        if not isinstance(pred.left, exp.Column) or not isinstance(pred.right, exp.Column):
            continue
        left = _normalize_name(pred.left.table)
        right = _normalize_name(pred.right.table)
        if left and right and left != right:
            pairs.add(tuple(sorted((left, right))))
    return pairs


def _join_pairs_from_table_order(table_ids: List[str]) -> Set[Tuple[str, str]]:
    bases = [_base_table_id(t) for t in table_ids if _base_table_id(t)]
    pairs: Set[Tuple[str, str]] = set()
    if len(bases) < 2:
        return pairs
    for idx in range(1, len(bases)):
        left = bases[idx - 1]
        right = bases[idx]
        if left and right and left != right:
            pairs.add(tuple(sorted((left, right))))
    return pairs


def _build_filter_map(filter_predicates: List[str]) -> Dict[str, List[str]]:
    filter_map: Dict[str, List[str]] = {}
    for pred_sql in filter_predicates:
        table_key = "__global__"
        try:
            cond = parse_one(f"SELECT 1 WHERE {pred_sql}").args["where"].this
            first_col = next(cond.find_all(exp.Column), None)
            if first_col is not None and first_col.table:
                table_key = _normalize_name(first_col.table)
        except Exception:
            pass
        filter_map.setdefault(table_key, []).append(pred_sql)
    return filter_map


def _compose_sql(
    cte_prefix: str,
    projection_columns: List[str],
    from_sql: str,
    predicates: List[str],
    groupby_columns: Optional[Set[str]] = None,
) -> str:
    select_sql = ", ".join(projection_columns) if projection_columns else "*"
    if not from_sql:
        body = f"SELECT {select_sql} FROM dual"
    else:
        body = f"SELECT {select_sql} {from_sql}"
    if predicates:
        body += " WHERE " + " AND ".join(predicates)
    if groupby_columns:
        body += " GROUP BY " + ", ".join(sorted(groupby_columns))
    if cte_prefix:
        body = f"{cte_prefix} {body}"
    return body.rstrip(";")


def _extract_select_sql(sql: str) -> str:
    if not sql:
        return "*"
    match = re.search(r"\bselect\s+(.*?)\s+from\b", sql, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip().rstrip(";")
    return "*"


def _extract_setop_tables(outer_tree) -> List[str]:
    tables: List[str] = []
    seen: Set[str] = set()
    for tbl in outer_tree.find_all(exp.Table):
        if any(isinstance(parent, exp.CTE) for parent in tbl.parents):
            continue
        name = _normalize_name(tbl.name)
        alias = _normalize_name(tbl.alias)
        table_id = f"{name}:{alias}" if alias and alias != name else name
        if table_id and table_id not in seen:
            seen.add(table_id)
            tables.append(table_id)
    return tables


def _from_only_subquery_sql(outer_tree) -> Optional[str]:
    """Return the inner SQL when the outer SELECT only wraps one derived table."""
    if not isinstance(outer_tree, exp.Select):
        return None
    from_expr = outer_tree.args.get("from_")
    if from_expr is None or outer_tree.args.get("joins"):
        return None
    derived_table = from_expr.this
    if not isinstance(derived_table, exp.Subquery):
        return None
    inner_query = derived_table.this
    return inner_query.sql().rstrip(";") if inner_query is not None else None


def _build_base_candidates(sql: str, source_sql: str) -> List[CandidateView]:
    cte_prefix, _outer_sql = _split_cte_prefix(sql)
    outer_tree = _extract_outer_tree(sql)

    if _is_set_operation(outer_tree):
        # Keep set-operation SQL intact to ensure database-valid extracted views.
        return [
            CandidateView(
                sql=sql.strip().rstrip(";"),
                level=0,
                source_sql=source_sql or sql,
                tables=_extract_setop_tables(outer_tree),
                label="L0-SETOP-FULLVIEW",
                select_columns={_extract_select_sql(sql)},
            )
        ]

    nested_sql = _from_only_subquery_sql(outer_tree)
    if nested_sql:
        # An outer SELECT over one derived table introduces no new base-table
        # work, so candidate extraction belongs to the inner query.
        return _build_base_candidates(nested_sql, source_sql or sql)

    from_sql, table_ids = _extract_from_and_tables(outer_tree)
    join_preds, filter_preds = _extract_join_and_filter_predicates(outer_tree)
    all_preds = join_preds + filter_preds
    projection_cols = _extract_projection_columns(outer_tree, join_preds)
    joins_pairs = _join_pairs_from_predicates(join_preds) | _join_pairs_from_table_order(table_ids)
    nested_join_predicates: List[str] = []
    for where_node in outer_tree.find_all(exp.Where):
        for condition in _flatten_and(where_node.this):
            if _is_equi_join_condition(condition):
                nested_join_predicates.append(condition.sql())
    joins_pairs |= _join_pairs_from_predicates(nested_join_predicates)
    filters_map = _build_filter_map(filter_preds)
    aggs = _extract_aggregates(outer_tree)
    groupby_cols = _extract_groupby(outer_tree)

    candidates: List[CandidateView] = [
        CandidateView(
            sql=_compose_sql(cte_prefix, projection_cols, from_sql, all_preds, groupby_cols),
            level=0,
            source_sql=source_sql or sql,
            tables=list(table_ids),
            join_pairs=joins_pairs,
            join_predicates=list(join_preds),
            filters=filters_map,
            aggregates=aggs,
            groupby_cols=groupby_cols,
            label="L0-FULLVIEW",
            select_columns=set(projection_cols),
        )
    ]

    if join_preds:
        candidates.append(
            CandidateView(
                sql=_compose_sql(cte_prefix, projection_cols, from_sql, list(join_preds), groupby_cols),
                level=1,
                source_sql=source_sql or sql,
                tables=list(table_ids),
                join_pairs=joins_pairs,
                join_predicates=list(join_preds),
                label="L1-JOINS",
                select_columns=set(projection_cols),
            )
        )

    if filter_preds:
        candidates.append(
            CandidateView(
                sql=_compose_sql(cte_prefix, projection_cols, from_sql, all_preds, groupby_cols),
                level=2,
                source_sql=source_sql or sql,
                tables=list(table_ids),
                join_pairs=joins_pairs,
                join_predicates=list(join_preds),
                filters=filters_map,
                label="L2-FILTERS",
                select_columns=set(projection_cols),
            )
        )

    if aggs:
        candidates.append(
            CandidateView(
                sql=_compose_sql(cte_prefix, projection_cols, from_sql, all_preds, groupby_cols),
                level=3,
                source_sql=source_sql or sql,
                tables=list(table_ids),
                join_pairs=joins_pairs,
                join_predicates=list(join_preds),
                filters=filters_map,
                aggregates=aggs,
                groupby_cols=groupby_cols,
                label="L3-AGGREGATE",
                select_columns=set(projection_cols),
            )
        )

    if join_preds and filter_preds:
        candidates.append(
            CandidateView(
                sql=_compose_sql(cte_prefix, projection_cols, from_sql, all_preds, groupby_cols),
                level=4,
                source_sql=source_sql or sql,
                tables=list(table_ids),
                join_pairs=joins_pairs,
                join_predicates=list(join_preds),
                filters=filters_map,
                label="L4-JOINS-FILTERS",
                select_columns=set(projection_cols),
            )
        )

    if join_preds and aggs:
        candidates.append(
            CandidateView(
                sql=_compose_sql(cte_prefix, projection_cols, from_sql, all_preds, groupby_cols),
                level=5,
                source_sql=source_sql or sql,
                tables=list(table_ids),
                join_pairs=joins_pairs,
                join_predicates=list(join_preds),
                filters=filters_map,
                aggregates=aggs,
                groupby_cols=groupby_cols,
                label="L5-JOINS-AGGS",
                select_columns=set(projection_cols),
            )
        )

    if cte_prefix:
        candidates.append(
            CandidateView(
                sql=_compose_sql(cte_prefix, projection_cols, from_sql, all_preds, groupby_cols),
                level=6,
                source_sql=source_sql or sql,
                tables=list(table_ids),
                join_pairs=joins_pairs,
                join_predicates=list(join_preds),
                filters=filters_map,
                aggregates=aggs,
                groupby_cols=groupby_cols,
                label="L6-CTE",
                select_columns=set(projection_cols),
            )
        )

    return candidates


def extract_full_views(sql: str, table_stats: Dict[str, TableStats], column_schema: Optional[Dict[str, Set[str]]] = None, source_sql: str = "") -> List[CandidateView]:
    return [c for c in _build_base_candidates(sql, source_sql or sql) if c.level == 0]


def extract_join_combinations(sql: str, table_stats: Dict[str, TableStats], column_schema: Optional[Dict[str, Set[str]]] = None, source_sql: str = "") -> List[CandidateView]:
    return [c for c in _build_base_candidates(sql, source_sql or sql) if c.level == 1]


def extract_filter_views(sql: str, table_stats: Dict[str, TableStats], column_schema: Optional[Dict[str, Set[str]]] = None, source_sql: str = "") -> List[CandidateView]:
    return [c for c in _build_base_candidates(sql, source_sql or sql) if c.level == 2]


def extract_aggregate_views(sql: str, table_stats: Dict[str, TableStats], column_schema: Optional[Dict[str, Set[str]]] = None, source_sql: str = "") -> List[CandidateView]:
    return [c for c in _build_base_candidates(sql, source_sql or sql) if c.level == 3]


def extract_joins_filters(sql: str, table_stats: Dict[str, TableStats], column_schema: Optional[Dict[str, Set[str]]] = None, source_sql: str = "") -> List[CandidateView]:
    return [c for c in _build_base_candidates(sql, source_sql or sql) if c.level == 4]


def extract_joins_aggregates(sql: str, table_stats: Dict[str, TableStats], column_schema: Optional[Dict[str, Set[str]]] = None, source_sql: str = "") -> List[CandidateView]:
    return [c for c in _build_base_candidates(sql, source_sql or sql) if c.level == 5]


def extract_cte_views(sql: str, table_stats: Dict[str, TableStats], column_schema: Optional[Dict[str, Set[str]]] = None, source_sql: str = "") -> List[CandidateView]:
    return [c for c in _build_base_candidates(sql, source_sql or sql) if c.level == 6]


def _extract_single_cte(cte_sql: str, cte_name: str, table_stats: Dict[str, TableStats], column_schema: Optional[Dict[str, Set[str]]] = None, source_sql: str = "") -> Optional[CandidateView]:
    cands = _build_base_candidates(cte_sql, source_sql or cte_sql)
    return cands[0] if cands else None


def _find_subqueries(tree) -> List[Tuple[str, str, str]]:
    return []


def extract_subquery_variants(sql: str, table_stats: Dict[str, TableStats], column_schema: Optional[Dict[str, Set[str]]] = None, source_sql: str = "") -> List[CandidateView]:
    return []


def _combine_query_with_subquery(query_sql: str, subq_sql: str, alias: str) -> str:
    return query_sql


def get_where_clause(sql: str) -> str:
    if not sql or parse_one is None:
        return ""
    try:
        outer = _extract_outer_tree(sql)
        if isinstance(outer, exp.Select) and outer.args.get("where"):
            return outer.args["where"].sql()
    except Exception:
        return ""
    return ""


def extract_all_candidates(sql: str, table_stats: Dict[str, TableStats], column_schema: Optional[Dict[str, Set[str]]] = None) -> List[CandidateView]:
    if not sql or not sql.strip():
        return []
    if parse_one is None:
        return [CandidateView(sql=sql.strip().rstrip(";"), level=0, source_sql=sql, label="L0-FULLVIEW")]
    try:
        candidates = _build_base_candidates(sql, sql)
    except Exception:
        candidates = [CandidateView(sql=sql.strip().rstrip(";"), level=0, source_sql=sql, label="L0-FULLVIEW")]
    return _deduplicate_candidates(candidates)


def extract_workload_candidates(queries: List[str], table_stats: Dict[str, TableStats], column_schema: Optional[Dict[str, Set[str]]] = None, deduplicate: bool = True) -> List[CandidateView]:
    all_candidates: List[CandidateView] = []
    for sql in queries:
        all_candidates.extend(extract_all_candidates(sql, table_stats, column_schema))
    if deduplicate:
        all_candidates = _deduplicate_candidates(all_candidates)
    return all_candidates


def _deduplicate_candidates(candidates: List[CandidateView]) -> List[CandidateView]:
    deduped: List[CandidateView] = []
    seen_sql: Set[str] = set()
    for cand in candidates:
        if not cand.sql:
            continue
        key = cand.sql.strip().lower()
        if key in seen_sql:
            continue
        seen_sql.add(key)
        deduped.append(cand)
    return deduped


def extract(query_sql: str, table_stats: Dict[str, TableStats], column_schema=None) -> List[CandidateView]:
    return extract_all_candidates(query_sql, table_stats, column_schema)


__all__ = [
    "TableStats",
    "CandidateView",
    "extract_all_candidates",
    "extract_workload_candidates",
    "extract_full_views",
    "extract_join_combinations",
    "extract_filter_views",
    "extract_aggregate_views",
    "extract_joins_filters",
    "extract_joins_aggregates",
    "extract_cte_views",
    "extract_subquery_variants",
    "extract",
]
