"""
Step 3 — Cost/Benefit Estimator
================================

Scores every candidate view against a query workload using a composite
benefit function that balances execution-time savings, CPU reduction, and
storage cost.

Benefit function
────────────────
benefit(candidate_view_i) =
    ((execution_time% + cpu_mean% + cpu_max%) / 3)
    × similarity_score
    ─  (storage_cost% / 10)

Where:
  execution_time%(i) =
      Σ execution_time of queries covered by candidate_view_i
      ──────────────────────────────────────────────────────
      Σ execution_time of all workload queries

  cpu_mean%(i) = average CPU_percentage_mean over covered queries
  cpu_max%(i)  = average CPU_percentage_max over covered queries

  storage_cost%(i) =
      estimated storage cost of candidate_view_i
      ──────────────────────────────────────────
      storage budget (20% of database size)

Data sources
────────────
  result_tpch.json         → execution_time, CPU_percentage_mean,
                             CPU_percentage_max per query_id
  final_candidates_tpch.json → candidate views with covered query IDs,
                               avg similarity scores, SQL, and schema info

Public API
──────────
  parse_sql(sql)              → (tables, cols_per_table, predicates)
  estimate_column_count(sql)  → int  (number of SELECT-level columns)
  compute_benefits(candidates, result_data, candidates_meta)
                              → (benefits, sorted_indices)
  get_top_k(sorted_indices, k) → List[int]
"""

from __future__ import annotations

import json
import math
import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

import schemas as _schema_module

# ─────────────────────────────────────────────────────────────────────────────
# Dynamic schema helpers — derive from active schema (TPC-H or TPC-DS) at call time
# ─────────────────────────────────────────────────────────────────────────────


def _build_prefix_to_table() -> Dict[str, str]:
    """Build prefix → table map from the active schema's columns.
    TPC-H: l_→lineitem, o_→orders, …  TPC-DS: ss_→store_sales, sr_→store_returns, …"""
    pmap: Dict[str, str] = {}
    for tbl, cols in _schema_module.ACTIVE.column_schema.items():
        short = tbl.split(".")[-1].lower()
        if not cols:
            continue
        sample = next(iter(cols)).lower()
        if "_" in sample and not sample.startswith("_"):
            pmap[sample.split("_")[0] + "_"] = short
        else:
            pmap[short + "_"] = short
    return pmap


def _build_all_tables() -> Set[str]:
    return set(_schema_module.ACTIVE.table_stats.keys())


def _build_known_cols() -> Set[str]:
    cols: Set[str] = set()
    for tbl, col_set in _schema_module.ACTIVE.column_schema.items():
        for c in col_set:
            cols.add(c.lower())
    return cols


def _get_total_db_columns() -> int:
    return len(_build_known_cols())


# Lazy caches — computed once after pipeline sets the schema
_PREFIX_TO_TABLE_CACHE: Dict[str, str] | None = None
_ALL_TABLES_CACHE: Set[str] | None = None
_KNOWN_COLS_CACHE: Set[str] | None = None


def _get_prefix_to_table() -> Dict[str, str]:
    global _PREFIX_TO_TABLE_CACHE
    if _PREFIX_TO_TABLE_CACHE is None:
        _PREFIX_TO_TABLE_CACHE = _build_prefix_to_table()
    return _PREFIX_TO_TABLE_CACHE


def _get_all_tables() -> Set[str]:
    global _ALL_TABLES_CACHE
    if _ALL_TABLES_CACHE is None:
        _ALL_TABLES_CACHE = _build_all_tables()
    return _ALL_TABLES_CACHE


def _get_known_cols() -> Set[str]:
    global _KNOWN_COLS_CACHE
    if _KNOWN_COLS_CACHE is None:
        _KNOWN_COLS_CACHE = _build_known_cols()
    return _KNOWN_COLS_CACHE


# Legacy module-level names for backwards compatibility
_PREFIX_TO_TABLE = _get_prefix_to_table
_ALL_TABLES = _get_all_tables
_KNOWN_COLS = _get_known_cols
TOTAL_DB_COLUMNS = _get_total_db_columns()

# Storage budget fraction of total database size
STORAGE_BUDGET_FRACTION = 0.20


# ─────────────────────────────────────────────────────────────────────────────
# SQL parsing (kept for compatibility — used by other pipeline steps)
# ─────────────────────────────────────────────────────────────────────────────

_Signature = Tuple[Set[str], Dict[str, Set[str]], Set[str]]


def parse_sql(sql: str) -> _Signature:
    """
    Parse a SQL statement and return its structural signature.

    Returns
    -------
    tables         : canonical TPC-H table names referenced in FROM / JOIN
    cols_per_table : {table: set(column_names)} — real schema columns only
    where_predicates : set of WHERE clause predicates (normalized string form)
    """
    from sqlglot import exp, parse_one

    try:
        tree = parse_one(sql)
    except Exception:
        return set(), {}, set()

    alias_map: Dict[str, str] = {}
    for node in tree.find_all(exp.Table):
        if node.alias:
            alias_map[node.alias.lower()] = node.name.lower()

    def _resolve(name: str) -> str:
        return alias_map.get(name, name)

    # Build reverse map: real_name -> set of aliases
    reverse_alias: Dict[str, Set[str]] = defaultdict(set)
    for ali, real in alias_map.items():
        reverse_alias[real].add(ali)

    all_tables = _ALL_TABLES() if callable(_ALL_TABLES) else _ALL_TABLES
    tables: Set[str] = set()
    for node in tree.find_all(exp.Table):
        real = node.name.lower()
        alias = _resolve(node.alias.lower() if node.alias else real)
        canonical = alias if alias in all_tables else real
        if canonical in all_tables:
            tables.add(canonical)

    select_aliases: Set[str] = {
        expr.alias.lower()
        for sel in tree.find_all(exp.Select)
        for expr in sel.expressions
        if expr.alias
    }

    known_cols = _KNOWN_COLS() if callable(_KNOWN_COLS) else _KNOWN_COLS
    prefix_to_table = _PREFIX_TO_TABLE() if callable(_PREFIX_TO_TABLE) else _PREFIX_TO_TABLE
    cols: Dict[str, Set[str]] = defaultdict(set)
    for col in tree.find_all(exp.Column):
        col_name = col.name.lower()
        if col_name in select_aliases:
            continue
        tbl_ref = col.table.lower() if col.table else ""
        canonical_tbl = _resolve(tbl_ref) if tbl_ref else ""
        if canonical_tbl and canonical_tbl in tables:
            if col_name in known_cols:
                cols[canonical_tbl].add(col_name)
        elif not tbl_ref and col_name in known_cols:
            for prefix, tbl in prefix_to_table.items():
                if col_name.startswith(prefix) and tbl in tables:
                    cols[tbl].add(col_name)
                    break

    predicates: Set[str] = set()
    select_nodes = list(tree.find_all(exp.Select))
    for select_node in select_nodes:
        where_clause = select_node.args.get("where")
        if where_clause:
            if isinstance(where_clause, exp.Where):
                where_expr = where_clause.this
            else:
                where_expr = where_clause

            def extract_and_conditions(expr: exp.Expression) -> List[str]:
                if expr is None:
                    return []
                if isinstance(expr, exp.And):
                    return extract_and_conditions(expr.left) + extract_and_conditions(expr.right)
                try:
                    sql_str = expr.sql().lower()
                    return [sql_str] if sql_str.strip() else []
                except Exception:
                    return []

            predicates.update(extract_and_conditions(where_expr))

    return tables, dict(cols), predicates


# ─────────────────────────────────────────────────────────────────────────────
# Storage cost estimation
# ─────────────────────────────────────────────────────────────────────────────

def _extract_select_columns(sql: str) -> int:
    """
    Count the number of columns / expressions in the SELECT list.

    Uses a simple heuristic: counts comma-separated items between SELECT
    and FROM (handling nested subqueries by tracking parenthesis depth).
    """
    try:
        from sqlglot import exp, parse_one
        tree = parse_one(sql)
        col_count = 0
        for sel in tree.find_all(exp.Select):
            col_count += len(sel.expressions)
        return max(col_count, 1)  # at least 1
    except Exception:
        # Fallback: rough regex count
        match = re.search(
            r"\bSELECT\s+(.+?)\bFROM\b",
            sql, re.IGNORECASE | re.DOTALL
        )
        if match:
            items = match.group(1).strip()
            # Guard against DISTINCT / TOP etc.
            items = re.sub(r"\b(DISTINCT|TOP\s+\d+|ALL)\b", "", items, flags=re.IGNORECASE).strip()
            if not items:
                return 1
            # Count top-level commas (ignore those inside parentheses)
            depth = 0
            count = 1
            for ch in items:
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                elif ch == "," and depth == 0:
                    count += 1
            return count
        return 1


def estimate_view_storage_cost(sql: str, tables: List[str]) -> float:
    """
    Estimate the storage cost of a materialized view.

    Uses the number of SELECT-level columns * number of unique base tables as a proxy.
    Strips alias qualifiers (``table:alias`` → ``table``) to avoid
    double-counting in self-join scenarios.

    This is a heuristic — real storage cost depends on row count and data
    types, but column × table count serves as a reasonable relative proxy.
    """
    n_cols = _extract_select_columns(sql)
    # Strip aliases: lineitem:a, lineitem:b → {lineitem}
    base_tables = set()
    for t in tables:
        base = t.split(':')[0] if ':' in t else t
        base_tables.add(base)
    n_tables = max(len(base_tables), 1)
    return n_cols * n_tables


def compute_storage_cost_pct(
    view_storage_cost: float,
    total_db_storage_cost: float,
    budget_fraction: float = STORAGE_BUDGET_FRACTION,
) -> float:
    """
    Storage cost as a percentage of the storage budget.

    storage_cost% = view_storage_cost / (budget_fraction × total_db_storage_cost)

    Parameters
    ----------
    view_storage_cost      : estimated storage cost of this view
    total_db_storage_cost  : estimated storage cost of the full database
    budget_fraction        : fraction of database size allocated as budget (default 0.20)

    Returns
    -------
    Float — ratio of view cost to allocated budget.
    A value > 1.0 means the view exceeds the storage budget.
    """
    budget = budget_fraction * total_db_storage_cost
    if budget <= 0:
        return 0.0
    return view_storage_cost / budget


# ─────────────────────────────────────────────────────────────────────────────
# Core benefit computation
# ─────────────────────────────────────────────────────────────────────────────

def _compute_total_db_storage_cost(candidates: List[dict]) -> float:
    """
    Estimate the total database storage cost as the max across all candidates.

    This represents the full database size — the largest view is the closest
    approximation to a full-table scan / database-wide storage baseline.
    """
    # Use total distinct columns across the active schema as the baseline
    total_cols = _get_total_db_columns() if callable(_get_total_db_columns) else TOTAL_DB_COLUMNS
    n_tables = len(_build_all_tables())
    return total_cols * n_tables


def compute_benefits(
    candidates: List[dict],
    result_data: List[dict],
    candidates_meta: dict,
    storage_budget_fraction: float = STORAGE_BUDGET_FRACTION,
) -> Tuple[List[float], List[int]]:
    """
    Compute the benefit score for every candidate view.

    This replaces the old frequency-counting logic with the cost/benefit
    formula:

      benefit = ((execution_time% + cpu_mean% + cpu_max%) / 3)
                × similarity_score
                ─ (storage_cost% / 10)

    Parameters
    ----------
    candidates                  : list of view dicts with "sql", "tables", etc.
                                  (as produced by step 2)
    result_data                 : list of dicts from result_tpch.json with
                                  keys: "query_id", "execution_time",
                                  "CPU_percentage_mean", "CPU_percentage_max"
    candidates_meta             : dict from final_candidates_tpch.json —
                                  the "candidate_views" key mapping view_id
                                  to metadata including "view_covered_query_ids",
                                  "view_avg_similarity_score", "view_tables"
    storage_budget_fraction     : fraction of total database size used as
                                  storage budget (default 0.20)

    Mutates each candidate dict in-place by adding / updating:
      - "benefit"
      - "execution_time_pct"
      - "storage_cost_pct"
      - "avg_cpu"
      - "cpu_mean_pct"
      - "cpu_max_pct"
      - "similarity_score"

    Returns
    -------
    benefits       : List[float]  — benefit score per candidate
    sorted_indices : List[int]    — candidate indices sorted by benefit DESC
    """
    import json

    # ── Build lookup: query_id → metrics ──────────────────────────────────
    query_metrics: Dict[str, dict] = {}
    for rec in result_data:
        qid = rec["query_id"]
        query_metrics[qid] = {
            "execution_time": rec["execution_time"],
            "cpu_mean": rec["CPU_percentage_mean"],
            "cpu_max": rec["CPU_percentage_max"],
        }

    # ── Total execution time across all queries ────────────────────────────
    total_exec_time = sum(
        rec["execution_time"] for rec in result_data
    )

    # ── Total database storage cost (baseline) ─────────────────────────────
    total_db_storage_cost = _compute_total_db_storage_cost(candidates)

    # ── Pre-Warm candidate meta lookup (view_id → covered_query_ids) ──────
    # The candidates_meta dict might have view IDs as keys or be nested
    meta_lookup: Dict[str, dict] = {}
    if isinstance(candidates_meta, dict):
        if "candidate_views" in candidates_meta:
            meta_lookup = candidates_meta["candidate_views"]
        elif all(
            isinstance(v, dict) and "view_covered_query_ids" in v
            for v in candidates_meta.values()
        ):
            meta_lookup = candidates_meta
        # Also try flat list
        elif isinstance(candidates_meta.get("candidate_views"), list):
            for entry in candidates_meta["candidate_views"]:
                if isinstance(entry, dict) and "view_id" in entry:
                    meta_lookup[entry["view_id"]] = entry

    # Build a set-based lookup of view_id → covered_query_ids for isin checks
    covered_query_sets: Dict[str, set] = {}
    similarity_scores: Dict[str, float] = {}
    for vid, meta in meta_lookup.items():
        qids = meta.get("view_covered_query_ids", meta.get("covered_query_ids", []))
        covered_query_sets[vid] = set(
            str(q) for q in qids if q
        )
        similarity_scores[vid] = float(
            meta.get("view_avg_similarity_score", meta.get("similarity_score", 0.0))
        )
        # Also store tables from meta
        meta.setdefault("view_tables", meta.get("tables", []))

    print(f"  Loaded metrics for {len(query_metrics)} queries (total exec time: {total_exec_time:.4f}s)", flush=True)
    print(f"  Loaded meta for {len(meta_lookup)} candidate views", flush=True)

    print(f"  Computing benefits for {len(candidates)} candidates …", flush=True)

    benefits: List[float] = []

    for i, candidate in enumerate(candidates):
        sql = candidate.get("sql", "").strip()
        view_id = candidate.get("view_id", f"candidate_{i}")
        tables = candidate.get("tables", [])

        # ── Execution time % ───────────────────────────────────────────────
        covered_qids: Set[str] = set()

        # Try multiple sources for covered query IDs
        if view_id in covered_query_sets:
            covered_qids = covered_query_sets[view_id]

        # Also check candidate's own covered_query_ids field
        candidate_qids = candidate.get("view_covered_query_ids",
                         candidate.get("covered_query_ids", []))
        if candidate_qids:
            covered_qids |= set(str(q) for q in candidate_qids)

        # Compute execution time of covered queries
        covered_exec_time = sum(
            query_metrics[qid]["execution_time"]
            for qid in covered_qids
            if qid in query_metrics
        )

        exec_time_pct = covered_exec_time / total_exec_time if total_exec_time > 0 else 0.0

        # ── Similarity score ───────────────────────────────────────────────
        similarity = 0.0
        if view_id in similarity_scores:
            similarity = similarity_scores[view_id]
        else:
            # Fallback: use candidate field or average
            candidate_sim = candidate.get("view_avg_similarity_score",
                          candidate.get("similarity_score", 0.0))
            similarity = float(candidate_sim)

        # ── CPU percentages (mean and max separately) ───────────────────────
        cpu_mean_values: List[float] = [
            query_metrics[qid]["cpu_mean"]
            for qid in covered_qids
            if qid in query_metrics
        ]
        cpu_max_values: List[float] = [
            query_metrics[qid]["cpu_max"]
            for qid in covered_qids
            if qid in query_metrics
        ]

        cpu_mean_pct = sum(cpu_mean_values) / len(cpu_mean_values) if cpu_mean_values else 0.0
        cpu_max_pct = sum(cpu_max_values) / len(cpu_max_values) if cpu_max_values else 0.0

        # Normalize CPU percentages to 0-1 range (same range as exec_time_pct)
        cpu_mean_norm = cpu_mean_pct / 100.0
        cpu_max_norm = cpu_max_pct / 100.0

        # ── Storage cost % ─────────────────────────────────────────────────
        view_storage_cost = estimate_view_storage_cost(sql, tables)
        storage_cost_pct = compute_storage_cost_pct(
            view_storage_cost, total_db_storage_cost, storage_budget_fraction
        )

        # ── Final benefit ──────────────────────────────────────────────────
        # All terms are in 0-1 range
        benefit = ((exec_time_pct + cpu_mean_norm + cpu_max_norm) / 3.0) * similarity - (storage_cost_pct / 10.0)

        benefits.append(benefit)

        # Mutate in-place for downstream use
        candidate["benefit"] = benefit
        candidate["execution_time_pct"] = exec_time_pct
        candidate["covered_exec_time"] = covered_exec_time
        candidate["covered_query_count"] = len(covered_qids)
        candidate["storage_cost_pct"] = storage_cost_pct
        candidate["avg_cpu"] = (cpu_mean_norm + cpu_max_norm) / 2.0
        candidate["cpu_mean_pct"] = cpu_mean_pct
        candidate["cpu_max_pct"] = cpu_max_pct
        candidate["similarity_score"] = similarity

        if (i + 1) % 200 == 0:
            print(f"    {i + 1}/{len(candidates)} candidates scored", flush=True)

    # ── Tiebreaker: for equal benefits, rank by covered query count ────────
    def _tiebreak(i: int) -> tuple:
        c = candidates[i]
        return (
            benefits[i],
            c.get("covered_query_count", 0),
            c.get("execution_time_pct", 0.0),
        )

    sorted_indices = sorted(
        range(len(benefits)),
        key=_tiebreak,
        reverse=True,
    )

    return benefits, sorted_indices


def get_top_k(sorted_indices: List[int], k: int) -> List[int]:
    """Return the first *k* indices from a pre-sorted (DESC) index list."""
    return sorted_indices[: max(1, min(k, len(sorted_indices)))]


# ─────────────────────────────────────────────────────────────────────────────
# Standalone entry point
# ─────────────────────────────────────────────────────────────────────────────

def main():
    """
    Load data files, compute benefits, and print a ranking summary.

    Usage:
        python step3_Cost-Benefit-Estimator.py
    """
    import os
    import sys

    # Resolve paths relative to this script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    result_path = os.path.join(script_dir, "result_tpch.json")
    candidates_path = os.path.join(script_dir, "final_candidates_tpch.json")

    print(f"  Loading result data from {result_path}")
    with open(result_path, "r") as f:
        result_data = json.load(f)

    print(f"  Loading candidates meta from {candidates_path}")
    with open(candidates_path, "r") as f:
        candidates_meta = json.load(f)

    # Build candidates list from the candidate_views dict
    cv = candidates_meta.get("candidate_views", candidates_meta)
    candidates = []
    for vid, meta in cv.items():
        if isinstance(meta, dict):
            candidate = {
                "view_id": vid,
                "sql": meta.get("view_sql", meta.get("sql", "")),
                "tables": meta.get("view_tables", meta.get("tables", [])),
                "view_covered_query_ids": meta.get("view_covered_query_ids", []),
                "view_avg_similarity_score": meta.get("view_avg_similarity_score", 0.0),
            }
            candidates.append(candidate)

    print(f"\n{'='*60}")
    print(f"  Cost/Benefit Estimator — {len(candidates)} candidate views")
    print(f"  Storage budget: {STORAGE_BUDGET_FRACTION*100:.0f}% of database")
    print(f"  DB baseline: {TOTAL_DB_COLUMNS} columns × 8 tables")
    print(f"{'='*60}\n")

    benefits, sorted_indices = compute_benefits(
        candidates, result_data, candidates_meta
    )

    print(f"\n{'='*60}")
    print(f"  Top-20 candidate views by benefit score")
    print(f"{'='*60}")
    print(f"  {'Rank':<6} {'View ID':<45} {'Benefit':<10} {'Exec%':<8} {'CPU':<8} {'Stor%':<8} {'Sim':<8} {'#Q':<6}")
    print(f"  {'─'*6} {'─'*45} {'─'*10} {'─'*8} {'─'*8} {'─'*8} {'─'*8} {'─'*6}")

    for rank, idx in enumerate(sorted_indices[:20], 1):
        c = candidates[idx]
        vid = c["view_id"]
        benefit = c["benefit"]
        et_pct = c["execution_time_pct"]
        avg_cpu = c["avg_cpu"]
        stor_pct = c["storage_cost_pct"]
        sim = c["similarity_score"]
        nq = c["covered_query_count"]
        print(f"  {rank:<6} {vid:<45} {benefit:<10.4f} {et_pct:<8.4f} {avg_cpu:<8.4f} {stor_pct:<8.4f} {sim:<8.4f} {nq:<6}")

    print(f"\n  Scores written to candidate dicts (benefit, execution_time_pct, avg_cpu, storage_cost_pct)")

    # Optionally write back to final_candidates_tpch.json
    # Build the updated candidates_meta
    for c in candidates:
        vid = c["view_id"]
        if vid in cv:
            cv[vid]["benefit"] = c["benefit"]
            cv[vid]["execution_time_pct"] = c["execution_time_pct"]
            cv[vid]["storage_cost_pct"] = c["storage_cost_pct"]
            cv[vid]["avg_cpu"] = c["avg_cpu"]
            cv[vid]["cpu_mean_pct"] = c["cpu_mean_pct"]
            cv[vid]["cpu_max_pct"] = c["cpu_max_pct"]
            cv[vid]["benefit_score"] = c["benefit"]

    output_path = os.path.join(script_dir, "final_candidates_tpch.json")
    # Preserve the original structure
    if "candidate_views" in candidates_meta:
        candidates_meta["candidate_views"] = cv
    else:
        candidates_meta = {"candidate_views": cv}

    # Remove pipeline_info from the output if present (only update candidate views)
    original = json.load(open(candidates_path))
    if "pipeline_info" in original:
        candidates_meta["pipeline_info"] = original["pipeline_info"]

    with open(output_path, "w") as f:
        json.dump(candidates_meta, f, indent=2)
    print(f"  Updated scores written to {output_path}")


if __name__ == "__main__":
    main()
