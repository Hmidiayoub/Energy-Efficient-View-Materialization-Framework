"""
schemas.py — TPC-H and TPC-DS Schema Definitions
=================================================

Centralizes all table statistics, column schemas, and table-type constants
so every pipeline step references a single source of truth.

Usage:
    from schemas import ACTIVE, TPCH, TPCDS
    
    # Switch schema before running pipeline:
    ACTIVE = TPCH      # default
    ACTIVE = TPCDS
    
Every step reads ACTIVE.table_stats, ACTIVE.column_schema, etc. at call time.
"""
from candidate_views_extractor import TableStats as _TableStats


# ─────────────────────────────────────────────────────────────────────────────
# Schema container
# ─────────────────────────────────────────────────────────────────────────────

class Schema:
    """Holds all per-database-schema information needed by the pipeline."""
    def __init__(
        self,
        table_stats,
        column_schema,
        dimension_tables,
        nation_region_tables,
    ):
        self.table_stats = table_stats
        self.column_schema = column_schema
        self.dimension_tables = dimension_tables
        self.nation_region_tables = nation_region_tables


def _normalize_column_schema(raw):
    """Lowercase keys and values in a column schema dict."""
    return {k.lower(): {c.lower() for c in v} for k, v in raw.items()}


# ─────────────────────────────────────────────────────────────────────────────
# TPC-H Schema  (values aligned with main.py — the canonical runner)
# ─────────────────────────────────────────────────────────────────────────────

TPCH_TABLE_STATS = {
    "lineitem":  _TableStats(6_000_000, True, 7),
    "orders":    _TableStats(1_500_000, True, 2),
    "customer":  _TableStats(150_000, False, 1),
    "part":      _TableStats(200_000, False, 2),
    "partsupp":  _TableStats(800_000, False, 2),
    "supplier":  _TableStats(10_000, False, 1),
    "nation":    _TableStats(25, False, 2),
    "region":    _TableStats(5, False, 1),
}

TPCH_COLUMN_SCHEMA = _normalize_column_schema({
    "lineitem": {"l_orderkey","l_partkey","l_suppkey","l_linenumber","l_quantity",
                 "l_extendedprice","l_discount","l_tax","l_returnflag","l_linestatus",
                 "l_shipdate","l_commitdate","l_receiptdate","l_shipinstruct","l_shipmode","l_comment"},
    "orders":   {"o_orderkey","o_custkey","o_orderstatus","o_totalprice","o_orderdate",
                 "o_orderpriority","o_clerk","o_shippriority","o_comment"},
    "customer": {"c_custkey","c_name","c_address","c_nationkey","c_phone",
                 "c_acctbal","c_mktsegment","c_comment"},
    "supplier": {"s_suppkey","s_name","s_address","s_nationkey","s_phone","s_acctbal","s_comment"},
    "part":     {"p_partkey","p_name","p_mfgr","p_brand","p_type","p_size","p_container","p_retailprice","p_comment"},
    "partsupp": {"ps_partkey","ps_suppkey","ps_availqty","ps_supplycost","ps_comment"},
    "nation":   {"n_nationkey","n_name","n_regionkey","n_comment"},
    "region":   {"r_regionkey","r_name","r_comment"},
})

TPCH_DIMENSION_TABLES = {"customer", "supplier", "part", "nation", "region"}
TPCH_NATION_REGION_TABLES = {"nation", "region"}

TPCH = Schema(
    table_stats=TPCH_TABLE_STATS,
    column_schema=TPCH_COLUMN_SCHEMA,
    dimension_tables=TPCH_DIMENSION_TABLES,
    nation_region_tables=TPCH_NATION_REGION_TABLES,
)


# ─────────────────────────────────────────────────────────────────────────────
# TPC-DS Schema (SF=1 approximate)
# ─────────────────────────────────────────────────────────────────────────────

TPCDS_TABLE_STATS = {
    "store_sales":       _TableStats(864000,   True, 7),
    "store_returns":     _TableStats(287000,   True, 5),
    "catalog_sales":     _TableStats(144000,   True, 7),
    "catalog_returns":   _TableStats(144000,   True, 5),
    "web_sales":         _TableStats(72000,    True, 7),
    "web_returns":       _TableStats(72000,    True, 5),
    "inventory":         _TableStats(17400000, True, 3),
    "customer":          _TableStats(100000,    False, 2),
    "customer_address":  _TableStats(50000,     False, 1),
    "customer_demographics": _TableStats(1920800, False, 1),
    "date_dim":          _TableStats(73000,     False, 6),
    "household_demographics": _TableStats(720,  False, 1),
    "income_band":       _TableStats(20,        False, 0),
    "item":              _TableStats(18000,     False, 3),
    "promotion":         _TableStats(300,       False, 2),
    "reason":            _TableStats(35,        False, 0),
    "ship_mode":         _TableStats(20,        False, 0),
    "store":             _TableStats(12,        False, 0),
    "time_dim":          _TableStats(86400,     False, 1),
    "warehouse":         _TableStats(5,         False, 1),
    "web_page":          _TableStats(60,        False, 1),
    "web_site":          _TableStats(6,         False, 1),
    "call_center":       _TableStats(6,         False, 0),
    "dbgen_version":     _TableStats(1,         False, 0),
}

# TPC-DS has no pre-defined column_schema — extractor works without it.
TPCDS_COLUMN_SCHEMA = ({
  "call_center": {
    "cc_call_center_sk",
    "cc_call_center_id",
    "cc_rec_start_date",
    "cc_rec_end_date",
    "cc_closed_date_sk",
    "cc_open_date_sk",
    "cc_name",
    "cc_class",
    "cc_employees",
    "cc_sq_ft",
    "cc_hours",
    "cc_manager",
    "cc_mkt_id",
    "cc_mkt_class",
    "cc_mkt_desc",
    "cc_market_manager",
    "cc_division",
    "cc_division_name",
    "cc_company",
    "cc_company_name",
    "cc_street_number",
    "cc_street_name",
    "cc_street_type",
    "cc_suite_number",
    "cc_city",
    "cc_county",
    "cc_state",
    "cc_zip",
    "cc_country",
    "cc_gmt_offset",
    "cc_tax_percentage"
},
  "catalog_page": {
    "cp_catalog_page_sk",
    "cp_catalog_page_id",
    "cp_start_date_sk",
    "cp_end_date_sk",
    "cp_department",
    "cp_catalog_number",
    "cp_catalog_page_number",
    "cp_description",
    "cp_type"
},
  "catalog_returns": {
    "cr_returned_date_sk",
    "cr_returned_time_sk",
    "cr_item_sk",
    "cr_refunded_customer_sk",
    "cr_refunded_cdemo_sk",
    "cr_refunded_hdemo_sk",
    "cr_refunded_addr_sk",
    "cr_returning_customer_sk",
    "cr_returning_cdemo_sk",
    "cr_returning_hdemo_sk",
    "cr_returning_addr_sk",
    "cr_call_center_sk",
    "cr_catalog_page_sk",
    "cr_ship_mode_sk",
    "cr_warehouse_sk",
    "cr_reason_sk",
    "cr_order_number",
    "cr_return_quantity",
    "cr_return_amount",
    "cr_return_tax",
    "cr_return_amt_inc_tax",
    "cr_fee",
    "cr_return_ship_cost",
    "cr_refunded_cash",
    "cr_reversed_charge",
    "cr_store_credit",
    "cr_net_loss"
},
  "catalog_sales": {
    "cs_sold_date_sk",
    "cs_sold_time_sk",
    "cs_ship_date_sk",
    "cs_bill_customer_sk",
    "cs_bill_cdemo_sk",
    "cs_bill_hdemo_sk",
    "cs_bill_addr_sk",
    "cs_ship_customer_sk",
    "cs_ship_cdemo_sk",
    "cs_ship_hdemo_sk",
    "cs_ship_addr_sk",
    "cs_call_center_sk",
    "cs_catalog_page_sk",
    "cs_ship_mode_sk",
    "cs_warehouse_sk",
    "cs_item_sk",
    "cs_promo_sk",
    "cs_order_number",
    "cs_quantity",
    "cs_wholesale_cost",
    "cs_list_price",
    "cs_sales_price",
    "cs_ext_discount_amt",
    "cs_ext_sales_price",
    "cs_ext_wholesale_cost",
    "cs_ext_list_price",
    "cs_ext_tax",
    "cs_coupon_amt",
    "cs_ext_ship_cost",
    "cs_net_paid",
    "cs_net_paid_inc_tax",
    "cs_net_paid_inc_ship",
    "cs_net_paid_inc_ship_tax",
    "cs_net_profit"
},
  "customer": {
    "c_customer_sk",
    "c_customer_id",
    "c_current_cdemo_sk",
    "c_current_hdemo_sk",
    "c_current_addr_sk",
    "c_first_shipto_date_sk",
    "c_first_sales_date_sk",
    "c_salutation",
    "c_first_name",
    "c_last_name",
    "c_preferred_cust_flag",
    "c_birth_day",
    "c_birth_month",
    "c_birth_year",
    "c_birth_country",
    "c_login",
    "c_email_address",
    "c_last_review_date"
},
  "customer_address": {
    "ca_address_sk",
    "ca_address_id",
    "ca_street_number",
    "ca_street_name",
    "ca_street_type",
    "ca_suite_number",
    "ca_city",
    "ca_county",
    "ca_state",
    "ca_zip",
    "ca_country",
    "ca_gmt_offset",
    "ca_location_type"
},
  "customer_demographics": {
    "cd_demo_sk",
    "cd_gender",
    "cd_marital_status",
    "cd_education_status",
    "cd_purchase_estimate",
    "cd_credit_rating",
    "cd_dep_count",
    "cd_dep_employed_count",
    "cd_dep_college_count"
},
  "date_dim": {
    "d_date_sk",
    "d_date_id",
    "d_date",
    "d_month_seq",
    "d_week_seq",
    "d_quarter_seq",
    "d_year",
    "d_dow",
    "d_moy",
    "d_dom",
    "d_qoy",
    "d_fy_year",
    "d_fy_quarter_seq",
    "d_fy_week_seq",
    "d_day_name",
    "d_quarter_name",
    "d_holiday",
    "d_weekend",
    "d_following_holiday",
    "d_first_dom",
    "d_last_dom",
    "d_same_day_ly",
    "d_same_day_lq",
    "d_current_day",
    "d_current_week",
    "d_current_month",
    "d_current_quarter",
    "d_current_year"
},
  "dbgen_version": {
    "dv_version",
    "dv_create_date",
    "dv_create_time",
    "dv_cmdline_args"
},
  "household_demographics": {
    "hd_demo_sk",
    "hd_income_band_sk",
    "hd_buy_potential",
    "hd_dep_count",
    "hd_vehicle_count"
},
  "income_band": {
    "ib_income_band_sk",
    "ib_lower_bound",
    "ib_upper_bound"
},
  "inventory": {
    "inv_date_sk",
    "inv_item_sk",
    "inv_warehouse_sk",
    "inv_quantity_on_hand"
},
  "item": {
    "i_item_sk",
    "i_item_id",
    "i_rec_start_date",
    "i_rec_end_date",
    "i_item_desc",
    "i_current_price",
    "i_wholesale_cost",
    "i_brand_id",
    "i_brand",
    "i_class_id",
    "i_class",
    "i_category_id",
    "i_category",
    "i_manufact_id",
    "i_manufact",
    "i_size",
    "i_formulation",
    "i_color",
    "i_units",
    "i_container",
    "i_manager_id",
    "i_product_name"
},
  "pg_stat_statements": {
    "userid",
    "dbid",
    "toplevel",
    "queryid",
    "query",
    "plans",
    "total_plan_time",
    "min_plan_time",
    "max_plan_time",
    "mean_plan_time",
    "stddev_plan_time",
    "calls",
    "total_exec_time",
    "min_exec_time",
    "max_exec_time",
    "mean_exec_time",
    "stddev_exec_time",
    "rows",
    "shared_blks_hit",
    "shared_blks_read",
    "shared_blks_dirtied",
    "shared_blks_written",
    "local_blks_hit",
    "local_blks_read",
    "local_blks_dirtied",
    "local_blks_written",
    "temp_blks_read",
    "temp_blks_written",
    "shared_blk_read_time",
    "shared_blk_write_time",
    "local_blk_read_time",
    "local_blk_write_time",
    "temp_blk_read_time",
    "temp_blk_write_time",
    "wal_records",
    "wal_fpi",
    "wal_bytes",
    "jit_functions",
    "jit_generation_time",
    "jit_inlining_count",
    "jit_inlining_time",
    "jit_optimization_count",
    "jit_optimization_time",
    "jit_emission_count",
    "jit_emission_time",
    "jit_deform_count",
    "jit_deform_time",
    "stats_since",
    "minmax_stats_since"
},
  "pg_stat_statements_info": {
    "dealloc",
    "stats_reset"
},
  "promotion": {
    "p_promo_sk",
    "p_promo_id",
    "p_start_date_sk",
    "p_end_date_sk",
    "p_item_sk",
    "p_cost",
    "p_response_target",
    "p_promo_name",
    "p_channel_dmail",
    "p_channel_email",
    "p_channel_catalog",
    "p_channel_tv",
    "p_channel_radio",
    "p_channel_press",
    "p_channel_event",
    "p_channel_demo",
    "p_channel_details",
    "p_purpose",
    "p_discount_active"
},
  "reason": {
    "r_reason_sk",
    "r_reason_id",
    "r_reason_desc"
  },
  "ship_mode": {
    "sm_ship_mode_sk",
    "sm_ship_mode_id",
    "sm_type",
    "sm_code",
    "sm_carrier",
    "sm_contract"
},
  "store": {
    "s_store_sk",
    "s_store_id",
    "s_rec_start_date",
    "s_rec_end_date",
    "s_closed_date_sk",
    "s_store_name",
    "s_number_employees",
    "s_floor_space",
    "s_hours",
    "s_manager",
    "s_market_id",
    "s_geography_class",
    "s_market_desc",
    "s_market_manager",
    "s_division_id",
    "s_division_name",
    "s_company_id",
    "s_company_name",
    "s_street_number",
    "s_street_name",
    "s_street_type",
    "s_suite_number",
    "s_city",
    "s_county",
    "s_state",
    "s_zip",
    "s_country",
    "s_gmt_offset",
    "s_tax_precentage"
},
  "store_returns": {
    "sr_returned_date_sk",
    "sr_return_time_sk",
    "sr_item_sk",
    "sr_customer_sk",
    "sr_cdemo_sk",
    "sr_hdemo_sk",
    "sr_addr_sk",
    "sr_store_sk",
    "sr_reason_sk",
    "sr_ticket_number",
    "sr_return_quantity",
    "sr_return_amt",
    "sr_return_tax",
    "sr_return_amt_inc_tax",
    "sr_fee",
    "sr_return_ship_cost",
    "sr_refunded_cash",
    "sr_reversed_charge",
    "sr_store_credit",
    "sr_net_loss"
  },
  "store_sales": {
    "ss_sold_date_sk",
    "ss_sold_time_sk",
    "ss_item_sk",
    "ss_customer_sk",
    "ss_cdemo_sk",
    "ss_hdemo_sk",
    "ss_addr_sk",
    "ss_store_sk",
    "ss_promo_sk",
    "ss_ticket_number",
    "ss_quantity",
    "ss_wholesale_cost",
    "ss_list_price",
    "ss_sales_price",
    "ss_ext_discount_amt",
    "ss_ext_sales_price",
    "ss_ext_wholesale_cost",
    "ss_ext_list_price",
    "ss_ext_tax",
    "ss_coupon_amt",
    "ss_net_paid",
    "ss_net_paid_inc_tax",
    "ss_net_profit"
},
  "time_dim": {
    "t_time_sk",
    "t_time_id",
    "t_time",
    "t_hour",
    "t_minute",
    "t_second",
    "t_am_pm",
    "t_shift",
    "t_sub_shift",
    "t_meal_time"
},
  "warehouse": {
    "w_warehouse_sk",
    "w_warehouse_id",
    "w_warehouse_name",
    "w_warehouse_sq_ft",
    "w_street_number",
    "w_street_name",
    "w_street_type",
    "w_suite_number",
    "w_city",
    "w_county",
    "w_state",
    "w_zip",
    "w_country",
    "w_gmt_offset"
},
  "web_page": {
    "wp_web_page_sk",
    "wp_web_page_id",
    "wp_rec_start_date",
    "wp_rec_end_date",
    "wp_creation_date_sk",
    "wp_access_date_sk",
    "wp_autogen_flag",
    "wp_customer_sk",
    "wp_url",
    "wp_type",
    "wp_char_count",
    "wp_link_count",
    "wp_image_count",
    "wp_max_ad_count"
},
  "web_returns": {
    "wr_returned_date_sk","wr_returned_time_sk","wr_item_sk","wr_refunded_customer_sk",
    "wr_refunded_cdemo_sk","wr_refunded_hdemo_sk","wr_refunded_addr_sk","wr_returning_customer_sk",
    "wr_returning_cdemo_sk","wr_returning_hdemo_sk","wr_returning_addr_sk","wr_web_page_sk",
    "wr_reason_sk","wr_order_number","wr_return_quantity","wr_return_amt","wr_return_tax","wr_return_amt_inc_tax",
    "wr_fee","wr_return_ship_cost","wr_refunded_cash","wr_reversed_charge","wr_account_credit","wr_net_loss"
},
  "web_sales": {
    "ws_sold_date_sk","ws_sold_time_sk","ws_ship_date_sk","ws_item_sk","ws_bill_customer_sk","ws_bill_cdemo_sk",
    "ws_bill_hdemo_sk","ws_bill_addr_sk","ws_ship_customer_sk","ws_ship_cdemo_sk","ws_ship_hdemo_sk",
    "ws_ship_addr_sk","ws_web_page_sk","ws_web_site_sk","ws_ship_mode_sk","ws_warehouse_sk","ws_promo_sk",
    "ws_order_number","ws_quantity","ws_wholesale_cost","ws_list_price","ws_sales_price","ws_ext_discount_amt",
    "ws_ext_sales_price","ws_ext_wholesale_cost","ws_ext_list_price","ws_ext_tax","ws_coupon_amt","ws_ext_ship_cost",
    "ws_net_paid","ws_net_paid_inc_tax","ws_net_paid_inc_ship","ws_net_paid_inc_ship_tax","ws_net_profit"},
  "web_site": {
    "web_site_sk","web_site_id","web_rec_start_date","web_rec_end_date","web_name","web_open_date_sk",
    "web_close_date_sk","web_class","web_manager","web_mkt_id","web_mkt_class","web_mkt_desc","web_market_manager",
    "web_company_id","web_company_name","web_street_number","web_street_name","web_street_type","web_suite_number",
    "web_city","web_county","web_state","web_zip","web_country","web_gmt_offset","web_tax_percentage"}
})

# TPC-DS dimension tables (every table not listed as fact above).
# No nation/region filter applies to TPC-DS.
TPCDS_DIMENSION_TABLES = {
    "customer", "customer_address", "customer_demographics", "date_dim",
    "household_demographics", "income_band", "item", "promotion",
    "reason", "ship_mode", "store", "time_dim", "warehouse",
    "web_page", "web_site", "call_center", "dbgen_version",
}
TPCDS_NATION_REGION_TABLES = set()

TPCDS = Schema(
    table_stats=TPCDS_TABLE_STATS,
    column_schema=TPCDS_COLUMN_SCHEMA,
    dimension_tables=TPCDS_DIMENSION_TABLES,
    nation_region_tables=TPCDS_NATION_REGION_TABLES,
)


# ─────────────────────────────────────────────────────────────────────────────
# Active schema  —  set by main.py / run_tpcds.py at startup
# ─────────────────────────────────────────────────────────────────────────────

ACTIVE = TPCH  # default
