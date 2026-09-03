#!/usr/bin/env python3
"""
GreenVIEW Pipeline — Reconstructed
====================================

Pipeline order:
  1. candidate_views_extractor     — Extract L0–L7 candidates per query
  2. candidate_views_merger        — Merge structurally similar candidates
  3. view_collections              — Compute coverage & group views into collections
  4. sql_embedding_similarity      — Score (view, query) pairs via neural embeddings
  5. cost_benefit_estimator        — Compute cost/benefit score per view

Output (final_candidate_views):
  Collections of non-redundant views, each view with cost/benefit score,
  ordered by SUM(all view_scores) DESC.

Usage:
    python pipeline.py [tpch|tpcds]
"""
import sys
import os
import json
import time
from typing import Dict, List, Set
from collections import Counter
try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable, **kwargs):
        """Fallback: simple iterate without progress bar."""
        for item in iterable:
            yield item

# Force offline mode for HuggingFace (avoids SSL/network failures)
os.environ.setdefault('HF_HUB_OFFLINE', '1')
os.environ.setdefault('TRANSFORMERS_OFFLINE', '1')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 1)

import schemas as _sch
from schemas import TPCH, TPCDS

# ── Parse arguments ─────────────────────────────────────────────────────────
DB_ARGS = {"tpch", "tpcds", "tpc-h", "tpc-ds", "tpc_h", "tpc_ds"}
DB_NAME = (sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].lower().replace("-", "_") in DB_ARGS
           else "tpch").lower().replace("-", "_")

USE_TPCH  = DB_NAME == "tpch"
USE_TPCDS = DB_NAME == "tpcds"

if USE_TPCH:
    _sch.ACTIVE = TPCH
    from tpch_workload import workload_1 as WORKLOAD
    CACHE_PATH    = os.path.join(os.path.dirname(__file__), "step1_cache_tpch.json")
    RESULT_PATH   = os.path.join(os.path.dirname(__file__), "time_cpu_tpch.json")
    INTERIM_PATH  = os.path.join(os.path.dirname(__file__), "interim_merged_tpch.json")
    EMBED_PATH    = os.path.join(os.path.dirname(__file__), "interim_embeddings_tpch.json")
    COLLECT_PATH  = os.path.join(os.path.dirname(__file__), "interim_collections_tpch.json")
    FINAL_OUTPUT  = os.path.join(os.path.dirname(__file__), "final_candidate_views_tpch.json")
else:
    _sch.ACTIVE = TPCDS
    from tpcds_workload import workload_1 as WORKLOAD
    CACHE_PATH    = os.path.join(os.path.dirname(__file__), "step1_cache_tpcds.json")
    RESULT_PATH   = os.path.join(os.path.dirname(__file__), "time_cpu_tpcds.json")
    INTERIM_PATH  = os.path.join(os.path.dirname(__file__), "interim_merged_tpcds.json")
    EMBED_PATH    = os.path.join(os.path.dirname(__file__), "interim_embeddings_tpcds.json")
    COLLECT_PATH  = os.path.join(os.path.dirname(__file__), "interim_collections_tpcds.json")
    FINAL_OUTPUT  = os.path.join(os.path.dirname(__file__), "final_candidate_views_tpcds.json")

# ─────────────────────────────────────────────────────────────────────────────
# Imports per step
# ─────────────────────────────────────────────────────────────────────────────
from step1_candidates_extractor import extract as step1_extract
from step2_global_candidates_merger import merge as step2_merge

from sql_embeddings import (
    parse_sql_object, SQLObject, TableStats,
    compute_weights, extract_components,
    view_query_similarity, ComponentEmbedder,
)

from step2b_view_collections import build_collections as step4_build_collections
from step2b_view_collections import is_subset_related as _is_subset_related
import importlib.util

# step3 file has hyphens — dynamic import (cannot use regular import)
_spec3 = importlib.util.spec_from_file_location(
    "step3_mod", os.path.join(os.path.dirname(__file__), "step3_Cost-Benefit-Estimator.py"))
_step3_mod = importlib.util.module_from_spec(_spec3)
_spec3.loader.exec_module(_step3_mod)
parse_sql = _step3_mod.parse_sql


# ── Logging helper ──────────────────────────────────────────────────────────

def log(msg):
    print(msg, flush=True)


def banner(title):
    n = 70
    log("")
    log("═" * n)
    log(f"  {title}")
    log("═" * n)


# ── Step 1 helpers ──────────────────────────────────────────────────────────

def _candidate_to_dict(c):
    """Convert a CandidateView dataclass to dict if needed."""
    if hasattr(c, 'sql'):
        return {
            "sql": c.sql,
            "level": c.level,
            "label": c.label,
            "source_sql": c.source_sql,
            "source_query": getattr(c, 'source_query', 'global'),
            "tables": list(c.tables),
            "join_pairs": list(c.join_pairs),
            "join_predicates": list(c.join_predicates) if hasattr(c, "join_predicates") and c.join_predicates else [],
            "filters": {k: list(v) for k, v in c.filters.items()},
            "aggregates": list(c.aggregates),
            "groupby_cols": list(c.groupby_cols),
        }
    return c


# ── Step 3 helpers ──────────────────────────────────────────────────────────

# ── Multi-dimensional coverage helpers ──────────────────────────────────
import re

def _extract_between_ranges(predicates: Set[str]) -> Dict[str, tuple]:
    """
    Extract date-range boundaries from BETWEEN predicates.

    Returns {column: (lower, upper)} where lower/upper are comparable values
    (typically date strings like '1992-01-01').
    """
    ranges: Dict[str, tuple] = {}
    pattern = re.compile(
        r"\b(\w+)\s+BETWEEN\s+'([^']+)'\s+AND\s+'([^']+)'",
        re.IGNORECASE
    )
    for p in predicates:
        m = pattern.search(p)
        if m:
            col, lo, hi = m.groups()
            ranges[col.lower()] = (lo, hi)
    return ranges


def _ranges_subsume(view_ranges: Dict[str, tuple],
                    query_ranges: Dict[str, tuple]) -> bool:
    """
    Check that view date ranges cover query date ranges for every
    overlapping column.
    """
    for col, (q_lo, q_hi) in query_ranges.items():
        if col in view_ranges:
            v_lo, v_hi = view_ranges[col]
            # Query range must be inside view range
            if q_lo < v_lo or q_hi > v_hi:
                return False
    return True


def _columns_contain(view_cols: Dict[str, Set[str]],
                     query_cols: Dict[str, Set[str]]) -> bool:
    """
    Check that for every table the view and query share, the view
    includes ALL columns the query needs from that table.
    """
    for tbl, qcols in query_cols.items():
        if tbl in view_cols:
            if not qcols.issubset(view_cols[tbl]):
                return False
    return True


def _covered_queries(view_tables, view_cols, view_preds, parsed_workload):
    """
    Check each workload query for coverage by this view using multi-
    dimensional criteria:

      1. TABLE CONTAINMENT (reverse of old): the view must have ALL
         tables the query references (query_tables ⊆ view_tables).
      2. PREDICATE SUBSET: the view's date-range predicates must be
         at least as restrictive as the query's.  E.g. if the view
         filters ``l_shipdate BETWEEN '1992-01-01' AND '1992-12-31'``
         then a query asking about 1995 is NOT covered.
      3. COLUMN AVAILABILITY: for every shared table, the view must
         project all columns the query needs from that table.

    Returns (total_score, covered_ids_list).
    """
    view_ranges = _extract_between_ranges(view_preds)
    total = 0.0
    covered = []

    for j, (qt, qc, qp) in enumerate(parsed_workload):
        if not view_tables or not qt:
            continue

        # ── 1. Table containment (reverse direction) ──────────────
        # View must have ALL tables the query needs.
        if not qt.issubset(view_tables):
            continue

        # ── 2. Predicate compatibility ────────────────────────────
        if view_ranges:
            query_ranges = _extract_between_ranges(qp)
            if not _ranges_subsume(view_ranges, query_ranges):
                continue

        # ── 3. Column availability ────────────────────────────────
        if view_cols and qc:
            if not _columns_contain(view_cols, qc):
                continue

        # All checks passed → covered
        # Score is higher when table sets are more similar
        overlap_ratio = len(qt & view_tables) / len(qt)
        total += overlap_ratio
        covered.append(f"Q{j}")

    return total, covered


def _make_view_id(candidate: dict) -> str:
    label = candidate.get('label', f"L{candidate.get('level', '?')}")
    return f"{label}_{candidate.get('source_query', 'global')}"


def _requires_exact_source_view(candidate: dict) -> bool:
    """Return whether a merged definition must fall back to its source SQL.

    Predicate broadening is only reusable when the materialized output retains
    enough row-level information to apply each original predicate afterwards.
    Aggregate, windowed, CTE, derived-table, and set-operation queries do not
    meet that condition generically, so exporting their merged SQL would not
    preserve source-query semantics.
    """
    source_sql = candidate.get("source_sql", "").strip().rstrip(";")
    merged_sql = candidate.get("sql", "").strip().rstrip(";")
    if not source_sql or not merged_sql or source_sql == merged_sql:
        return False
    try:
        from sqlglot import exp, parse_one

        tree = parse_one(source_sql)
    except Exception:
        return True
    return any(tree.find_all((exp.AggFunc, exp.Window, exp.CTE, exp.Subquery, exp.Union, exp.Intersect, exp.Except)))


def _preserve_semantic_view_definitions(candidates: List[dict]) -> None:
    """Replace unsafe merged SQL with exact source definitions in place."""
    for candidate in candidates:
        if not _requires_exact_source_view(candidate):
            continue
        source_query = candidate.get("source_query")
        candidate["view_sql"] = candidate["source_sql"].strip().rstrip(";")
        candidate["_covered_ids"] = [source_query] if source_query else []
        candidate["_avg_similarity"] = 1.0


def _extract_select_columns(sql: str) -> int:
    """Count SELECT-level columns/expressions in a SQL string."""
    try:
        from sqlglot import exp, parse_one
        tree = parse_one(sql)
        for sel in tree.find_all(exp.Select):
            return max(len(sel.expressions), 1)
        return 1
    except Exception:
        match = re.search(r"\bSELECT\s+(.+?)\bFROM\b", sql, re.IGNORECASE | re.DOTALL)
        if match:
            items = match.group(1).strip()
            items = re.sub(r"\b(DISTINCT|TOP\s+\d+|ALL)\b", "", items, flags=re.IGNORECASE).strip()
            if not items:
                return 1
            depth = 0
            count = 1
            for ch in items:
                if ch == "(": depth += 1
                elif ch == ")": depth -= 1
                elif ch == "," and depth == 0: count += 1
            return count
        return 1


# ─────────────────────────────────────────────────────────────────────────────
# ═══════════════════════════════════════════════════════════════════════════
# MAIN PIPELINE
# ═══════════════════════════════════════════════════════════════════════════
# ─────────────────────────────────────────────────────────────────────────────

def main():
    t0 = time.time()

    banner(f"GreenVIEW Pipeline — Reconstructed"
           f"\n  Database: {DB_NAME.upper()} ({len(WORKLOAD)} queries)"
           f"\n  Pipeline: Extract → Merge → Embed → Cost/Benefit → Collections")

    # ══════════════════════════════════════════════════════════════════════
    # STEP 1 — candidate_views_extractor
    # ══════════════════════════════════════════════════════════════════════
    banner("Step 1: candidate_views_extractor — Extract L0–L7 per query")

    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH) as f:
            cache = json.load(f)
        log(f"  Loaded cache: {len(cache)} query entries")
        flat = []
        for qkey, cands in cache.items():
            if not cands:
                continue
            for c in cands:
                if hasattr(c, 'sql'):
                    c = _candidate_to_dict(c)
                c['source_query'] = qkey
                flat.append(c)
        log(f"  {len(flat):,} candidates from cache")
    else:
        cache = {}
        errors = 0
        pbar = tqdm(WORKLOAD, desc="  Extracting", unit="q", ncols=80)
        for i, sql in enumerate(pbar):
            try:
                cands = step1_extract(sql, _sch.ACTIVE.table_stats, _sch.ACTIVE.column_schema)
                if cands:
                    cache[f"Q{i}"] = cands
                    pbar.set_postfix(cands=len(cands))
            except Exception as e:
                errors += 1
                pbar.set_postfix(err=f"Q{i}")
        pbar.close()
        with open(CACHE_PATH, 'w') as f:
            json.dump(cache, f)
        log(f"  Saved cache ({len(cache)} entries, {errors} errors)")

        flat = []
        for qkey, cands in cache.items():
            if not cands:
                continue
            for c in cands:
                if hasattr(c, 'sql'):
                    c = _candidate_to_dict(c)
                c['source_query'] = qkey
                flat.append(c)

    log(f"  Total raw candidates: {len(flat):,}")
    t1 = time.time()
    log(f"  Duration: {t1 - t0:.1f}s")

    # ══════════════════════════════════════════════════════════════════════
    # STEP 2 — candidate_views_merger
    # ══════════════════════════════════════════════════════════════════════
    banner("Step 2: candidate_views_merger — Merge structurally similar candidates")

    merged, merge_stats = step2_merge(flat)
    t2 = time.time()

    layer_counts = Counter()
    for c in merged:
        level = c.get('level', c.get('layer', -1))
        layer_counts[str(level)] += 1

    log(f"  Input: {merge_stats['input_count']:,} → Output: {len(merged):,}")
    log(f"  Perfect duplicates removed: {merge_stats['perfect_duplicates_removed']:,}")
    log(f"  Filter merges: {merge_stats.get('filter_merges', 0)}, "
        f"SELECT merges: {merge_stats.get('select_merges', 0)}")
    log(f"  By layer: {dict(layer_counts)}")
    log(f"  Duration: {t2 - t1:.1f}s")

    def _json_safe(value):
        if isinstance(value, dict):
            return {str(k): _json_safe(v) for k, v in value.items()}
        if isinstance(value, (list, tuple)):
            return [_json_safe(v) for v in value]
        if isinstance(value, set):
            return sorted(_json_safe(v) for v in value)
        return value

    # Save interim merged candidates
    with open(INTERIM_PATH, 'w') as f:
        json.dump(_json_safe(merged), f, indent=2)
    log(f"  Saved interim merged → {INTERIM_PATH}")

    # ── Frequency constraint: drop views with frequency < 2 ─────────────
    # A pattern appearing in only 1 query is too workload-specific.
    #
    # We identify views by (tables, joins, aggregates, groupby, level)
    # — deliberately EXCLUDING filters.  Filter merging can normalise
    # operators (``<=`` → ``<``) or drop low-selectivity filters
    # entirely (``p_name IN (10 values…)`` → ``(no filter)``), which
    # would break any filter-based signature.
    def _freq_sig(c: dict) -> tuple:
        return (
            tuple(sorted(c.get("tables", []))),
            tuple(sorted(tuple(sorted(p)) for p in c.get("join_pairs", []))),
            tuple(sorted(c.get("aggregates", []))),
            tuple(sorted(c.get("groupby_cols", []))),
            c.get("level", -1),
        )

    freq_map: Dict[tuple, int] = {}
    seen_raw: Set[tuple] = set()
    for c in flat:
        sig = _freq_sig(c)
        sq = c.get("source_query", "?")
        key = (sig, sq)
        if key not in seen_raw:
            seen_raw.add(key)
            freq_map[sig] = freq_map.get(sig, 0) + 1

    before_freq = len(merged)
    merged = [c for c in merged if freq_map.get(_freq_sig(c), 0) >= 2]
    dropped_freq = before_freq - len(merged)
    log(f"  Frequency constraint: {before_freq} → {len(merged)} "
        f"({dropped_freq} dropped, freq < 2)")

    # ══════════════════════════════════════════════════════════════════════
    # STEP 3 — sql_embedding_similarity (coverage + scoring)
    # ══════════════════════════════════════════════════════════════════════
    banner("Step 3: sql_embedding_similarity — Score views & compute coverage")

    # ── Compute per-view coverage using parse_sql ───────────────────────
    log(f"  Computing query coverage for {len(merged)} candidates …")
    parsed_workload = [parse_sql(q) for q in WORKLOAD]
    for i, c in enumerate(merged):
        sql = c.get("sql", "").strip()
        if not sql:
            c["_covered_ids"] = []
            continue
        vt, vc, vp = parse_sql(sql)
        _, covered = _covered_queries(vt, vc, vp, parsed_workload)
        c["_covered_ids"] = covered
        if (i + 1) % 100 == 0:
            log(f"    {i + 1}/{len(merged)} coverage computed")

    # ── Embedding similarity ────────────────────────────────────────────
    log(f"  Running batched neural embedding similarity scorer on {len(merged)} candidates …")

    import torch
    import torch.nn.functional as F

    embedder = ComponentEmbedder()
    ts = _sch.ACTIVE.table_stats

    log(f"  Parsing {len(merged)} candidates for embedding …")
    v_objects_raw = []
    v_sqls = []
    for c in merged:
        sql = c.get("sql", "").strip()
        v_sqls.append(sql)
        try:
            v_objects_raw.append(parse_sql_object(sql, ts, _sch.ACTIVE.column_schema))
        except Exception:
            v_objects_raw.append(None)

    log(f"  Parsing {len(WORKLOAD)} workload queries for embedding …")
    q_sqls = list(WORKLOAD)
    q_objects_raw = []
    for q in q_sqls:
        try:
            q_objects_raw.append(parse_sql_object(q, ts, _sch.ACTIVE.column_schema))
        except Exception:
            q_objects_raw.append(None)

    log(f"  Encoding all SQLs (batch) …")
    all_sqls = v_sqls + q_sqls
    all_embeddings = embedder.model.encode(all_sqls, convert_to_tensor=True, batch_size=64)
    n_views = len(v_sqls)
    v_embs = all_embeddings[:n_views]
    q_embs = all_embeddings[n_views:]

    v_embs = F.normalize(v_embs, dim=1)
    q_embs = F.normalize(q_embs, dim=1)

    log(f"  Computing {n_views} x {len(q_sqls)} similarity matrix …")
    sim_matrix = torch.mm(v_embs, q_embs.T)

    for i, c in enumerate(merged):
        scores = sim_matrix[i]
        v_obj = v_objects_raw[i]
        if v_obj is None:
            c["_avg_similarity"] = 0.0
            continue
        constrained_scores = []
        covered = c.get("_covered_ids", [])
        for qid in covered:
            try:
                j = int(qid.replace("Q", ""))
            except ValueError:
                continue
            if j >= len(q_objects_raw):
                continue
            q_obj = q_objects_raw[j]
            if q_obj is None:
                continue
            # ── Common-table column containment check ───────────────────
            # The view may cover only PART of this query (fewer tables).
            # We only check columns for the tables they SHARE.
            common_tables = v_obj.tables & q_obj.tables
            if not common_tables:
                continue
            cols_ok = True
            for table in common_tables:
                # columns the QUERY needs from this table (used in SELECT/WHERE/JOIN)
                query_cols_for_table = q_obj.columns_per_table.get(table, set())
                # columns the VIEW provides from this table
                view_cols_for_table  = v_obj.columns_per_table.get(table, set())
                # View must have ALL the columns the query needs from this shared table
                if not query_cols_for_table.issubset(view_cols_for_table):
                    cols_ok = False
                    break
            if not cols_ok:
                continue
            constrained_scores.append(scores[j].item())
        avg_sim = sum(constrained_scores) / max(len(constrained_scores), 1) if constrained_scores else 0.0
        c["_avg_similarity"] = max(0.0, float(avg_sim))

    _preserve_semantic_view_definitions(merged)

    def _json_safe(value):
        if isinstance(value, dict):
            return {str(k): _json_safe(v) for k, v in value.items()}
        if isinstance(value, (list, tuple)):
            return [_json_safe(v) for v in value]
        if isinstance(value, set):
            return sorted(_json_safe(v) for v in value)
        return value

    log(f"  Similarity scored: {len(merged)} candidates")
    with open(EMBED_PATH, 'w') as f:
        json.dump(_json_safe(merged), f, indent=2)
    log(f"  Saved interim embedding results -> {EMBED_PATH}")

    t3 = time.time()
    log(f"  Duration: {t3 - t2:.1f}s")

    # ══════════════════════════════════════════════════════════════════════
    # STEP 4 — cost_benefit_estimator
    # ══════════════════════════════════════════════════════════════════════
    banner("Step 4: cost_benefit_estimator — Score each view with cost/benefit")

    if os.path.exists(RESULT_PATH):
        with open(RESULT_PATH) as f:
            result_data = json.load(f)
        log(f"  Loaded result data: {len(result_data)} query metrics")
    else:
        result_data = []
        log(f"  WARNING: result data not found at {RESULT_PATH}")

    query_metrics = {}
    total_exec_time = 0.0
    total_cpu_mean = 0.0
    total_cpu_max = 0.0
    for rec in result_data:
        raw_qid = str(rec["query_id"]).upper().replace("Q", "")
        try:
            idx = int(raw_qid) - 1
        except ValueError:
            idx = len(query_metrics)
        norm_qid = f"Q{idx}"
        query_metrics[norm_qid] = {
            "execution_time": float(rec.get("execution_time", 0)),
            "cpu_mean": float(rec.get("CPU_percentage_mean", 0)),
            "cpu_max": float(rec.get("CPU_percentage_max", 0)),
        }
        total_exec_time += query_metrics[norm_qid]["execution_time"]
        total_cpu_mean += query_metrics[norm_qid]["cpu_mean"]
        total_cpu_max += query_metrics[norm_qid]["cpu_max"]

    log(f"  Totals - exec_time: {total_exec_time:.4f}s, "
        f"CPU_mean: {total_cpu_mean:.2f}, CPU_max: {total_cpu_max:.2f}")

    # ── Pre-compute per-table storage weight factors ───────────────────
    # Weight = row_count × num_columns (proxy for physical size)
    # The dominant table in a view determines its base storage cost.
    _table_weights: Dict[str, float] = {}
    _table_col_counts: Dict[str, int] = {}
    for t, ts in _sch.ACTIVE.table_stats.items():
        ncols = max(len(_sch.ACTIVE.column_schema.get(t, [])), 1)
        _table_weights[t] = ts.row_count * ncols
        _table_col_counts[t] = ncols
    _total_db_weight = sum(_table_weights.values())

    log(f"  Computing cost/benefit for {len(merged)} candidates ...")

    benefit_lookup = {}
    for c in merged:
        cid = _make_view_id(c)
        covered_ids = c.get("_covered_ids", [])
        similarity = c.get("_avg_similarity", 0.0)
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
        exec_time_pct = (covered_exec_time / total_exec_time) if total_exec_time > 0 else 0.0
        avg_cpu = (covered_cpu_mean / n_covered / 100.0) if n_covered > 0 else 0.0
        max_cpu_val = sum(covered_cpu_max_vals) if covered_cpu_max_vals else 0.0
        max_cpu = (max_cpu_val / n_covered / 100.0) if n_covered > 0 else 0.0

        # ── Storage cost: n_cols × n_tables, weighted by dominant table size ──
        # Views on large fact tables (lineitem, 6M rows) cost more than
        # views on small dimension tables (nation, 25 rows, or partsupp, 800K).
        n_cols = _extract_select_columns(c.get("view_sql", c.get("sql", "")))
        view_tables = c.get("view_tables", list(c.get("tables", [])))
        max_table_weight = 0
        max_table_cols = 1
        for tbl in view_tables:
            tname = tbl.split(":")[0] if ":" in tbl else tbl
            w = _table_weights.get(tname, 0)
            if w > max_table_weight:
                max_table_weight = w
                max_table_cols = _table_col_counts.get(tname, 1)
        # Baseline: original n_cols × n_tables / 200 heuristic
        base_storage = n_cols * max(len(view_tables), 1) / 200.0
        # Weight by how much of the database the dominant table consumes
        dominant_db_share = max_table_weight / _total_db_weight if _total_db_weight > 0 else 0.0
        storage_cost_pct = base_storage * dominant_db_share

        benefit = exec_time_pct * similarity + avg_cpu + max_cpu - storage_cost_pct
        benefit_lookup[cid] = {
            "benefit": round(benefit, 6),
            "execution_time_pct": round(exec_time_pct, 6),
            "avg_cpu": round(avg_cpu, 6),
            "max_cpu": round(max_cpu, 6),
            "storage_cost_pct": round(storage_cost_pct, 6),
            "similarity_score": round(similarity, 6),
            "covered_queries": len(covered_ids),
            "covered_exec_time": round(covered_exec_time, 4),
        }

    t4 = time.time()
    sorted_views = sorted(benefit_lookup.items(), key=lambda kv: -kv[1]["benefit"])
    log(f"  Top 5 views by cost/benefit score:")
    log(f"  {'view_id':<50} {'benefit':<10} {'exec%':<10} {'avg_cpu':<10} {'max_cpu':<10} {'stor%':<10}")
    log(f"  {'-'*90}")
    for vid, info in sorted_views[:5]:
        log(f"  {vid:<50} {info['benefit']:<10.4f} {info['execution_time_pct']:<10.4f} "
            f"{info['avg_cpu']:<10.6f} {info['max_cpu']:<10.6f} {info['storage_cost_pct']:<10.4f}")
    log(f"  Duration: {t4 - t3:.1f}s")

    # ══════════════════════════════════════════════════════════════════════
    # STEP 5 — view_collections
    # ══════════════════════════════════════════════════════════════════════
    banner("Step 5: view_collections — Group views into non-redundant collections")

    # Build metadata dict for the collection builder
    candidates_meta = {}
    for c in merged:
        cid = _make_view_id(c)
        joins = c.get("join_pairs", [])
        filters = c.get("filters", {})
        aggs = c.get("aggregates", [])
        n_filters = sum(len(v) for v in filters.values())
        complexity = len(joins) + n_filters + len(aggs)
        candidates_meta[cid] = {
            "view_id": cid,
            "view_sql": c.get("view_sql", c.get("sql", "")),
            "view_covered_query_ids": c.get("_covered_ids", []),
            "view_avg_similarity_score": c.get("_avg_similarity", 0.0),
            "view_tables": c.get("view_tables", []) or c.get("tables", []),
            "view_joins": joins,
            "view_join_predicates": c.get("join_predicates", []),
            "view_filters": filters,
            "view_aggregates": list(aggs),
            "view_complexity": complexity,
        }

    log(f"  Building collections from {len(candidates_meta)} candidates ...")
    collections = step4_build_collections({"candidate_views": candidates_meta})

    t5 = time.time()
    log(f"  Collections built: {len(collections)}")
    log(f"  Duration: {t5 - t4:.1f}s")
    # ══════════════════════════════════════════════════════════════════════
    # BUILD FINAL OUTPUT — Collections with scored views, ordered DESC
    # ══════════════════════════════════════════════════════════════════════
    banner("Building Final Candidate Views — Collections ordered by SUM(scores) DESC")

    final_collections = []
    for col in collections:
        scored_views = []
        for vid in col.view_ids:
            meta = candidates_meta.get(vid, {})
            score_info = benefit_lookup.get(vid, {})
            scored_views.append({
                "view_id": vid,
                "view_sql": meta.get("view_sql", ""),
                "view_tables": meta.get("view_tables", []),
                "view_joins": meta.get("view_joins", []),
                "view_join_predicates": meta.get("view_join_predicates", []),
                "view_filters": meta.get("view_filters", {}),
                "view_aggregates": meta.get("view_aggregates", []),
                "view_complexity": meta.get("view_complexity", 0),
                "covered_query_ids": meta.get("view_covered_query_ids", []),
                "avg_similarity_score": meta.get("view_avg_similarity_score", 0.0),
                "cost_benefit_score": score_info.get("benefit", 0.0),
                "execution_time_pct": score_info.get("execution_time_pct", 0.0),
                "storage_cost_pct": score_info.get("storage_cost_pct", 0.0),
                "avg_cpu": score_info.get("avg_cpu", 0.0),
                "max_cpu": score_info.get("max_cpu", 0.0),
            })
        # Sort views within collection by view_complexity DESC
        scored_views.sort(key=lambda v: -v["view_complexity"])

        total_score = sum(v["cost_benefit_score"] for v in scored_views)
        final_collections.append({
            "collection_id": col.collection_id,
            "size": col.size,
            "total_score": round(total_score, 6),
            "unique_queries_covered": len(col.all_covered),
            "views": scored_views,
        })

    # Order collections by total_score DESC
    final_collections.sort(key=lambda c: -c["total_score"])

    # Re-assign collection_id based on new order
    for i, col in enumerate(final_collections):
        col["collection_id"] = i

    final_output = {
        "pipeline_info": {
            "workload_size": len(WORKLOAD),
            "database": DB_NAME.upper(),
            "pipeline_order": [
                "1: candidate_views_extractor",
                "2: candidate_views_merger",
                "3: sql_embedding_similarity",
                "4: cost_benefit_estimator",
                "5: view_collections",
            ],
            "step1_raw_candidates": len(flat),
            "step2_merged_candidates": len(merged),
            "step3_embedding_scored": len(merged),
            "step4_cost_benefit_scored": len(benefit_lookup),
            "step5_collections": len(final_collections),
            "timing_s": {
                "step1_extract": round(t1 - t0, 1),
                "step2_merge": round(t2 - t1, 1),
                "step3_embedding": round(t3 - t2, 1),
                "step4_cost_benefit": round(t4 - t3, 1),
                "step5_collections": round(t5 - t4, 1),
                "total": round(t5 - t0, 1),
            },
        },
        "collections": final_collections,
    }

    with open(FINAL_OUTPUT, 'w') as f:
        json.dump(_json_safe(final_output), f, indent=2)

    log(f"\n  Saved final candidate views → {FINAL_OUTPUT}")

    # ── Print leaderboard ───────────────────────────────────────────────
    log(f"\n  {'='*70}")
    log(f"  Collections Leaderboard — Ordered by SUM(view_scores) DESC")
    log(f"  {'='*70}")
    log(f"  {'Rank':<6} {'Collection':<12} {'Views':<7} {'Queries':<9} {'Total Score':<14} {'Top View':<30}")
    log(f"  {'─'*6} {'─'*12} {'─'*7} {'─'*9} {'─'*14} {'─'*30}")
    for rank, col in enumerate(final_collections, 1):
        top_view = col["views"][0]["view_id"][:28] if col["views"] else "—"
        log(f"  {rank:<6} #{col['collection_id']:<9} {col['size']:<7} "
            f"{col['unique_queries_covered']:<9} {col['total_score']:<14.4f} {top_view:<30}")

    log(f"\n  {'═'*70}")
    log(f"  Pipeline complete: {t5 - t0:.1f}s total")
    log(f"  {'═'*70}\n")


if __name__ == "__main__":
    main()
