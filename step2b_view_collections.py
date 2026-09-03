"""
step2b_view_collections.py
===========================

Build view collections where each view can be part of many collections.

COLLECTION RULE (overlap constraint):
  For each pair (view_i, view_j):
    IF common_covered_queries(view_i, view_j) > 0
       AND common_tables(view_i, view_j) > 0
    THEN view_i and view_j CANNOT be in the same collection.

  In other words: views that share both queries AND tables conflict.
  Views that share queries but have disjoint tables ARE compatible.
  Views with disjoint queries are always compatible.

Strategy:
  Each view seeds collections as an anchor, and other views are greedily
  added if they satisfy the pairwise overlap constraint with EVERY view
  already in the collection.
"""

import logging
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple, Optional, Any
import statistics

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# Data structures
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Collection:
    """One collection of complementary views."""
    collection_id: int
    view_ids: List[str]          = field(default_factory=list)
    all_covered: Set[str]        = field(default_factory=set)
    all_tables: Set[str]         = field(default_factory=set)
    size: int                    = 0
    avg_similarity_score: float  = 0.0

    def __post_init__(self):
        self.size = len(self.view_ids)


# ─────────────────────────────────────────────────────────────────────────────
# Helper: extract coverage and tables from a view
# ─────────────────────────────────────────────────────────────────────────────

def _get_covered_queries(view_meta: dict) -> Set[str]:
    """
    Extract the set of query IDs this view covers.
    Returns empty set when no coverage info is present.
    """
    covered = view_meta.get("view_covered_query_ids", 
               view_meta.get("covered_queries", 
               view_meta.get("source_queries", [])))
    if isinstance(covered, (list, tuple, set)):
        return set(str(q) for q in covered if q)
    return set()


def _get_tables(view_meta: dict) -> Set[str]:
    """
    Extract the set of table names a view references.
    Handles both original (tables list) and collection format (view_tables list).
    """
    tables = view_meta.get("view_tables", view_meta.get("tables", []))
    if isinstance(tables, (list, tuple, set)):
        # Normalize: strip schema prefixes and alias suffixes
        result = set()
        for t in tables:
            t = str(t).lower()
            # Handle "schema.table" format
            if '.' in t:
                t = t.split('.')[-1]
            # Handle "table:alias" format (self-joins)
            if ':' in t:
                t = t.split(':')[0]
            result.add(t)
        return result
    return set()


def _coverage_fingerprint(view_meta: dict) -> frozenset:
    """
    Extract the set of query IDs this view covers as an immutable fingerprint.
    """
    return frozenset(_get_covered_queries(view_meta))


def _tables_fingerprint(view_meta: dict) -> frozenset:
    """
    Extract the set of table names as an immutable fingerprint.
    """
    return frozenset(_get_tables(view_meta))


# ═════════════════════════════════════════════════════════════════════════════
# Overlap constraint check (THE CORE RULE)
# ═════════════════════════════════════════════════════════════════════════════

def views_can_coexist(view_a_meta: dict, view_b_meta: dict) -> bool:
    """
    Check if two views can coexist in the same collection.

    RULE:
      IF common_queries > 0 AND common_tables > 0 → CANNOT coexist (CONFLICT)
      Otherwise → CAN coexist

    Args:
        view_a_meta: metadata dict for first view (must have covered_queries and tables)
        view_b_meta: metadata dict for second view

    Returns:
        True if views can be in the same collection, False if they conflict.
    """
    q_a = _get_covered_queries(view_a_meta)
    q_b = _get_covered_queries(view_b_meta)
    t_a = _get_tables(view_a_meta)
    t_b = _get_tables(view_b_meta)

    common_queries = q_a & q_b
    common_tables = t_a & t_b

    # CORE RULE: Conflict only when BOTH queries AND tables overlap
    if common_queries and common_tables:
        return False  # CONFLICT: cannot be in same collection
    return True  # Compatible


def view_can_join_collection(
    view_meta: dict,
    collection_views_meta: List[dict],
    collection_coverage: Optional[Set[str]] = None,
    collection_tables: Optional[Set[str]] = None,
) -> bool:
    """
    Check if a view can join a collection based on the overlap constraint.

    The view must be compatible with EVERY view already in the collection.

    Args:
        view_meta: metadata dict for the candidate view
        collection_views_meta: list of metadata dicts for views in the collection
        collection_coverage: union of covered queries (unused, kept for compat)
        collection_tables: union of tables (unused, kept for compat)

    Returns:
        True if the view can join, False if it conflicts with any existing view.
    """
    for existing_meta in collection_views_meta:
        if not views_can_coexist(view_meta, existing_meta):
            return False
    return True


# ─────────────────────────────────────────────────────────────────────────────
# Representative selection
# ─────────────────────────────────────────────────────────────────────────────

def is_subset_related(view_a: dict, view_b: dict) -> bool:
    """
    Return True when one view's coverage is a strict subset of the other's.
    This is used for deduplication (not for overlap constraint).
    """
    cov_a = _coverage_fingerprint(view_a)
    cov_b = _coverage_fingerprint(view_b)
    if not cov_a or not cov_b:
        return False
    return cov_a < cov_b or cov_b < cov_a


def _pick_representative(
    vids: List[str],
    meta_lookup: Dict[str, dict],
) -> str:
    """
    From a group of views with identical coverage, select the one with the
    highest complexity (most joins + filters + aggregates).
    """
    def _complexity(vid: str) -> int:
        return meta_lookup.get(vid, {}).get("view_complexity", 0)
    return max(vids, key=lambda v: (_complexity(v), v))


def _mean_similarity(vids: List[str], meta_lookup: Dict[str, dict]) -> float:
    """
    Compute the mean view_avg_similarity_score for a list of view IDs.
    """
    scores = [
        meta_lookup.get(vid, {}).get("view_avg_similarity_score", 0.0)
        for vid in vids
    ]
    if not scores:
        return 0.0
    return round(statistics.mean(scores), 6)


# ─────────────────────────────────────────────────────────────────────────────
# Collection builder
# ─────────────────────────────────────────────────────────────────────────────

def view_collections_builder(
    view_collections: Dict[str, dict],
    max_collection_size: int = 8,
    min_new_coverage_pct: float = 5.0,
    max_collections: int = 50,
) -> List[Collection]:
    """
    Build view collections enforcing the pairwise overlap constraint:

      For each (view_i, view_j):
        IF common_queries > 0 AND common_tables > 0 → CONFLICT
        Otherwise → compatible

    Strategy:
      1. Group views by identical coverage, keep only representative
      2. For each anchor view, seed a collection
      3. Greedily add compatible views that bring new query coverage
      4. Sort by mean similarity descending

    Args:
        view_collections: {view_id: view_meta} dict.
        max_collection_size: Maximum views per collection.
        min_new_coverage_pct: Minimum %% new queries a view must add.
        max_collections: Maximum collections to return.

    Returns:
        List of Collection objects sorted by mean similarity descending.
    """
    if not view_collections:
        return []

    # ── Step 1: Deduplicate identical coverage → keep best representative ──
    coverage_map: Dict[str, frozenset] = {}
    tables_map: Dict[str, frozenset] = {}
    for vid, meta in view_collections.items():
        coverage_map[vid] = _coverage_fingerprint(meta)
        tables_map[vid] = _tables_fingerprint(meta)

    groups: Dict[frozenset, List[str]] = defaultdict(list)
    for vid, cov in coverage_map.items():
        groups[cov].append(vid)

    # Keep only views with non-empty coverage
    non_empty = [(cov, vids) for cov, vids in groups.items() if cov]
    if not non_empty:
        return []

    representatives: Dict[frozenset, str] = {}
    for cov, vids in non_empty:
        representatives[cov] = _pick_representative(vids, view_collections)
    rep_list = list(representatives.values())
    rep_set = set(rep_list)

    # ── Step 2: Precompute compatibility matrix ──────────────────────
    # For efficient conflict checking
    # compatible[i][j] = True if rep_list[i] and rep_list[j] can coexist
    n = len(rep_list)
    compatible: List[List[bool]] = [[True] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            vi_meta = view_collections[rep_list[i]]
            vj_meta = view_collections[rep_list[j]]
            can = views_can_coexist(vi_meta, vj_meta)
            compatible[i][j] = can
            compatible[j][i] = can

    # ── Step 3: Per-view anchor expansion ────────────────────────────
    collections: List[Collection] = []
    collection_id = 0

    for anchor_idx, anchor_vid in enumerate(rep_list):
        anchor_meta = view_collections[anchor_vid]
        anchor_covered = coverage_map[anchor_vid]

        # Rank candidates: order by how many NEW queries they bring
        candidates: List[Tuple[str, int, int]] = []  # (vid, new_queries_count, candidate_idx)
        for cand_idx, cand_vid in enumerate(rep_list):
            if cand_vid == anchor_vid:
                continue
            if not compatible[anchor_idx][cand_idx]:
                # Even for the second view, the constraint must hold
                continue
            cand_covered = coverage_map[cand_vid]
            new_q = cand_covered - anchor_covered
            inc_pct = len(new_q) / max(len(cand_covered), 1) * 100
            if inc_pct >= min_new_coverage_pct:
                candidates.append((cand_vid, len(new_q), cand_idx))

        candidates.sort(key=lambda x: -x[1])

        # Try multiple starting points (different 2nd-view seeds)
        for start in range(min(len(candidates), 5)):
            current_vids: List[str] = [anchor_vid]
            current_meta_list: List[dict] = [anchor_meta]
            current_coverage: Set[str] = set(anchor_covered)
            current_tables: Set[str] = set(tables_map[anchor_vid])

            for cand_vid, _new_q, cand_idx in candidates[start:]:
                if len(current_vids) >= max_collection_size:
                    break

                cand_meta = view_collections[cand_vid]
                cand_covered = coverage_map[cand_vid]
                cand_tables_set = tables_map[cand_vid]

                # ── ENFORCE CONSTRAINT: compatible with ALL existing views ──
                can_add = True
                for existing_meta in current_meta_list:
                    if not views_can_coexist(cand_meta, existing_meta):
                        can_add = False
                        break

                if not can_add:
                    continue

                # Also check min_new_coverage_pct
                new_q = cand_covered - current_coverage
                inc_pct = len(new_q) / max(len(cand_covered), 1) * 100
                if inc_pct < min_new_coverage_pct:
                    continue

                current_vids.append(cand_vid)
                current_meta_list.append(cand_meta)
                current_coverage |= cand_covered
                current_tables |= cand_tables_set

            if len(current_vids) >= 2:
                avg_sim = _mean_similarity(current_vids, view_collections)
                collections.append(Collection(
                    collection_id=collection_id,
                    view_ids=list(current_vids),
                    all_covered=set(current_coverage),
                    all_tables=set(current_tables),
                    avg_similarity_score=avg_sim,
                ))
                collection_id += 1

    # ── Step 4: Keep one collection per exact membership ────────────────
    # Different anchor/start paths can produce the same set of views.
    unique_collections: List[Collection] = []
    seen_memberships: Set[frozenset] = set()
    for collection in collections:
        membership = frozenset(collection.view_ids)
        if membership in seen_memberships:
            continue
        seen_memberships.add(membership)
        unique_collections.append(collection)
    collections = unique_collections

    # ── Step 5: Sort by mean(avg_similarity_score) descending ───────────
    collections.sort(key=lambda c: -c.avg_similarity_score)
    for i, col in enumerate(collections):
        col.collection_id = i

    # Trim to max_collections
    if len(collections) > max_collections:
        collections = collections[:max_collections]

    return collections


# ─────────────────────────────────────────────────────────────────────────────
# Main entry point (pipeline interface)
# ─────────────────────────────────────────────────────────────────────────────

def build_collections(
    candidates_input: Dict[str, Any],
    max_collections: int = 50,
    max_collection_size: int = 8,
    min_new_coverage_pct: float = 5.0,
) -> List[Collection]:
    """
    Build view collections with the overlap constraint.

    COLLECTION RULE:
      For each (view_i, view_j):
        IF common_queries > 0 AND common_tables > 0 → views CANNOT coexist
        Otherwise → views CAN coexist

    Args:
        candidates_input: dict with key "candidate_views" mapping to
            {view_id: view_meta} where each view_meta has:
            - view_covered_query_ids (or covered_queries): list of query IDs
            - view_tables (or tables): list of table names

    Returns:
        List of Collection objects.
    """
    views = candidates_input.get("candidate_views", {}) if isinstance(
        candidates_input, dict
    ) else candidates_input

    if not views:
        logger.warning("build_collections: no candidate views provided")
        return []

    collections = view_collections_builder(
        views,
        max_collection_size=max_collection_size,
        min_new_coverage_pct=min_new_coverage_pct,
        max_collections=max_collections,
    )

    return collections


# ─────────────────────────────────────────────────────────────────────────────
# Quick self-test
# ─────────────────────────────────────────────────────────────────────────────

def _demo():
    """
    Run a small self-test to verify the builder works with the overlap constraint.

    Test data:
      V1: covers Q1,Q2, tables: {customer, store_sales}
      V2: covers Q3,Q4, tables: {date_dim, item}        → compatible with V1 (disjoint queries)
      V3: covers Q1,Q2, tables: {customer, store_sales}  → same as V1, dedup
      V4: covers Q5, tables: {inventory}                 → compatible with all
      V5: covers Q1,Q3, tables: {customer, item}         → shares Q1 with V1, shares customer → CONFLICT with V1
    """
    test_views = {
        "V1": {
            "view_covered_query_ids": ["Q1", "Q2"],
            "view_tables": ["customer", "store_sales"],
            "view_complexity": 3,
        },
        "V2": {
            "view_covered_query_ids": ["Q3", "Q4"],
            "view_tables": ["date_dim", "item"],
            "view_complexity": 5,
        },
        "V3": {
            "view_covered_query_ids": ["Q1", "Q2"],
            "view_tables": ["customer", "store_sales"],
            "view_complexity": 2,
        },
        "V4": {
            "view_covered_query_ids": ["Q5"],
            "view_tables": ["inventory"],
            "view_complexity": 1,
        },
        "V5": {
            "view_covered_query_ids": ["Q1", "Q3"],
            "view_tables": ["customer", "item"],
            "view_complexity": 4,
        },
    }

    print("Overlap constraint tests:")
    print(f"  V1 vs V2: {views_can_coexist(test_views['V1'], test_views['V2'])} (expect True - disjoint queries)")
    print(f"  V1 vs V5: {views_can_coexist(test_views['V1'], test_views['V5'])} (expect False - share Q1 AND customer)")
    print(f"  V1 vs V4: {views_can_coexist(test_views['V1'], test_views['V4'])} (expect True - disjoint queries)")
    print(f"  V1 vs V3: {views_can_coexist(test_views['V1'], test_views['V3'])} (expect True - identical, dedup separately)")
    print()

    cols = build_collections({"candidate_views": test_views})
    print(f"Built {len(cols)} collections:\n")
    for col in cols:
        print(f"  Collection #{col.collection_id}  (size={col.size}, queries={len(col.all_covered)}, tables={len(col.all_tables)})")
        for vid in col.view_ids:
            cov = test_views[vid]["view_covered_query_ids"]
            tbls = test_views[vid]["view_tables"]
            print(f"    {vid}  → queries={cov}, tables={tbls}")
    print()

    # Verify: V1 and V5 should NEVER be in the same collection
    for col in cols:
        if "V1" in col.view_ids and "V5" in col.view_ids:
            print("ERROR: V1 and V5 are in the same collection! Overlap constraint violated!")
        if "V1" in col.view_ids and "V2" in col.view_ids:
            print("OK: V1 and V2 can coexist (disjoint queries)")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _demo()
