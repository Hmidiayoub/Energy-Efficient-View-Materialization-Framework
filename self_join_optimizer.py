"""
GreenVIEW — Self-Join Stripping Optimizer
===========================================

For candidate views that contain self-joins (same base table with multiple
aliases), create a stripped version without the self-join tables, then
keep whichever version (original or stripped) has higher benefit.

Self-joins come from queries like:
    SELECT ... FROM nation n1, nation n2 WHERE n1.n_nationkey = n2.n_nationkey

Stripping removes:
    - The redundant table aliases
    - Join conditions involving removed aliases
    - Filter predicates on removed aliases
    - Aggregate expressions referencing removed aliases
    - GROUP BY columns referencing removed aliases
    - SELECT expressions referencing removed aliases

Pipeline integration:
    After step 4 (cost-benefit), before step 5 (collections):
        from self_join_optimizer import optimize_self_joins
        merged = optimize_self_joins(merged, schema, conn_params)
"""

import re
import copy
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional, Any


# ─────────────────────────────────────────────────────────────────────────────
# Self-join detection
# ─────────────────────────────────────────────────────────────────────────────

def _parse_table_id(tid: str) -> Tuple[str, str]:
    """
    Parse a table identifier into (base_table, alias).
    
    Examples:
        'nation:n1'      → ('nation', 'n1')
        'lineitem'       → ('lineitem', 'lineitem')
        'customer_address:ad1' → ('customer_address', 'ad1')
    """
    if ':' in tid:
        parts = tid.split(':', 1)
        return (parts[0], parts[1])
    return (tid, tid)


def _extract_table_refs(sql: str) -> Set[str]:
    """
    Extract all table.column references (qualified columns) from SQL.
    Returns set of table names used as qualifiers.
    
    Example:
        'n1.n_nationkey, n2.n_name' → {'n1', 'n2'}
    """
    return set(re.findall(r'(?<![.\w])(\w+)\.(\w+)', sql))


def detect_self_joins(tables: Set[str]) -> Dict[str, List[str]]:
    """
    Detect self-joined tables.
    
    Returns:
        {base_table: [alias1, alias2, ...]}
        Only includes base tables that appear more than once.
        
    Example:
        {'nation': ['n1', 'n2'], 'customer_address': ['ad1', 'ad2']}
    """
    alias_by_base: Dict[str, List[str]] = defaultdict(list)
    for tid in tables:
        base, alias = _parse_table_id(tid)
        alias_by_base[base].append(alias if ':' in tid else None)
    
    self_joins = {}
    for base, aliases in alias_by_base.items():
        if len(aliases) >= 2:
            self_joins[base] = aliases
    return self_joins


# ─────────────────────────────────────────────────────────────────────────────
# Stripping logic
# ─────────────────────────────────────────────────────────────────────────────

def _build_id_for_alias(base: str, alias: str) -> str:
    """Build the full table identifier for a base:alias pair."""
    if alias == base:
        return base
    return f"{base}:{alias}"


def _aliases_to_remove(
    self_joins: Dict[str, List[str]]
) -> Dict[str, str]:
    """
    For each self-joined base table, pick the alias to KEEP and
    return {alias_to_remove: base_table} for the ones to remove.
    
    Strategy: keep the FIRST alias (arbitrary but deterministic),
    remove all others.
    
    Returns:
        {removed_alias: base_table} for each alias to strip
    """
    remove_map = {}
    for base, aliases in self_joins.items():
        keep = aliases[0]  # Keep first
        for alias in aliases[1:]:
            remove_map[alias] = base
    return remove_map


def _needs_stripping(tables: Set[str]) -> bool:
    """Check if a candidate has any self-joins."""
    return len(detect_self_joins(tables)) > 0


def strip_self_joins(candidate: dict) -> Optional[dict]:
    """
    Create a stripped version of a candidate view without self-joins.
    
    Returns a new dict with the same structure as the original, or
    None if stripping is not applicable (no self-joins) or would
    produce an empty view.
    """
    tables = set(candidate.get("tables", []))
    if not _needs_stripping(tables):
        return None
    
    self_joins = detect_self_joins(tables)
    remove_map = _aliases_to_remove(self_joins)
    removed_aliases = set(remove_map.keys())
    removed_ids = set()
    for alias in removed_aliases:
        for tid in tables:
            base, al = _parse_table_id(tid)
            if al == alias or tid == alias:
                removed_ids.add(tid)
    
    if not removed_ids:
        return None
    
    # Create a deep copy to modify
    stripped = copy.deepcopy(candidate)
    stripped_tables = set(stripped.get("tables", [])) - removed_ids
    
    if len(stripped_tables) < 1:
        return None  # Stripped down to nothing
    
    stripped["tables"] = list(stripped_tables)
    
    # ── Remove join_pairs involving removed tables ────────────────
    old_joins = list(stripped.get("join_pairs", []))
    new_joins = []
    for pair in old_joins:
        a, b = pair
        if a not in removed_ids and b not in removed_ids:
            new_joins.append(pair)
    stripped["join_pairs"] = new_joins
    
    # ── Remove filters on removed tables ──────────────────────────
    old_filters = dict(stripped.get("filters", {}))
    new_filters = {}
    for tbl, preds in old_filters.items():
        if tbl not in removed_ids:
            new_filters[tbl] = preds
    stripped["filters"] = new_filters
    
    # ── Remove aggregate expressions referencing removed aliases ──
    old_aggs = set(stripped.get("aggregates", []))
    new_aggs = set()
    for agg_sql in old_aggs:
        refs = _extract_table_refs(agg_sql)
        if not refs & removed_aliases:  # No references to removed aliases
            new_aggs.add(agg_sql)
    stripped["aggregates"] = list(new_aggs)
    
    # ── Remove GROUP BY columns referencing removed aliases ───────
    old_gb = set(stripped.get("groupby_cols", []))
    new_gb = set()
    for gc in old_gb:
        refs = _extract_table_refs(gc)
        if not refs & removed_aliases:
            new_gb.add(gc)
    stripped["groupby_cols"] = list(new_gb)
    
    # ── Rebuild SQL ───────────────────────────────────────────────
    # We need to parse the original SQL, remove the table aliases,
    # remove related conditions, and reassemble.
    stripped["view_sql"] = _rebuild_sql_without_self_joins(
        candidate.get("view_sql", candidate.get("sql", "")),
        removed_ids,
        removed_aliases,
    )
    stripped["sql"] = stripped["view_sql"]
    
    # Update label
    old_label = stripped.get("label", "")
    if old_label:
        stripped["label"] = old_label + "_NO_SELF_JOIN"
    
    stripped["_self_join_stripped"] = True
    
    return stripped


def _rebuild_sql_without_self_joins(
    sql: str,
    removed_ids: Set[str],
    removed_aliases: Set[str],
) -> str:
    """
    Rebuild a SQL string by removing self-joined tables and all
    conditions/references to their aliases.
    
    This works at the string level (no sqlglot AST) for robustness.
    """
    if not sql:
        return sql
    
    # ── Step 1: Remove alias definitions from SELECT ──────────────
    # Replace patterns like "n1.n_name AS ..." with nothing
    # Look for column references using removed aliases
    lines = sql.split('\n')
    
    # ── Step 2: Remove FROM clause entries for removed tables ─────
    from_idx = -1
    for i, line in enumerate(lines):
        if re.search(r'\bFROM\b', line, re.IGNORECASE):
            from_idx = i
            break
    
    if from_idx >= 0:
        from_line = lines[from_idx]
        # Remove table references that match removed_ids
        for tid in removed_ids:
            base, alias = _parse_table_id(tid)
            # Patterns: "base alias," or "base,"  or "alias,"
            patterns = [
                re.escape(base) + r'\s+' + re.escape(alias),
                re.escape(alias),
            ]
            for pat in patterns:
                from_line = re.sub(
                    rf'{pat}\s*,?\s*', '', from_line, flags=re.IGNORECASE
                )
        lines[from_idx] = from_line
    
    # ── Step 3: Remove WHERE conditions involving removed aliases ─
    where_idx = -1
    for i, line in enumerate(lines):
        if re.search(r'\bWHERE\b', line, re.IGNORECASE):
            where_idx = i
            break
    
    if where_idx >= 0:
        # Collect all WHERE conditions
        conditions = []
        current_cond = ""
        where_started = False
        for i in range(where_idx, len(lines)):
            line = lines[i]
            if where_started:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                if stripped_line.upper().startswith(('GROUP', 'ORDER', 'HAVING', 'LIMIT')):
                    # Next clause started
                    break
                current_cond += " " + stripped_line
            else:
                where_started = True
                current_cond = re.sub(
                    r'\bWHERE\b', '', line, flags=re.IGNORECASE
                ).strip()
        
        # Split on AND (at top level, respecting parentheses)
        parts = _split_and(current_cond)
        
        # Keep only conditions that don't reference removed aliases
        kept_parts = []
        for part in parts:
            refs = _extract_table_refs(part)
            if not refs & removed_aliases:
                kept_parts.append(part)
        
        if kept_parts:
            new_where = "WHERE " + "\n  AND ".join(kept_parts)
            lines[where_idx] = new_where
            for i in range(where_idx + 1, len(lines)):
                line = lines[i].strip()
                if line.upper().startswith(('GROUP', 'ORDER', 'HAVING', 'LIMIT')):
                    break
                lines[i] = ""
        else:
            lines[where_idx] = ""
    
    result = "\n".join(line for line in lines if line.strip())
    
    # Clean up: remove double commas, trailing commas
    result = re.sub(r',\s*,', ',', result)
    result = re.sub(r',\s*\n\s*FROM', '\nFROM', result, flags=re.IGNORECASE)
    result = re.sub(r'\(\s*\)', '', result)  # Empty parentheses
    
    return result.strip()


def _split_and(clause: str) -> List[str]:
    """Split a WHERE clause on AND, respecting parentheses."""
    parts = []
    depth = 0
    current = ""
    in_string = False
    string_char = None
    
    i = 0
    while i < len(clause):
        ch = clause[i]
        
        # Handle string literals
        if ch in ("'", '"'):
            if not in_string:
                in_string = True
                string_char = ch
            elif string_char == ch:
                in_string = False
            current += ch
            i += 1
            continue
        
        if in_string:
            current += ch
            i += 1
            continue
        
        if ch == '(':
            depth += 1
            current += ch
        elif ch == ')':
            depth -= 1
            current += ch
        elif depth == 0 and i + 2 < len(clause):
            if clause[i:i+3].upper() == 'AND' and (i == 0 or not clause[i-1].isalnum()):
                and_end = i + 3
                if and_end >= len(clause) or not clause[and_end].isalnum():
                    parts.append(current.strip())
                    current = ""
                    i += 3
                    continue
                current += ch
            else:
                current += ch
        else:
            current += ch
        i += 1
    
    if current.strip():
        parts.append(current.strip())
    
    return parts


# ─────────────────────────────────────────────────────────────────────────────
# Benefit comparison and optimization
# ─────────────────────────────────────────────────────────────────────────────

def compute_benefit_for_candidate(
    candidate: dict,
    query_metrics: Dict[str, Dict],
    total_metrics: Dict[str, float],
    storage_bytes: int,
    total_db_size: int,
    db_size_threshold: float = 0.20,
) -> float:
    """
    Compute the benefit score for a single candidate.
    
    benefit = exec_time_pct * similarity + avg_cpu + max_cpu
              - storage_cost_pct
    
    Where storage_cost_pct = storage_bytes / total_db_size
    """
    covered_ids = candidate.get("_covered_ids", [])
    similarity = candidate.get("_avg_similarity", 0.0)
    
    covered_exec_time = 0.0
    covered_cpu_mean = 0.0
    covered_cpu_max_vals = []
    
    for qid in covered_ids:
        m = query_metrics.get(qid)
        if m:
            covered_exec_time += m["execution_time"]
            covered_cpu_mean += m["cpu_mean"]
            covered_cpu_max_vals.append(m["cpu_max"])
    
    n_covered = len(covered_ids)
    total_exec_time = total_metrics.get("exec_time", 0)
    
    exec_time_pct = covered_exec_time / total_exec_time if total_exec_time > 0 else 0.0
    avg_cpu = (covered_cpu_mean / n_covered / 100.0) if n_covered > 0 else 0.0
    max_cpu = (sum(covered_cpu_max_vals) / n_covered / 100.0) if n_covered > 0 else 0.0
    storage_cost_pct = storage_bytes / total_db_size if total_db_size > 0 else 0.0
    
    benefit = exec_time_pct * similarity + avg_cpu + max_cpu - storage_cost_pct
    return benefit


def optimize_self_joins(
    candidates: List[dict],
    query_metrics: Dict[str, Dict],
    total_metrics: Dict[str, float],
    total_db_size: int,
    measure_storage_fn: callable,
) -> List[dict]:
    """
    For each candidate with self-joins, create a stripped version,
    measure both storage costs, compute benefits, and keep the
    higher-benefit version.
    
    Args:
        candidates: List of candidate view dicts (from merged output)
        query_metrics: {query_id: {execution_time, cpu_mean, cpu_max}}
        total_metrics: {exec_time, cpu_mean, cpu_max} - global totals
        total_db_size: Database size in bytes
        measure_storage_fn: Callable(view_sql) -> int (storage bytes)
    
    Returns:
        Optimized candidate list (some candidates replaced by
        their self-join-stripped counterparts)
    """
    optimized = []
    
    stats = {
        "total_with_self_joins": 0,
        "stripped_kept": 0,
        "original_kept": 0,
        "failed": 0,
    }
    
    for c in candidates:
        tables = set(c.get("tables", []))
        
        if not _needs_stripping(tables):
            optimized.append(c)
            continue
        
        stats["total_with_self_joins"] += 1
        self_joins = detect_self_joins(tables)
        
        # Create stripped version
        stripped = strip_self_joins(c)
        if stripped is None:
            optimized.append(c)
            stats["failed"] += 1
            continue
        
        # Get SQL for both
        orig_sql = c.get("view_sql", c.get("sql", ""))
        stripped_sql = stripped.get("view_sql", stripped.get("sql", ""))
        
        # Measure storage for both
        orig_storage = measure_storage_fn(orig_sql)
        stripped_storage = measure_storage_fn(stripped_sql)
        
        if orig_storage == 0 and stripped_storage == 0:
            # Neither can be materialized — keep original
            optimized.append(c)
            stats["failed"] += 1
            continue
        
        # If stripped version has 0 storage (can't measure), skip comparison
        if stripped_storage == 0:
            optimized.append(c)
            stats["original_kept"] += 1
            continue
        
        # Compute benefits
        orig_benefit = compute_benefit_for_candidate(
            c, query_metrics, total_metrics, orig_storage, total_db_size
        )
        stripped_benefit = compute_benefit_for_candidate(
            stripped, query_metrics, total_metrics, stripped_storage, total_db_size
        )
        
        if stripped_benefit > orig_benefit:
            stripped["_original_benefit"] = round(orig_benefit, 6)
            stripped["_stripped_benefit"] = round(stripped_benefit, 6)
            stripped["_original_storage"] = orig_storage
            stripped["_stripped_storage"] = stripped_storage
            stripped["_self_joins"] = dict(self_joins)
            optimized.append(stripped)
            stats["stripped_kept"] += 1
        else:
            c["_self_join_analysis"] = {
                "has_self_joins": dict(self_joins),
                "stripped_benefit": round(stripped_benefit, 6),
                "original_benefit": round(orig_benefit, 6),
                "stripped_storage": stripped_storage,
                "original_storage": orig_storage,
                "kept_original": True,
            }
            optimized.append(c)
            stats["original_kept"] += 1
    
    # Log stats
    sj = stats["total_with_self_joins"]
    kept = stats["stripped_kept"]
    print(f"[Self-Join Optimizer] {sj} candidates with self-joins")
    print(f"  Stripped: {kept} (higher benefit), "
          f"Original kept: {stats['original_kept']}, "
          f"Failed: {stats['failed']}")
    
    return optimized


if __name__ == "__main__":
    # Quick test
    test_sql = """
SELECT n1.n_name AS supp_nation, n2.n_name AS cust_nation,
       EXTRACT(YEAR FROM l_shipdate) AS l_year,
       l_extendedprice * (1 - l_discount) AS volume
FROM nation n1, nation n2, lineitem, supplier, orders, customer
WHERE s_suppkey = l_suppkey
  AND o_orderkey = l_orderkey
  AND c_custkey = o_custkey
  AND s_nationkey = n1.n_nationkey
  AND c_nationkey = n2.n_nationkey
  AND l_shipdate BETWEEN '1992-01-01' AND '1992-12-31'
"""
    
    test_candidate = {
        "tables": ["nation:n1", "nation:n2", "lineitem", "supplier",
                   "orders", "customer"],
        "join_pairs": [
            ("nation:n1", "supplier"),
            ("nation:n2", "customer"),
            ("lineitem", "orders"),
            ("lineitem", "supplier"),
            ("customer", "orders"),
        ],
        "filters": {
            "lineitem": ["l_shipdate BETWEEN '1992-01-01' AND '1992-12-31'"]
        },
        "aggregates": [],
        "groupby_cols": [],
        "view_sql": test_sql,
        "sql": test_sql,
        "label": "L1-JOINS-customer_lineitem_...",
    }
    
    sj = detect_self_joins(set(test_candidate["tables"]))
    print(f"Self-joins detected: {sj}")
    
    stripped = strip_self_joins(test_candidate)
    if stripped:
        print(f"\nOriginal SQL:\n{test_sql[:200]}")
        print(f"\nStripped SQL:\n{stripped.get('view_sql', '')[:200]}")
