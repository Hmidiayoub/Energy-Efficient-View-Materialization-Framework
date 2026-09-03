"""
Step 2 — Global View Candidate Merge & Dedup
==============================================

Merges structurally similar candidates across the entire workload.

Interface:
    merge(candidates: List[dict]) -> (merged_list: List[dict], stats: dict)
    
Merge rules:
    1. Perfectly equal → deduplicate
    2. Differ only in SELECT → union projections
    3. Differ only in filter value (non-date, =/LIKE) → IN(val1, val2, ...)
    4. Differ only in filter value (date, <) → col < MIN(date1, date2)
    5. Differ only in filter value (date, >) → col > MAX(date1, date2)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import schemas as _sch
from global_candidate_merger import merge_candidates as _merge
from step1_candidates_extractor import extract as step1_extract


def _prepare_candidates(candidates):
    """Convert raw query inputs into Step 1 candidate dicts when needed."""
    prepared = []
    for c in candidates:
        if isinstance(c, dict) and "query" in c:
            prepared.extend(step1_extract(
                c["query"], _sch.ACTIVE.table_stats, _sch.ACTIVE.column_schema))
        else:
            prepared.append(c)
    return prepared


def _is_nation_or_region_only_view(candidate):
    """Return True if the candidate uses only nation and/or region tables."""
    tables = {t.lower() for t in candidate.get("tables", [])}
    return bool(tables) and tables.issubset(_sch.ACTIVE.nation_region_tables)


def merge(candidates):
    """Merge list of candidate dicts. Returns (merged_list, stats_dict)."""
    prepared = _prepare_candidates(candidates)
    prepared = [c for c in prepared if not _is_nation_or_region_only_view(c)]
    result = _merge(prepared)
    return result.merged_candidates, {
        "input_count": result.stats["input_count"],
        "perfect_duplicates_removed": result.stats["perfect_duplicates_removed"],
        "select_merges": result.stats["select_merges"],
        "filter_merges": result.stats["filter_merges"],
        "output_count": result.stats["output_count"],
    }
