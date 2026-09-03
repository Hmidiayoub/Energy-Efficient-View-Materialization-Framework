"""fix_step1_serializer.py — Augments step1_candidates_extractor to pass join_predicates through."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, r'C:\Users\BELLATOR\Desktop\View_paper')

from candidate_views_extractor import (
    extract_all_candidates as _extract,
    TableStats as _TableStats,
    CandidateView as _CandidateView,
)

TableStats = _TableStats

def extract(query_sql, table_stats, column_schema=None):
    """Extract L0–L7 candidates from one query. Returns List[dict] with join_predicates."""
    cands = _extract(query_sql, table_stats, column_schema)
    return [_candidate_to_dict(c) for c in cands]

def _candidate_to_dict(c):
    return {
        "sql": c.sql,
        "level": c.level,
        "label": c.label,
        "source_sql": c.source_sql,
        "tables": list(c.tables),
        "join_pairs": list(c.join_pairs),
        "join_predicates": list(c.join_predicates) if hasattr(c, 'join_predicates') and c.join_predicates else [],
        "filters": {k: list(v) for k, v in c.filters.items()},
        "aggregates": list(c.aggregates),
        "groupby_cols": list(c.groupby_cols),
    }

import schemas as _schemas_mod

def __getattr__(name):
    if name == "column_schema":
        return _schemas_mod.ACTIVE.column_schema
    if name == "table_stats":
        return _schemas_mod.ACTIVE.table_stats
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
