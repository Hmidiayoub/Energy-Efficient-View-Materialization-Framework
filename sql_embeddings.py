"""
View Selection Pipeline — Coverage-Weight Similarity
=====================================================

Similarity between a candidate view and a query is defined as:

    score = similarity(query_w.embeddings, view.embeddings)

    where query_w is the fact-table-boosted, log-row-count weight
    computed over the QUERY's full table set (asymmetric, normalized) and stored in embeddings with semantic preservation.

Hard constraints applied before any weight computation:
    |view.tables| > |query.tables|  →  0.0 score (view over-joined, can't be used for the query)
    view.tables  ⊄  query.tables   →  0.0 score (view references foreign tables not in the query, can't be used)
    columns(view, view_tables) ⊄ columns(query, view_tables) →  0.0 score (view missing required columns from the query, can't be used)
    similarity(view,query) = 1 if view is perfectly equal to the query (same structure, same joins, same columns, same aggregates, same filters, etc.)

Column containment interpretation:
    For each table t in view.tables, the set of columns the QUERY uses from t must
    be a subset of the set of columns the VIEW provides from t. If any shared table
    has columns the query needs that the view lacks, the view cannot answer the query.

Alpha blend fix:
    The full SQL embedding was masking containment violations because even when
    per-table weights fail containment, the full SQL captures enough structure to
    produce a non-zero cosine similarity.  FIX: apply ALL hard constraints BEFORE
    any embedding computation.  If constraints fail, return 0.0 immediately.
    The alpha blend (weighted + full SQL) only runs on valid view-query pairs.
"""
import sqlglot
from sqlglot import exp
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Set, List, Tuple, Optional
import numpy as np
import re
from tpch_workload import workload_1 as queries


# ─────────────────────────────────────────────────────────────────────────────
# Data structures
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class TableStats:
    row_count: int
    is_fact: bool           # explicit label if available
    join_count: int = 0     # how many times it appears in joins


@dataclass
class SQLObject:
    """
    Parsed structural representation of a SQL view or query.
    """
    sql:               str
    tables:            Set[str]                    # all tables referenced
    fact_tables:       Set[str]                    # subset: fact tables
    dim_tables:        Set[str]                    # subset: dimension tables
    join_pairs:        Set[Tuple[str, str]]        # sorted (t1, t2) join pairs
    columns_per_table: Dict[str, Set[str]]         # {table: {col1, col2, ...}}
    aggregates:        Set[str]                    # aggregate function signatures
    groupby_cols:      Set[str]                    # GROUP BY columns
    filter_predicates: Set[str]                    # WHERE clause conditions (normalized)


# ─────────────────────────────────────────────────────────────────────────────
# SQL Parser → column-aware SQLObject
# ─────────────────────────────────────────────────────────────────────────────

def _resolve_aliases(tree) -> Dict[str, str]:
    """Build alias → real table name map from AST."""
    alias_map: Dict[str, str] = {}
    for tbl in tree.find_all(exp.Table):
        if tbl.alias:
            alias_map[tbl.alias.lower()] = tbl.name.lower()
    return alias_map


def _resolve(name: str, alias_map: Dict[str, str]) -> str:
    return alias_map.get(name.lower(), name.lower())


def _extract_columns_per_table(tree, alias_map: Dict[str, str],
                                 column_schema: Optional[Dict[str, Set[str]]] = None
                                 ) -> Dict[str, Set[str]]:
    """
    Walk all Column nodes in the AST and group by table.
    Returns {table_name: {column_name, ...}}.

    Qualified columns → attributed to their table (via alias_map).
    Unqualified columns (e.g. TPC-H's bare 'n_name'):
      - If `column_schema` is provided, each unqualified column is matched
        against the schema (table → set of columns) to find its owner.
      - If `column_schema` is None or resolution fails, the column goes to
        '__unqualified__'.
    SELECT-aliased references (ORDER BY revenue where revenue = SUM(...))
    are excluded — we only care about base column references.
    """
    columns: Dict[str, Set[str]] = defaultdict(set)

    # Collect SELECT aliases so we can exclude ORDER-BY-alias references
    select_aliases: Set[str] = set()
    for sel in tree.find_all(exp.Select):
        for expr in sel.expressions:
            if expr.alias:
                select_aliases.add(expr.alias.lower())

    # Build reverse schema: column_name → set of tables that have it
    reverse_schema: Optional[Dict[str, Set[str]]] = None
    if column_schema:
        reverse_schema = defaultdict(set)
        for tbl, cols in column_schema.items():
            for col in cols:
                reverse_schema[col.lower()].add(tbl.lower())

    for col in tree.find_all(exp.Column):
        col_name = col.name.lower()
        # Skip ORDER-BY alias references (e.g. ORDER BY revenue)
        if col_name in select_aliases:
            continue
        if col.table:
            resolved = alias_map.get(col.table.lower(), col.table.lower())
            columns[resolved].add(col_name)
        elif reverse_schema and col_name in reverse_schema:
            # Resolve unqualified column using schema
            candidates = reverse_schema[col_name]
            if len(candidates) == 1:
                # Unambiguous → attribute to the only matching table
                columns[next(iter(candidates))].add(col_name)
            else:
                # Ambiguous (same column name in multiple tables)
                # Attach to all candidate tables
                for t in candidates:
                    columns[t].add(col_name)
        else:
            # No table qualifier and no schema resolution → unqualified bucket
            columns['__unqualified__'].add(col_name)

    return dict(columns)


def _extract_aggregates(tree) -> Set[str]:
    """Extract aggregate function signatures: e.g. {'SUM(l_extendedprice)', 'COUNT(*)'}."""
    aggs: Set[str] = set()
    for func in tree.find_all(exp.AggFunc):
        # Normalize the signature: function name + lowercased args
        args = ", ".join(a.name.lower() if hasattr(a, 'name') else a.sql() for a in func.expressions)
        aggs.add(f"{func.sql_name()}({args})")
    return aggs


def _extract_groupby(tree) -> Set[str]:
    """Extract GROUP BY columns as normalized strings."""
    gb_cols: Set[str] = set()
    for gb in tree.find_all(exp.Group):
        for expr in gb.expressions:
            if isinstance(expr, exp.Column):
                if expr.table:
                    gb_cols.add(f"{expr.table.lower()}.{expr.name.lower()}")
                else:
                    gb_cols.add(expr.name.lower())
            else:
                gb_cols.add(expr.sql().lower())
    return gb_cols


def _extract_join_pairs(tree, alias_map: Dict[str, str]) -> Set[Tuple[str, str]]:
    """
    Extract join pairs from the FROM and JOIN clauses.
    Handles implicit joins (FROM t1, t2) by pairing adjacent table references.
    """
    pairs: Set[Tuple[str, str]] = set()

    # Collect all table references in FROM/JOIN order
    from_tables = list(tree.find_all(exp.Table))

    # Explicit JOINs: traverse the join tree structurally
    for join in tree.find_all(exp.Join):
        left = _resolve(join.this.name, alias_map)
        # The right side is the join expression or a table reference
        right = None
        for ref in join.find_all(exp.Table):
            r = _resolve(ref.name, alias_map)
            if r != left:
                right = r
                break
        if right:
            pairs.add(tuple(sorted([left, right])))

    # Implicit joins: adjacent tables in the FROM clause that aren't
    # already captured by explicit join pairs
    if len(from_tables) >= 2:
        for i in range(1, len(from_tables)):
            a = _resolve(from_tables[i - 1].name, alias_map)
            b = _resolve(from_tables[i].name, alias_map)
            pairs.add(tuple(sorted([a, b])))

    return pairs


def _normalize_filter(sql: str) -> str:
    """Canonicalize a SQL filter string for equality comparison."""
    # Remove whitespace, lowercase, strip parens
    normalized = re.sub(r'\s+', ' ', sql).strip().lower()
    return normalized


def _extract_filter_predicates(tree) -> Set[str]:
    """Extract normalized WHERE filter predicates."""
    predicates: Set[str] = set()
    where = tree.find(exp.Where)
    if where:
        # Walk AND-separated conditions
        for condition in where.find_all(exp.Condition):
            predicates.add(_normalize_filter(condition.sql()))
    return predicates


def _extract_columns_per_table_from_sql(
    sql: str,
    column_schema: Optional[Dict[str, Set[str]]] = None,
) -> Dict[str, Set[str]]:
    """Standalone column extraction (can be called without a full SQLObject)."""
    tree = sqlglot.parse_one(sql)
    alias_map = _resolve_aliases(tree)
    return _extract_columns_per_table(tree, alias_map, column_schema)


def parse_sql_object(
    sql: str,
    table_stats: Dict[str, TableStats],
    column_schema: Optional[Dict[str, Set[str]]] = None,
) -> SQLObject:
    """
    Walk the AST and extract table set, join pairs, and per-table columns.

    If `column_schema` is provided (table → set of column names), unqualified
    column references (bare 'n_name' instead of 'nation.n_name') are resolved
    to their owning tables.  This is essential for TPC-H-style SQL where
    columns are almost never qualified.
    """
    tree = sqlglot.parse_one(sql)
    alias_map = _resolve_aliases(tree)

    def resolve(name: str) -> str:
        return _resolve(name, alias_map)

    # ── Tables ──────────────────────────────────────────────────────────
    all_tables: Set[str] = {
        resolve(tbl.name) for tbl in tree.find_all(exp.Table)
    }

    # ── Join pairs ──────────────────────────────────────────────────────
    join_pairs = _extract_join_pairs(tree, alias_map)

    # ── Fact / dimension split ──────────────────────────────────────────
    fact_tables = {
        t for t in all_tables
        if table_stats.get(t, TableStats(0, False)).is_fact
    }

    # ── Per-table columns (with optional schema resolution) ─────────────
    columns_pt = _extract_columns_per_table(tree, alias_map, column_schema)

    # ── Aggregates, GROUP BY, filters ───────────────────────────────────
    aggregates = _extract_aggregates(tree)
    groupby_cols = _extract_groupby(tree)
    filter_predicates = _extract_filter_predicates(tree)

    return SQLObject(
        sql=sql,
        tables=all_tables,
        fact_tables=fact_tables,
        dim_tables=all_tables - fact_tables,
        join_pairs=join_pairs,
        columns_per_table=columns_pt,
        aggregates=aggregates,
        groupby_cols=groupby_cols,
        filter_predicates=filter_predicates,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Component extraction (for SentenceTransformer embedding)
# ─────────────────────────────────────────────────────────────────────────────

def extract_components(sql: str) -> dict:
    """
    Parse SQL and group each clause by the tables it references.
    Returns a dict: { table_name: [clause_strings] }
    """
    tree = sqlglot.parse_one(sql)
    components = defaultdict(list)

    # Extract each join condition, keeping which table it touches
    for join in tree.find_all(exp.Join):
        table_name = join.this.name.lower()
        components[table_name].append(join.sql())

    # Extract WHERE predicates per referenced table
    where = tree.find(exp.Where)
    if where:
        for condition in where.find_all(exp.Condition):
            for col in condition.find_all(exp.Column):
                if col.table:
                    components[col.table.lower()].append(condition.sql())

    # Extract SELECT expressions per table
    for sel in tree.find_all(exp.Select):
        for expr in sel.expressions:
            for col in expr.find_all(exp.Column):
                if col.table:
                    components[col.table.lower()].append(expr.sql())

    # Always keep the full SQL as the structural anchor
    components['__full__'] = [sql]

    return dict(components)


# ─────────────────────────────────────────────────────────────────────────────
# Table weighting (log-row-count, fact-boosted)
# ─────────────────────────────────────────────────────────────────────────────

class TableWeighter:
    def __init__(
        self,
        table_stats: Dict[str, TableStats],
        method: str = "log_rows",   # log_rows | explicit | hybrid
        fact_boost: float = 2.0     # multiplier for explicitly labeled fact tables
    ):
        self.stats = table_stats
        self.method = method
        self.fact_boost = fact_boost

    def compute_weights(self) -> Dict[str, float]:
        raw = {}

        for table, stats in self.stats.items():
            if self.method == "log_rows":
                w = np.log1p(stats.row_count)

            elif self.method == "explicit":
                w = self.fact_boost if stats.is_fact else 1.0

            elif self.method == "hybrid":
                w = np.log1p(stats.row_count)
                if stats.is_fact:
                    w *= self.fact_boost
                w *= (1 + 0.1 * stats.join_count)

            raw[table] = w

        total = sum(raw.values()) + 1e-8
        return {t: w / total for t, w in raw.items()}


# ─────────────────────────────────────────────────────────────────────────────
# SentenceTransformer component embedder with weighted pooling
# ─────────────────────────────────────────────────────────────────────────────

from sentence_transformers import SentenceTransformer
import torch
import torch.nn.functional as F


class ComponentEmbedder:
    """Embeds SQL clauses per table, then pools with table weights + alpha blend."""

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_components(
        self,
        components: Dict[str, list],
        weights: Dict[str, float]
    ) -> torch.Tensor:
        """
        Embed each table's clauses separately, then pool with table weights.
        The full SQL is always embedded as a structural anchor.

        Hard constraints (containment, over-join) are expected to be checked
        BEFORE calling this function — see view_query_similarity().
        """
        table_embeddings = {}

        for table, clauses in components.items():
            if table == '__full__':
                continue
            if not clauses:
                continue

            clause_text = " | ".join(clauses)
            emb = self.model.encode(clause_text, convert_to_tensor=True)
            table_embeddings[table] = emb

        if not table_embeddings:
            return self.model.encode(components['__full__'][0], convert_to_tensor=True)

        # ── Weighted pooling ──────────────────────────────────────────
        # final = Σ ( weight_t × embedding_t )  for all tables t
        weighted_sum = None
        total_weight = 0.0

        for table, emb in table_embeddings.items():
            w = weights.get(table, 1e-3)
            scaled = w * emb
            weighted_sum = scaled if weighted_sum is None else weighted_sum + scaled
            total_weight += w

        weighted_embedding = weighted_sum / (total_weight + 1e-8)

        # ── Structural anchor fusion (alpha blend) ─────────────────────
        # Blend the weighted per-table embedding with the full SQL embedding.
        # The alpha blend ONLY runs after containment checks have passed
        # (enforced in view_query_similarity), so the full SQL embedding
        # does NOT mask containment failures.
        full_sql_emb = self.model.encode(
            components['__full__'][0],
            convert_to_tensor=True
        )
        alpha = 0.7
        final = alpha * weighted_embedding + (1 - alpha) * full_sql_emb

        return F.normalize(final, dim=0)


def weighted_pool(
    embeddings: Dict[str, torch.Tensor],
    weights: Dict[str, float],
) -> torch.Tensor:
    """
    Standalone weighted pooling function.
    Sums embeddings scaled by their per-table weights, then L2-normalizes.
    """
    weighted_sum = None
    total_weight = 0.0

    for table, emb in embeddings.items():
        w = weights.get(table, 1e-8)
        scaled = w * emb
        weighted_sum = scaled if weighted_sum is None else weighted_sum + scaled
        total_weight += w

    pooled = weighted_sum / (total_weight + 1e-8)
    return F.normalize(pooled, dim=0)


# ─────────────────────────────────────────────────────────────────────────────
# Weight computation (standalone, for asymmetric query-side weights)
# ─────────────────────────────────────────────────────────────────────────────

def compute_weights(
    tables: Set[str],
    table_stats: Dict[str, TableStats],
    fact_boost: float = 3.0,
) -> Dict[str, float]:
    """
    Log-row-count weights with fact-table boost, normalized over `tables`.

      w(t) = log(1 + row_count(t)) × (fact_boost if is_fact else 1.0)

    Normalized so Σ w(t) = 1 over the given table set.
    """
    raw: Dict[str, float] = {}
    for t in tables:
        stats = table_stats.get(t, TableStats(row_count=1_000, is_fact=False))
        w = np.log1p(stats.row_count)
        if stats.is_fact:
            w *= fact_boost
        raw[t] = w

    total = sum(raw.values()) + 1e-9
    return {t: w / total for t, w in raw.items()}


# ─────────────────────────────────────────────────────────────────────────────
# Structural equality check
# ─────────────────────────────────────────────────────────────────────────────

def _sql_tree_hash(tree) -> str:
    """
    Produce a canonical hash of a SQL AST for equality comparison.
    Normalizes table/column names and removes aliases.
    """
    # Collect key structural elements sorted for deterministic comparison
    tables = sorted({t.name.lower() for t in tree.find_all(exp.Table)})

    # Join types and conditions
    joins = []
    for j in tree.find_all(exp.Join):
        kind = j.kind if j.kind else "IMPLICIT"
        cond = j.this.sql().lower() if j.this else ""
        joins.append(f"{kind}:{cond}")

    # Column references in SELECT
    selects = []
    for sel in tree.find_all(exp.Select):
        for expr in sel.expressions:
            selects.append(expr.sql())

    # WHERE conditions (normalized)
    wheres = []
    for w in tree.find_all(exp.Where):
        wheres.append(_normalize_filter(w.this.sql()))

    # GROUP BY
    groupbys = []
    for g in tree.find_all(exp.Group):
        for expr in g.expressions:
            groupbys.append(expr.sql())

    # Aggregate functions
    aggs = []
    for a in tree.find_all(exp.AggFunc):
        aggs.append(f"{a.sql_name()}({','.join(e.name.lower() if hasattr(e, 'name') else e.sql() for e in a.expressions)})")

    parts = [
        "TABLES:" + ",".join(tables),
        "JOINS:" + ";".join(sorted(joins)),
        "SELECT:" + ";".join(sorted(selects)),
        "WHERE:" + ";".join(sorted(wheres)),
        "GROUPBY:" + ";".join(sorted(groupbys)),
        "AGGS:" + ";".join(sorted(aggs)),
    ]
    return "|".join(parts)


def _structurally_equal(view: SQLObject, query: SQLObject) -> bool:
    """
    Check if view and query are structurally identical.
    Returns True only if they have the same:
      - Tables (same set)
      - Join pairs (same set)
      - Per-table columns (same set per table)
      - Aggregate functions (same signatures)
      - Group By columns (same set)
      - Filter predicates (same set, normalized)
    """
    # Quick structural checks
    if view.tables != query.tables:
        return False
    if view.join_pairs != query.join_pairs:
        return False
    if view.aggregates != query.aggregates:
        return False
    if view.groupby_cols != query.groupby_cols:
        return False
    if view.filter_predicates != query.filter_predicates:
        return False

    # Per-table column check: for shared tables, column sets must match
    for table in view.tables:
        view_cols = set(view.columns_per_table.get(table, set()))
        query_cols = set(query.columns_per_table.get(table, set()))
        if view_cols != query_cols:
            return False

    # Also check unqualified columns
    v_unqual = set(view.columns_per_table.get('__unqualified__', set()))
    q_unqual = set(query.columns_per_table.get('__unqualified__', set()))
    if v_unqual != q_unqual:
        return False

    return True


# ─────────────────────────────────────────────────────────────────────────────
# Similarity — embeddings with hard constraint guard
# ─────────────────────────────────────────────────────────────────────────────

def view_query_similarity(
    view_obj:      SQLObject,
    query_obj:     SQLObject,
    table_stats:   Dict[str, TableStats],
    fact_boost:    float = 3.0,
    alpha:         float = 0.7,
    embedder:      Optional[ComponentEmbedder] = None,
    column_schema: Optional[Dict[str, Set[str]]] = None,
) -> float:
    """
    Similarity between a candidate view and a query.

    HARD CONSTRAINTS (checked BEFORE any embedding computation → 0.0 if fail):
        1. |view.tables| > |query.tables|                         (over-joined)
        2. view.tables  ⊄  query.tables                           (foreign tables)
        3. columns(view, view_tables) ⊄ columns(query, view_tables)
           ↳ For each shared table t in view.tables, the query's required
             columns from t must be available in the view.

    PERFECT EQUALITY:
        If view is structurally identical to query → 1.0

    EMBEDDING-BASED SIMILARITY (only after constraints pass):
        score = cosine(query_w_emb, view_w_emb)

    PARAMETERS:
        column_schema: Optional[Dict[str, Set[str]]]
            Maps table → set of column names, e.g.
            {"lineitem": {"l_orderkey", "l_extendedprice", ...}}.
            When provided, unqualified column references (bare 'n_name') are
            resolved to their owning tables during parsing, making the column
            containment check accurate even for TPC-H-style unqualified SQL.
            When omitted, unqualified columns fall into '__unqualified__'
            and containment is skipped (too strict without schema context).

    Design rationale:
        - Alpha blend runs AFTER containment check so the full SQL embedding
          cannot mask containment violations.
    """
    # ═══════════════════════════════════════════════════════════════════
    # PHASE 1: Hard constraints (return 0.0 immediately on any failure)
    # ═══════════════════════════════════════════════════════════════════

    # ── H1: view must not join MORE tables than query ───────────
    if len(view_obj.tables) > len(query_obj.tables):
        return 0.0

    # ── H2: every view table must be present in the query ───────
    if not view_obj.tables.issubset(query_obj.tables):
        return 0.0

    # ── H3: column containment ──────────────────────────────────
    #   For each table t shared by view and query, the query's required
    #   columns from t must be a subset of what the view provides.
    #
    #   When column_schema is provided, unqualified columns get resolved
    #   to their tables during parsing, so the per-table check works
    #   correctly even for TPC-H-style bare column names.
    #
    #   When column_schema is NOT provided, we conservatively skip the
    #   __unqualified__ check (it's too strict to require ALL unqualified
    #   query columns — a view over just lineitem+orders shouldn't fail
    #   just because the query also uses columns from nation).

    for table in view_obj.tables:
        query_cols = query_obj.columns_per_table.get(table, set())
        view_cols  = view_obj.columns_per_table.get(table, set())
        if not query_cols.issubset(view_cols):
            return 0.0

    # Unqualified column check: only enforce if we have a schema to
    # resolve them.  Without a schema, __unqualified__ contains bare
    # names from ALL query tables and the check becomes meaningless.
    q_unqual = query_obj.columns_per_table.get('__unqualified__', set())
    v_unqual = view_obj.columns_per_table.get('__unqualified__', set())
    if column_schema is not None:
        # Schema was provided; unqualified columns should have been resolved
        # but some may remain if the column name is missing from schema.
        if q_unqual and not q_unqual.issubset(v_unqual):
            return 0.0
    # else: no schema → skip unqualified check (lenient for TPC-H)

    # ═══════════════════════════════════════════════════════════════════
    # PHASE 2: Perfect equality → 1.0
    # ═══════════════════════════════════════════════════════════════════

    if _structurally_equal(view_obj, query_obj):
        return 1.0

    # ═══════════════════════════════════════════════════════════════════
    # PHASE 3: Coverage-weight embedding similarity
    # ═══════════════════════════════════════════════════════════════════

    # ── Compute query-side weights (asymmetric, over query.tables) ──
    query_weights = compute_weights(query_obj.tables, table_stats, fact_boost)

    # ── Embed both view and query with the same query-side weights ──
    if embedder is None:
        embedder = ComponentEmbedder()

    view_components  = extract_components(view_obj.sql)
    query_components = extract_components(query_obj.sql)

    view_emb  = embedder.embed_components(view_components, query_weights)
    query_emb = embedder.embed_components(query_components, query_weights)

    # ── Cosine similarity ───────────────────────────────────────────
    similarity = float(F.cosine_similarity(
        view_emb.unsqueeze(0),
        query_emb.unsqueeze(0)
    ).item())

    # Clamp to [0, 1] (cosine can be slightly negative due to numerical noise)
    return max(0.0, min(1.0, similarity))


# ─────────────────────────────────────────────────────────────────────────────
# View selection pipeline
# ─────────────────────────────────────────────────────────────────────────────

class ViewSelectionPipeline:
    """
    Scores and ranks candidate materialized views against a query workload
    using embedding-based coverage-weight similarity with hard constraints.

    PARAMETERS:
        table_stats:    Dict[str, TableStats] — row counts, fact flags
        column_schema:  Optional[Dict[str, Set[str]]] — table → column names
                        for resolving unqualified column references (TPC-H).
                        When provided, column containment is accurate even
                        for bare column names like 'n_name'.
        fact_boost:     Float — multiplier for fact table weight (default 3.0)
        alpha:          Float — blend factor (default 0.7)
        embedder:       Optional[ComponentEmbedder] — SentenceTransformer
                        embedder (lazy-init if None)
    """

    def __init__(
        self,
        table_stats:   Dict[str, TableStats],
        column_schema: Optional[Dict[str, Set[str]]] = None,
        fact_boost:    float = 3.0,
        alpha:         float = 0.7,
        embedder:      Optional[ComponentEmbedder] = None,
    ):
        self.table_stats   = table_stats
        self.column_schema = column_schema
        self.fact_boost    = fact_boost
        self.alpha         = alpha
        self.embedder      = embedder

    def parse(self, sql: str) -> SQLObject:
        return parse_sql_object(sql, self.table_stats, self.column_schema)

    def _get_embedder(self) -> ComponentEmbedder:
        """Lazy init the SentenceTransformer embedder only when needed."""
        if self.embedder is None:
            self.embedder = ComponentEmbedder()
        return self.embedder

    def score_view(
        self,
        view_sql:       str,
        query_workload: List[str],
        candidate_id:   str = "",
    ) -> Dict:
        """
        Score one candidate view against the full workload.

        PARAMETERS:
            view_sql:       The candidate view's SQL definition.
            query_workload: List of query SQL strings to score against.
            candidate_id:   Optional human-readable label (e.g. "v1", "TPCH-Q1-view").
                            Included in the result dict for readability.
        """
        view_obj = self.parse(view_sql)
        scores: Dict[str, float] = {}

        for q_sql in query_workload:
            q_obj = self.parse(q_sql)
            scores[q_sql] = view_query_similarity(
                view_obj, q_obj,
                table_stats=self.table_stats,
                fact_boost=self.fact_boost,
                alpha=self.alpha,
                embedder=self._get_embedder(),
                column_schema=self.column_schema,
            )

        covered = [q for q, s in scores.items() if s > 0.0]

        return {
            "candidate_id":     candidate_id or self._auto_id(view_sql),
            "view_sql":         view_sql,
            "view_tables":      view_obj.tables,
            "view_fact_tables": view_obj.fact_tables,
            "per_query_scores": scores,
            "n_covered":        len(covered),
            "total_benefit":    sum(scores.values()),
            "avg_similarity":   sum(scores.values()) / max(len(query_workload), 1),
        }

    @staticmethod
    def _auto_id(sql: str) -> str:
        """Generate a short auto-ID from the SQL for readability."""
        import hashlib
        return hashlib.md5(sql.strip().encode()).hexdigest()[:8]

    def rank_views(
        self,
        candidate_views: List[str],
        query_workload:  List[str],
        candidate_ids:   Optional[List[str]] = None,
    ) -> List[Dict]:
        """
        Rank all candidate views by total benefit over the workload.

        PARAMETERS:
            candidate_views: List of candidate view SQL strings.
            query_workload:  List of query SQL strings to score against.
            candidate_ids:   Optional list of human-readable labels, one per
                             candidate view (same order). If omitted, auto-IDs
                             (first 8 hex chars of MD5) are generated.
        """
        ids = candidate_ids if candidate_ids else [""] * len(candidate_views)
        results = [
            self.score_view(v, query_workload, cid)
            for v, cid in zip(candidate_views, ids)
        ]
        return sorted(results, key=lambda r: r["total_benefit"], reverse=True)


# ─────────────────────────────────────────────────────────────────────────────
# Legacy compatibility: WeightedSQLEmbedder
# ─────────────────────────────────────────────────────────────────────────────

class WeightedSQLEmbedder:
    """
    Simple embed-SQL → vector utility (no similarity/scoring).
    Uses SentenceTransformer with per-table weighted pooling and alpha blend.
    """

    def __init__(
        self,
        table_stats: Dict[str, TableStats],
        alpha: float = 0.7,
    ):
        self.weighter = TableWeighter(table_stats, method="hybrid", fact_boost=2.0)
        self.embedder = ComponentEmbedder()
        self.weights  = self.weighter.compute_weights()
        self.alpha    = alpha

    def embed(self, sql: str) -> torch.Tensor:
        components = extract_components(sql)
        return self.embedder.embed_components(components, self.weights)

    def embed_batch(self, queries: List[str]) -> torch.Tensor:
        return torch.stack([self.embed(q) for q in queries])


# ─────────────────────────────────────────────────────────────────────────────
# Example — TPC-H
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    table_stats = {
        "lineitem": TableStats(row_count=6_000_000, is_fact=True,  join_count=5),
        "orders":   TableStats(row_count=1_500_000, is_fact=True,  join_count=4),
        "partsupp": TableStats(row_count=  800_000, is_fact=True,  join_count=2),
        "customer": TableStats(row_count=  150_000, is_fact=False, join_count=2),
        "part":     TableStats(row_count=  200_000, is_fact=False, join_count=2),
        "supplier": TableStats(row_count=   10_000, is_fact=False, join_count=2),
        "nation":   TableStats(row_count=       25, is_fact=False, join_count=1),
        "region":   TableStats(row_count=        5, is_fact=False, join_count=1),
    }

    # TPC-H column schema for resolving unqualified column names
    column_schema = {
        "lineitem": ["l_orderkey", "l_partkey", "l_suppkey", "l_linenumber",
                     "l_quantity", "l_extendedprice", "l_discount", "l_tax",
                     "l_returnflag", "l_linestatus", "l_shipdate",
                     "l_commitdate", "l_receiptdate", "l_shipinstruct",
                     "l_shipmode", "l_comment"],
        "orders":   ["o_orderkey", "o_custkey", "o_orderstatus",
                     "o_totalprice", "o_orderdate", "o_orderpriority",
                     "o_clerk", "o_shippriority", "o_comment"],
        "customer": ["c_custkey", "c_name", "c_address", "c_nationkey",
                     "c_phone", "c_acctbal", "c_mktsegment", "c_comment"],
        "supplier": ["s_suppkey", "s_name", "s_address", "s_nationkey",
                     "s_phone", "s_acctbal", "s_comment"],
        "part":     ["p_partkey", "p_name", "p_mfgr", "p_brand",
                     "p_type", "p_size", "p_container", "p_retailprice",
                     "p_comment"],
        "partsupp": ["ps_partkey", "ps_suppkey", "ps_availqty",
                     "ps_supplycost", "ps_comment"],
        "nation":   ["n_nationkey", "n_name", "n_regionkey", "n_comment"],
        "region":   ["r_regionkey", "r_name", "r_comment"],
    }
    column_schema = {k.lower(): {c.lower() for c in v} for k, v in column_schema.items()}

    query = """
    select supp_nation, cust_nation, l_year, sum(volume) as revenue
        from (
        select n1.n_name as supp_nation, n2.n_name as cust_nation,
                extract(year from l_shipdate) as l_year,
                l_extendedprice * (1 - l_discount) as volume
        from supplier, lineitem, orders, customer, nation n1, nation n2
        where
        s_suppkey = l_suppkey
        and o_orderkey = l_orderkey
        and c_custkey = o_custkey
        and s_nationkey = n1.n_nationkey
        and c_nationkey = n2.n_nationkey
        and (
            (n1.n_name = 'CHINA' and n2.n_name = 'RUSSIA')
            or (n1.n_name = 'RUSSIA' and n2.n_name = 'CHINA')
        )
        and l_shipdate between date '1992-01-01' and date '1992-12-31'
        ) as shipping
    group by supp_nation, cust_nation, l_year
    order by supp_nation, cust_nation, l_year;
    """
    
    view_candidates = [
        """
        select supp_nation, cust_nation, l_year, sum(volume) as revenue
        from (
        select n1.n_name as supp_nation, n2.n_name as cust_nation,
                extract(year from l_shipdate) as l_year,
                l_extendedprice * (1 - l_discount) as volume
        from supplier, lineitem, orders, customer, nation n1, nation n2
    where
        s_suppkey = l_suppkey
        and o_orderkey = l_orderkey
        and c_custkey = o_custkey
        and s_nationkey = n1.n_nationkey
        and c_nationkey = n2.n_nationkey
        and (
            (n1.n_name = 'ETHIOPIA' and n2.n_name = 'JAPAN')
            or (n1.n_name = 'JAPAN' and n2.n_name = 'ETHIOPIA')
        )
        and l_shipdate between date '1992-01-01' and date '1992-12-31'
    ) as shipping
    group by supp_nation, cust_nation, l_year
    order by supp_nation, cust_nation, l_year;
    """, """
        select n1.n_name as supp_nation, n2.n_name as cust_nation,
                extract(year from l_shipdate) as l_year,
                l_extendedprice * (1 - l_discount) as volume
        from supplier, lineitem, orders, customer, nation n1, nation n2
    where
        s_suppkey = l_suppkey
        and o_orderkey = l_orderkey
        and c_custkey = o_custkey
        and s_nationkey = n1.n_nationkey
        and c_nationkey = n2.n_nationkey
        and l_shipdate between date '1992-01-01' and date '1992-12-31'"""
    ]
    pipeline = ViewSelectionPipeline(table_stats, column_schema=column_schema, fact_boost=3.0)
    ranked = pipeline.rank_views(view_candidates, [query])

    print(f"{'ID':<30} {'Tables':<30} {'Score':<8}")
    print("-" * 90)
    for r in ranked :
        cid = r["candidate_id"]
        tables = ", ".join(sorted(r["view_tables"]))
        score = r["avg_similarity"]
        print(f"{cid:<30} {tables:<30} {score:<8.4f}")
