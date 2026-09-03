# GreenVIEW — Workload-Driven Materialized View Selection (TPC-H / TPC-DS)

This repository contains the research implementation of **GreenVIEW**, an automatic
pipeline that discovers, merges, scores, and bundles **candidate materialized views**
for a given SQL workload. It targets the standard **TPC-H** and **TPC-DS** benchmarks
and ranks non-redundant *collections* of views by a cost/benefit score that balances
query execution-time / CPU savings against storage cost — i.e. it answers *"which views
should I materialize to make this workload faster (and greener), and in what combination?"*

The project folder is named `View_paper`; the codebase itself is referred to as
"GreenVIEW" throughout the sources.

---

## What the pipeline does

Given a workload (a list of SQL queries) plus measured per-query metrics
(`time_cpu_*.json`), the pipeline:

1. **Extracts** layered SQL sub-expression candidates (levels **L0–L7**) from every
   query — joins, filters, projections, aggregates — with strict fidelity handling for
   self-join aliases, CTEs, set operations and join predicates.
2. **Merges** structurally similar candidates across the whole workload
   (dedup, projection union, filter-value generalization such as `IN (...)` /
   date-range broadening) and drops patterns appearing in fewer than 2 queries.
3. **Scores** each (view, query) pair using neural **SQL embeddings** (offline
   `sentence-transformers` model) constrained by hard structural rules: table
   containment, per-table **column containment**, and predicate/date-range coverage.
   Views whose merged SQL would break semantics (aggregates, windows, CTEs,
   set ops) fall back to their exact source definitions.
4. **Estimates cost/benefit** per view from measured query execution time & CPU
   (`time_cpu_tpch.json` / `time_cpu_tpcds.json`) minus a storage-cost term that is
   weighted by the dominant table's share of the database (row count × columns).
5. **Builds collections** — sets of mutually compatible views. Views that share both
   covered queries *and* tables conflict and cannot co-exist; otherwise they are
   greedily grouped. Collections are ordered by the sum of their views' scores.

The final output is a leaderboard of view **collections** (each with ready-to-use
`view_sql` definitions), so you can pick the collection that best fits a storage budget.

> The file `pipeline.py` is labelled *"GreenVIEW Pipeline — Reconstructed"* and is the
> end-to-end orchestrator for both benchmarks.

---

## Repository layout

### Pipeline modules

| File | Step | Role |
|---|---|---|
| `pipeline.py` | runner | End-to-end orchestration of steps 1–5 (`python pipeline.py [tpch\|tpcds]`) |
| `candidate_views_extractor.py` | 1 | Layered L0–L7 candidate extraction from one SQL query (sqlglot + regex) |
| `step1_candidates_extractor.py` | 1 | Thin wrapper exposing `extract(query, table_stats, column_schema)` |
| `step1_cache_tpch.json` / `step1_cache_tpcds.json` | 1 | Cached raw candidates per query `Q0..Qn` |
| `global_candidate_merger.py` | 2 | Cross-workload structural merge + dedup logic |
| `step2_global_candidates_merger.py` | 2 | Wrapper for step 2 (drops junk nation/region-only views) |
| `sql_embeddings.py` | 3 | SQL parsing into `SQLObject`, component weights, neural view↔query similarity with hard containment constraints |
| `step4_sql_embedding_similarity.py` | 3 | Standalone structural/embedding similarity scorer variant |
| `step3_Cost-Benefit-Estimator.py` | 4 | Composite benefit scoring (execution time %, CPU %, storage cost %) — note the hyphen, loaded dynamically |
| `self_join_optimizer.py` | opt | Strips redundant self-join aliases from candidates and keeps the better variant |
| `step2b_view_collections.py` | 5 | Coverage computation + greedy non-redundant collection builder |

### Supporting modules

| File | Role |
|---|---|
| `schemas.py` | Single source of truth for TPC-H / TPC-DS table stats, column schemas, dimension/nation-region tables (`ACTIVE`, `TPCH`, `TPCDS`) |
| `canonical_ra/` | Canonical relational-algebra lattice: normalized predicates, interval representation & merging for date/comparable predicates (`lattice.py`, `models.py`) |
| `storage_measurer.py` | Optional PostgreSQL-backed actual storage measurement (`pg_total_relation_size`) replacing the heuristic cost |
| `tpch_workload.py` | Original TPC-H workload (~557 queries) |
| `tpcds_workload.py` | Original TPC-DS workload (~550 queries) |
| `tpch_rewritten.py` | TPC-H workload rewritten against a merged materialized view (`L0FullView_MERGED_Q7`) with residual predicates — used to validate rewrite benefit |
| `tpcds_rewritten.py` | Selected TPC-DS queries rewritten as `SELECT * FROM "L0-FULLVIEW_Qn"` |
| `time_cpu_tpch.json` / `time_cpu_tpcds.json` | Measured per-query `execution_time`, `CPU_percentage_mean`, `CPU_percentage_max` (data source for cost/benefit) |
| `final_candidate_views_tpch.json` / `final_candidate_views_tpcds.json` | **Final output**: scored, deduplicated view collections ordered by total score |

### Generated / cache artifacts (safe to delete)

`__pycache__/`, `interim_merged_*.json`, `interim_embeddings_*.json`,
`interim_collections_*.json`, `.venv/` (virtual environment, see below).

---

## Output format

`final_candidate_views_<bench>.json` contains:

```jsonc
{
  "pipeline_info": {
    "workload_size": 557,
    "database": "TPCH",
    "pipeline_order": [ "1: candidate_views_extractor", "...", "5: view_collections" ],
    "step1_raw_candidates": 1106,
    "step2_merged_candidates": 12,
    "step5_collections": 15,
    "timing_s": { "...": 15.2 }
  },
  "collections": [
    {
      "collection_id": 0,
      "size": 7,
      "total_score": 0.5648,
      "unique_queries_covered": 556,
      "views": [
        {
          "view_id": "L1_MERGED_Q7",
          "view_sql": "SELECT ...",
          "view_tables": ["lineitem", "orders", ...],
          "view_joins": [...],
          "view_filters": {...},
          "view_aggregates": [...],
          "view_complexity": 5,
          "covered_query_ids": ["Q0", "Q1", ...],
          "avg_similarity_score": 0.91,
          "cost_benefit_score": 0.23,
          "execution_time_pct": 0.15,
          "storage_cost_pct": 0.004,
          "avg_cpu": 0.02,
          "max_cpu": 0.04
        }
      ]
    }
  ]
}
```

The console leaderboard prints the same collections sorted by `SUM(cost_benefit_score) DESC`.

---

## Requirements

- **Python 3.12** (project uses a local `.venv`)
- `sqlglot` — SQL parsing / AST
- `torch` + `sentence-transformers` (+ `transformers`) — neural SQL embeddings
- `numpy`, `scikit-learn`, `tqdm`
- `psycopg2-binary` — *only* if you use `storage_measurer.py` against PostgreSQL

The pipeline forces Hugging Face **offline mode**
(`HF_HUB_OFFLINE=1`, `TRANSFORMERS_OFFLINE=1`), so the embedding model must already be
present in the local HF cache or it falls back gracefully.

---

## Usage

Run the full pipeline for a benchmark (defaults to `tpch`):

```bash
# from inside the project folder, using the bundled environment
.venv\Scripts\python pipeline.py tpch
.venv\Scripts\python pipeline.py tpcds
```

Pipeline flow (all steps cached in `step1_cache_*.json`, then saved as
`interim_*.json` after each phase):

```
Extract (L0–L7)  →  Merge / Dedup / Frequency-filter  →  Embedding similarity + coverage
  →  Cost/Benefit  →  Non-redundant Collections  →  final_candidate_views_<bench>.json
```

To switch schemas programmatically, set `schemas.ACTIVE = TPCH` or `TPCDS` before
calling the step modules.

---

## Notes / caveats

- **Research code**: several modules are exploratory snapshots ("reconstructed"
  pipeline, parallel implementations of the same step). `pipeline.py` is the
  canonical path; the standalone `step2_*` / `step3_*` / `step4_*` files are
  re-usable building blocks with slightly different interfaces.
- `step3_Cost-Benefit-Estimator.py` intentionally contains a hyphen in its filename,
  so `pipeline.py` loads it via a dynamic import (see source).
- The benefit formula in the sources has evolved (the header of
  `step3_Cost-Benefit-Estimator.py` documents `((exec% + cpu_mean% + cpu_max%)/3) ×
  similarity − storage%/10`; `pipeline.py` currently implements a slightly different
  weighted combination) — treat the numbers as internally consistent, not normative.
- Junk candidates built only from `nation`/`region` are filtered out in step 2.
- Materialized-view definitions that cannot safely be generalized (aggregates,
  windows, CTEs, set ops) are kept as exact per-query views (`_preserve_semantic_view_definitions`).
