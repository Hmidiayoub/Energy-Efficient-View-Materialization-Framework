"""
GreenVIEW — Actual Storage Cost Measurement via PostgreSQL
===========================================================

Replaces the heuristic storage cost estimate with actual
pg_total_relation_size() measurements.

Usage:
    from storage_measurer import measure_storage_cost

    storage_bytes = measure_storage_cost(view_sql, conn_params)

Dependencies:
    pip install psycopg2-binary
"""

import re
import psycopg2
from psycopg2 import sql as pysql
from typing import Dict, Optional, Set

# ─────────────────────────────────────────────────────────────────────────────
# Connection configuration
# ─────────────────────────────────────────────────────────────────────────────

DEFAULT_CONN = {
    "host": "localhost",
    "port": 5432,
    "dbname": "tpch",
    "user": "postgres",
    "password": "postgres",
}

_db_sizes_cache: Dict[str, int] = {}


def _get_db_size(dbname: str, conn_params: dict) -> int:
    if dbname in _db_sizes_cache:
        return _db_sizes_cache[dbname]
    conn = psycopg2.connect(**{**DEFAULT_CONN, **conn_params})
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT pg_database_size(%s)", (dbname,))
            size = cur.fetchone()[0]
            _db_sizes_cache[dbname] = size
            return size
    finally:
        conn.close()


def _sanitize_mv_name(view_sql: str, max_len: int = 50) -> str:
    sql_hash = abs(hash(view_sql)) & 0xFFFF_FFFF
    match = re.search(r'\bFROM\s+(\w+)', view_sql, re.IGNORECASE)
    first_table = match.group(1).lower()[:15] if match else "mv"
    name = f"mv_{first_table}_{sql_hash}"
    if len(name) > max_len:
        name = name[:max_len]
    return name


def measure_storage_cost(
    view_sql: str,
    conn_params: Optional[Dict] = None,
    conn=None,
    timeout_seconds: int = 30,
) -> int:
    """
    Create MV, measure pg_total_relation_size, drop it.
    Returns size in bytes (0 on failure).
    """
    params = {**DEFAULT_CONN, **(conn_params or {})}
    mv_name = _sanitize_mv_name(view_sql)

    should_close = False
    if conn is None:
        should_close = True
        conn = psycopg2.connect(**params)

    try:
        with conn.cursor() as cur:
            cur.execute(f"SET statement_timeout = '{timeout_seconds}s'")

            # Drop if exists
            cur.execute(
                pysql.SQL("DROP MATERIALIZED VIEW IF EXISTS {} CASCADE")
                .format(pysql.Identifier(mv_name))
            )

            # Create
            create_sql = pysql.SQL(
                "CREATE MATERIALIZED VIEW {} AS {}"
            ).format(pysql.Identifier(mv_name), pysql.SQL(view_sql))
            cur.execute(create_sql)

            # Measure
            cur.execute(
                pysql.SQL("SELECT pg_total_relation_size({})")
                .format(pysql.Literal(mv_name))
            )
            size = cur.fetchone()[0]

            # Drop
            cur.execute(
                pysql.SQL("DROP MATERIALIZED VIEW IF EXISTS {} CASCADE")
                .format(pysql.Identifier(mv_name))
            )
            conn.commit()
            return int(size)

    except Exception:
        try:
            conn.rollback()
            with conn.cursor() as cur:
                cur.execute(
                    pysql.SQL("DROP MATERIALIZED VIEW IF EXISTS {} CASCADE")
                    .format(pysql.Identifier(mv_name))
                )
                conn.commit()
        except Exception:
            conn.rollback()
        return 0
    finally:
        if should_close:
            conn.close()


def measure_batch(
    view_sqls: Dict[str, str],
    conn_params: Optional[Dict] = None,
    timeout_seconds: int = 30,
    progress_callback=None,
) -> Dict[str, int]:
    params = {**DEFAULT_CONN, **(conn_params or {})}
    conn = psycopg2.connect(**params)
    results: Dict[str, int] = {}
    total = len(view_sqls)

    try:
        for i, (vid, sql) in enumerate(view_sqls.items()):
            size = measure_storage_cost(
                sql, conn_params=params, conn=conn,
                timeout_seconds=timeout_seconds,
            )
            results[vid] = size
            if progress_callback:
                progress_callback(vid, size, i, total)
    finally:
        conn.close()

    return results


def replace_storage_cost_in_pipeline(
    merged_candidates: list,
    result_data: list,
    schema,
    conn_params: Optional[Dict] = None,
):
    """
    Full replacement for the heuristic storage cost step in pipeline.py.

    Instead of:
        storage_cost_pct = n_cols * n_tables / 200 * dominant_db_share

    This does:
        storage_bytes = measure_storage_cost(view_sql)
        storage_cost_pct = storage_bytes / total_db_size

    Returns benefit_lookup dict (same interface as pipeline.py).
    """
    params = {**DEFAULT_CONN, **(conn_params or {})}
    dbname = params.get("dbname", "tpch")
    total_db_size = _get_db_size(dbname, params)

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

    view_sqls = {}
    for c in merged_candidates:
        cid = _make_view_id_fast(c)
        sql = c.get("view_sql", c.get("sql", ""))
        if sql.strip():
            view_sqls[cid] = sql

    print(f"  Measuring {len(view_sqls)} views via PostgreSQL...")
    storage_sizes = measure_batch(
        view_sqls, conn_params=params, timeout_seconds=30,
    )
    zero_count = sum(1 for s in storage_sizes.values() if s == 0)
    print(f"  Measured: {len(storage_sizes)} "
          f"({zero_count} failed/zero)")

    benefit_lookup = {}
    for c in merged_candidates:
        cid = _make_view_id_fast(c)
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
        exec_time_pct = (covered_exec_time / total_exec_time
                         if total_exec_time > 0 else 0.0)
        avg_cpu = (covered_cpu_mean / n_covered / 100.0
                   if n_covered > 0 else 0.0)
        max_cpu_val = sum(covered_cpu_max_vals) if covered_cpu_max_vals else 0.0
        max_cpu = (max_cpu_val / n_covered / 100.0
                   if n_covered > 0 else 0.0)

        # Actual storage measurement
        storage_bytes = storage_sizes.get(cid, 0)
        storage_cost_pct = (
            storage_bytes / total_db_size
            if total_db_size > 0 else 0.0
        )

        benefit = (exec_time_pct * similarity + avg_cpu + max_cpu
                   - storage_cost_pct)
        benefit_lookup[cid] = {
            "benefit": round(benefit, 6),
            "execution_time_pct": round(exec_time_pct, 6),
            "avg_cpu": round(avg_cpu, 6),
            "max_cpu": round(max_cpu, 6),
            "storage_cost_pct": round(storage_cost_pct, 6),
            "storage_bytes": storage_bytes,
            "similarity_score": round(similarity, 6),
            "covered_queries": len(covered_ids),
            "covered_exec_time": round(covered_exec_time, 4),
        }

    return benefit_lookup


def _make_view_id_fast(candidate: dict) -> str:
    label = candidate.get("label", f"L{candidate.get('level', '?')}")
    return f"{label}_{candidate.get('source_query', 'global')}"


if __name__ == "__main__":
    test_sql = "SELECT * FROM nation WHERE n_regionkey = 1"
    print(f"Measuring: {test_sql}")
    size = measure_storage_cost(test_sql)
    print(f"  Size: {size:,} bytes ({size/1024:.1f} KB)")
    if size > 0:
        print("  OK!")
    else:
        print("  FAILED — check PostgreSQL connection")
