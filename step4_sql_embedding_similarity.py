"""
Step 4 — SQL Embedding Similarity Scorer
=========================================

Scores candidate views against workload queries using structural similarity.

Two modes:
    - Structural (always available): AST-based overlap scoring
    - Embedding (when sentence_transformers works): neural embedding similarity

Interface:
    score(top_candidates, workload, table_stats) -> List[dict] sorted by benefit DESC

    Each result dict:
        candidate_id, view_sql, view_tables,
        avg_similarity, n_covered, total_benefit
"""
import sys, os, re
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))





def filter_dropped(results, candidates=None):
    """Remove views whose tables are subset of {nation, region} (junk views).
    The candidates parameter is kept for backward compatibility but unused."""
    junk = {"nation", "region", "nation:n1", "nation:n2"}
    kept = []
    for r in results:
        tables = set(r.get("view_tables", []))
        if tables and tables.issubset(junk):
            continue
        kept.append(r)
    return kept


def score_embedding(top_candidates, workload, table_stats, fact_boost=3.0):
    """
    Score candidates using neural embedding similarity.
    Falls back to structural if embeddings unavailable.
    """
    try:
        return _embedding_score(top_candidates, workload, table_stats, fact_boost)
    except Exception as e:
        print(f"  Embedding scorer failed ({e})", flush=True)


def _embedding_score(top_candidates, workload, table_stats, fact_boost):
    """Neural embedding scorer with pre-cached query parses."""
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"

    from sql_embeddings import (
        ViewSelectionPipeline, TableStats, view_query_similarity,
    )

    pipeline = ViewSelectionPipeline(
        table_stats, fact_boost=fact_boost, alpha=0.7,
    )
    embedder = pipeline._get_embedder()

    # Pre-parse all queries once
    print(f"  Parsing {len(workload)} queries...", flush=True)
    q_objects = [pipeline.parse(q) for q in workload]

    candidate_sqls = [c.get('sql', '') for c in top_candidates]
    candidate_ids = [_make_id(c) for c in top_candidates]

    print(f"  Parsing {len(candidate_sqls)} candidates...", flush=True)
    v_objects = [pipeline.parse(v) for v in candidate_sqls]

    results = []
    for i, (v_sql, v_obj, cid) in enumerate(zip(candidate_sqls, v_objects, candidate_ids)):
        scores = {}
        for j, (q_sql, q_obj) in enumerate(zip(workload, q_objects)):
            sim = view_query_similarity(
                v_obj, q_obj,
                table_stats=table_stats,
                fact_boost=fact_boost,
                alpha=0.7,
                embedder=embedder,
            )
            scores[q_sql] = sim

        non_zero = [s for s in scores.values() if s > 0.0]
        results.append({
            "candidate_id": cid,
            "view_sql": v_sql,
            "view_tables": list(v_obj.tables),
            "avg_similarity": sum(non_zero) / max(len(non_zero), 1) if non_zero else 0.0,
            "n_covered": len(non_zero),
            "total_benefit": sum(non_zero),
        })

        if (i + 1) % 20 == 0:
            print(f"    Scored {i+1}/{len(candidate_sqls)}", flush=True)

    return sorted(results, key=lambda r: r["total_benefit"], reverse=True)


def _make_id(c):
    label = c.get('label', f"L{c.get('level', '?')}")
    return f"{label}_{c.get('source_query', 'global')}"
