workload_1 = [
        """
        select l_returnflag,
	    l_linestatus,
	    sum(l_quantity) as sum_qty,
	    sum(l_extendedprice) as sum_base_price,
	    sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
	    sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
	    avg(l_quantity) as avg_qty,
	    avg(l_extendedprice) as avg_price,
	    avg(l_discount) as avg_disc,
	    count(*) as count_order
        from lineitem
        where l_shipdate <= date '1992-12-01' - interval '3' day 
        group by l_returnflag, l_linestatus
        order by l_returnflag, l_linestatus;
            """
        , 
            """
        select l_returnflag,
	    l_linestatus,
	    sum(l_quantity) as sum_qty,
	    sum(l_extendedprice) as sum_base_price,
	    sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
	    sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
	    avg(l_quantity) as avg_qty,
	    avg(l_extendedprice) as avg_price,
	    avg(l_discount) as avg_disc,
	    count(*) as count_order
        from lineitem
        where l_shipdate <= date '1992-12-01' - interval '30' day 
        group by l_returnflag, l_linestatus
        order by l_returnflag, l_linestatus;
            """
        ,
            """ 
        select l_returnflag,
	    l_linestatus,
	    sum(l_quantity) as sum_qty,
	    sum(l_extendedprice) as sum_base_price,
	    sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
	    sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
	    avg(l_quantity) as avg_qty,
	    avg(l_extendedprice) as avg_price,
	    avg(l_discount) as avg_disc,
	    count(*) as count_order
        from lineitem
        where l_shipdate <= date '1992-12-01' - interval '300' day 
        group by l_returnflag, l_linestatus
        order by l_returnflag, l_linestatus;
            """
        ,
            """
        select l_returnflag,
	    l_linestatus,
	    sum(l_quantity) as sum_qty,
	    sum(l_extendedprice) as sum_base_price,
	    sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
	    sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
	    avg(l_quantity) as avg_qty,
	    avg(l_extendedprice) as avg_price,
	    avg(l_discount) as avg_disc,
	    count(*) as count_order
        from lineitem
        where l_shipdate <= date '1992-12-01' - interval '1000' day 
        group by l_returnflag, l_linestatus
        order by l_returnflag, l_linestatus;
            """
        ,
            """ 
        select l_returnflag,
	    l_linestatus,
	    sum(l_quantity) as sum_qty,
	    sum(l_extendedprice) as sum_base_price,
	    sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
	    sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
	    avg(l_quantity) as avg_qty,
	    avg(l_extendedprice) as avg_price,
	    avg(l_discount) as avg_disc,
	    count(*) as count_order
        from lineitem
        where l_shipdate <= date '1992-12-01' - interval '1500' day 
        group by l_returnflag, l_linestatus
        order by l_returnflag, l_linestatus;
            """
        ,
            """ 
        select l_returnflag,
	    l_linestatus,
	    sum(l_quantity) as sum_qty,
	    sum(l_extendedprice) as sum_base_price,
	    sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
	    sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
	    avg(l_quantity) as avg_qty,
	    avg(l_extendedprice) as avg_price,
	    avg(l_discount) as avg_disc,
	    count(*) as count_order
        from lineitem
        where l_shipdate <= date '1992-12-01' - interval '2000' day 
        group by l_returnflag, l_linestatus
        order by l_returnflag, l_linestatus;
            """
        ,
            """ 
        select l_returnflag,
	    l_linestatus,
	    sum(l_quantity) as sum_qty,
	    sum(l_extendedprice) as sum_base_price,
	    sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,
	    sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,
	    avg(l_quantity) as avg_qty,
	    avg(l_extendedprice) as avg_price,
	    avg(l_discount) as avg_disc,
	    count(*) as count_order
        from lineitem
        where l_shipdate <= date '1992-12-01' - interval '100' day 
        group by l_returnflag, l_linestatus
        order by l_returnflag, l_linestatus;
            """
        ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
             """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
        ,
        """
        select l_orderkey, sum(l_extendedprice * (1 - l_discount)) as revenue, o_orderdate, o_shippriority
        from customer, orders, lineitem
        where c_mktsegment = 'AUTOMOBILE'
	    and c_custkey = o_custkey
	    and l_orderkey = o_orderkey
	    and o_orderdate < date '1992-08-02'
	    and l_shipdate > date '1992-08-02'
        group by l_orderkey, o_orderdate, o_shippriority
        order by revenue desc, o_orderdate;
            """
        ,
        """
        select l_orderkey, sum(l_extendedprice * (1 - l_discount)) as revenue, o_orderdate, o_shippriority
        from customer, orders, lineitem
        where c_mktsegment = 'BUILDING'
	    and c_custkey = o_custkey
	    and l_orderkey = o_orderkey
	    and o_orderdate < date '1992-08-02'
	    and l_shipdate > date '1992-08-02'
        group by l_orderkey, o_orderdate, o_shippriority
        order by revenue desc, o_orderdate;
            """
        ,
        """
        select l_orderkey, sum(l_extendedprice * (1 - l_discount)) as revenue, o_orderdate, o_shippriority
        from customer, orders, lineitem
        where c_mktsegment = 'FURNITURE'
	    and c_custkey = o_custkey
	    and l_orderkey = o_orderkey
	    and o_orderdate < date '1992-08-02'
	    and l_shipdate > date '1992-08-02'
        group by l_orderkey, o_orderdate, o_shippriority
        order by revenue desc, o_orderdate;
            """
        ,
        """
        select l_orderkey, sum(l_extendedprice * (1 - l_discount)) as revenue, o_orderdate, o_shippriority
        from customer, orders, lineitem
        where c_mktsegment = 'HOUSEHOLD'
	    and c_custkey = o_custkey
	    and l_orderkey = o_orderkey
	    and o_orderdate < date '1992-08-02'
	    and l_shipdate > date '1992-08-02'
        group by l_orderkey, o_orderdate, o_shippriority
        order by revenue desc, o_orderdate;
            """
        ,
        """
        select l_orderkey, sum(l_extendedprice * (1 - l_discount)) as revenue, o_orderdate, o_shippriority
        from customer, orders, lineitem
        where c_mktsegment = 'MACHINERY'
	    and c_custkey = o_custkey
	    and l_orderkey = o_orderkey
	    and o_orderdate < date '1992-08-02'
	    and l_shipdate > date '1992-08-02'
        group by l_orderkey, o_orderdate, o_shippriority
        order by revenue desc, o_orderdate;
            """
        ,
        """
		select o_orderpriority, count(*) as order_count
		from orders
		where o_orderdate >= date '1992-01-01'
			and o_orderdate < date '1992-04-01' 
			and exists (select *
						from lineitem
						where l_orderkey = o_orderkey
							and l_commitdate < l_receiptdate
						)
		group by o_orderpriority
		order by o_orderpriority;
		"""
        ,
        """
		select n_name, sum(l_extendedprice * (1 - l_discount)) as revenue
		from customer, orders, lineitem, supplier, nation, region
		where c_custkey = o_custkey 
  			and l_orderkey = o_orderkey
			and l_suppkey = s_suppkey
			and c_nationkey = s_nationkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AFRICA'
			and o_orderdate >= date '1992-01-01'
			and o_orderdate < date '1996-01-01'
		group by n_name
		order by revenue desc;
        """
        ,
        """
		select n_name, sum(l_extendedprice * (1 - l_discount)) as revenue
		from customer, orders, lineitem, supplier, nation, region
		where c_custkey = o_custkey 
  			and l_orderkey = o_orderkey
			and l_suppkey = s_suppkey
			and c_nationkey = s_nationkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA'
			and o_orderdate >= date '1992-01-01'
			and o_orderdate < date '1996-01-01'
		group by n_name
		order by revenue desc;
		"""
        ,
        """
		select n_name, sum(l_extendedprice * (1 - l_discount)) as revenue
		from customer, orders, lineitem, supplier, nation, region
		where c_custkey = o_custkey 
  			and l_orderkey = o_orderkey
			and l_suppkey = s_suppkey
			and c_nationkey = s_nationkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA'
			and o_orderdate >= date '1992-01-01'
			and o_orderdate < date '1996-01-01'
		group by n_name
		order by revenue desc;
		"""
        ,
        """
		select n_name, sum(l_extendedprice * (1 - l_discount)) as revenue
		from customer, orders, lineitem, supplier, nation, region
		where c_custkey = o_custkey 
  			and l_orderkey = o_orderkey
			and l_suppkey = s_suppkey
			and c_nationkey = s_nationkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'EUROPE'
			and o_orderdate >= date '1992-01-01'
			and o_orderdate < date '1996-01-01'
		group by n_name
		order by revenue desc;
		"""
        ,
        """
		select n_name, sum(l_extendedprice * (1 - l_discount)) as revenue
		from customer, orders, lineitem, supplier, nation, region
		where c_custkey = o_custkey 
  			and l_orderkey = o_orderkey
			and l_suppkey = s_suppkey
			and c_nationkey = s_nationkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST'
			and o_orderdate >= date '1992-01-01'
			and o_orderdate < date '1996-01-01'
		group by n_name
		order by revenue desc;
		"""
	, 
	    """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
             """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'MIDDLE EAST'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'MIDDLE EAST' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,   
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
             """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
           select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AMERICA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'AMERICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,       
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
             """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'ASIA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'ASIA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,   
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
             """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'EUROPE'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'EUROPE' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
                """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'ECONOMY ANODIZED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
             """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED STEEL'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'PROMO BRUSHED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'MEDIUM BURNISHED COPPER'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'LARGE PLATED BRASS'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 10
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 14
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 30
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 3
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 16
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from L0FullView_MERGED_Q7
        where p_size = 22
        and p_type like 'SMALL BRUSHED TIN'
        and r_name = 'AFRICA'
        and ps_supplycost = (
            select min(ps_supplycost)
            from partsupp, supplier, nation, region
            where p_partkey = ps_partkey
            and s_suppkey = ps_suppkey
            and s_nationkey = n_nationkey
            and n_regionkey = r_regionkey
            and r_name = 'AFRICA' )
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """   
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'PERU')
					or (supp_nation = 'PERU' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'ALGERIA')
					or (supp_nation = 'ALGERIA' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'VIETNAM' and cust_nation = 'UNITED STATES')
					or (supp_nation = 'UNITED STATES' and cust_nation = 'VIETNAM')
				)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED STATES' and cust_nation = 'ARGENTINA')
				or (supp_nation = 'ARGENTINA' and cust_nation = 'UNITED STATES')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'CHINA')
					or (supp_nation = 'CHINA' and cust_nation = 'UNITED STATES')
				)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
			from L0FullView_Q234
			where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'IRAN')
					or (supp_nation = 'IRAN' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
			from L0FullView_Q234
			where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'UNITED KINGDOM')
					or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'BRAZIL')
					or (supp_nation = 'BRAZIL' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'INDIA')
					or (supp_nation = 'INDIA' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'MOZAMBIQUE')
					or (supp_nation = 'MOZAMBIQUE' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'RUSSIA')
					or (supp_nation = 'RUSSIA' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'ETHIOPIA')
					or (supp_nation = 'ETHIOPIA' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'FRANCE')
					or (supp_nation = 'FRANCE' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'MOROCCO')
					or (supp_nation = 'MOROCCO' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'EGYPT')
					or (supp_nation = 'EGYPT' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'KENYA')
					or (supp_nation = 'KENYA' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'JAPAN')
					or (supp_nation = 'JAPAN' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'INDONESIA')
					or (supp_nation = 'INDONESIA' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
					(supp_nation = 'UNITED STATES' and cust_nation = 'IRAQ')
					or (supp_nation = 'IRAQ' and cust_nation = 'UNITED STATES')
				)
			group by supp_nation, cust_nation, l_year
			order by supp_nation, cust_nation, l_year;
		"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED STATES' and cust_nation = 'CANADA')
				or (supp_nation = 'CANADA' and cust_nation = 'UNITED STATES')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED STATES' and cust_nation = 'JORDAN')
				or (supp_nation = 'JORDAN' and cust_nation = 'UNITED STATES')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED STATES' and cust_nation = 'ROMANIA')
				or (supp_nation = 'ROMANIA' and cust_nation = 'UNITED STATES')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED STATES' and cust_nation = 'GERMANY')
				or (supp_nation = 'GERMANY' and cust_nation = 'UNITED STATES')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED STATES' and cust_nation = 'SAUDI ARABIA')
				or (supp_nation = 'SAUDI ARABIA' and cust_nation = 'UNITED STATES')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'VIETNAM' and cust_nation = 'KENYA')
				or (supp_nation = 'KENYA' and cust_nation = 'VIETNAM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'ALGERIA')
				or (supp_nation = 'ALGERIA' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'UNITED STATES')
				or (supp_nation = 'UNITED STATES' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'ARGENTINA')
				or (supp_nation = 'ARGENTINA' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'IRAN')
				or (supp_nation = 'IRAN' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'BRAZIL')
				or (supp_nation = 'BRAZIL' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'INDIA')
				or (supp_nation = 'INDIA' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'MOZAMBIQUE')
				or (supp_nation = 'MOZAMBIQUE' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'RUSSIA')
				or (supp_nation = 'RUSSIA' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'ETHIOPIA')
				or (supp_nation = 'ETHIOPIA' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'FRANCE')
				or (supp_nation = 'FRANCE' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'MOROCCO')
				or (supp_nation = 'MOROCCO' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'EGYPT')
				or (supp_nation = 'EGYPT' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'PERU' and cust_nation = 'KENYA')
				or (supp_nation = 'KENYA' and cust_nation = 'PERU')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'JAPAN')
				or (supp_nation = 'JAPAN' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'INDONESIA')
				or (supp_nation = 'INDONESIA' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'IRAQ')
				or (supp_nation = 'IRAQ' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'CANADA')
				or (supp_nation = 'CANADA' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'JORDAN')
				or (supp_nation = 'JORDAN' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'ROMANIA')
				or (supp_nation = 'ROMANIA' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'GERMANY')
				or (supp_nation = 'GERMANY' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'SAUDI ARABIA')
				or (supp_nation = 'SAUDI ARABIA' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'PERU')
				or (supp_nation = 'PERU' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'ALGERIA')
				or (supp_nation = 'ALGERIA' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'UNITED STATES')
				or (supp_nation = 'UNITED STATES' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'VIETNAM' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'VIETNAM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'IRAN')
				or (supp_nation = 'IRAN' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'ARGENTINA')
				or (supp_nation = 'ARGENTINA' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'BRAZIL')
				or (supp_nation = 'BRAZIL' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'INDIA')
				or (supp_nation = 'INDIA' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'MOZAMBIQUE')
				or (supp_nation = 'MOZAMBIQUE' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'RUSSIA')
				or (supp_nation = 'RUSSIA' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'ETHIOPIA')
				or (supp_nation = 'ETHIOPIA' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'FRANCE')
				or (supp_nation = 'FRANCE' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'MOROCCO')
				or (supp_nation = 'MOROCCO' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'EGYPT')
				or (supp_nation = 'EGYPT' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'KENYA')
				or (supp_nation = 'KENYA' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'JAPAN')
				or (supp_nation = 'JAPAN' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'INDONESIA' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'INDONESIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAQ' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'IRAQ')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'CANADA' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'CANADA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'JORDAN' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'JORDAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ROMANIA' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'ROMANIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'GERMANY' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'GERMANY')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'SAUDI ARABIA' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'SAUDI ARABIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'VIETNAM')
				or (supp_nation = 'VIETNAM' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'PERU')
				or (supp_nation = 'PERU' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'UNITED STATES')
				or (supp_nation = 'UNITED STATES' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'ARGENTINA')
				or (supp_nation = 'ARGENTINA' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'ALGERIA')
				or (supp_nation = 'ALGERIA' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'BRAZIL')
				or (supp_nation = 'BRAZIL' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'INDIA')
				or (supp_nation = 'INDIA' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'MOZAMBIQUE')
				or (supp_nation = 'MOZAMBIQUE' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'RUSSIA')
				or (supp_nation = 'RUSSIA' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'ETHIOPIA')
				or (supp_nation = 'ETHIOPIA' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'FRANCE')
				or (supp_nation = 'FRANCE' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'MOROCCO')
				or (supp_nation = 'MOROCCO' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'EGYPT')
				or (supp_nation = 'EGYPT' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'KENYA')
				or (supp_nation = 'KENYA' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'JAPAN')
				or (supp_nation = 'JAPAN' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'INDONESIA')
				or (supp_nation = 'INDONESIA' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'IRAQ')
				or (supp_nation = 'IRAQ' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'CANADA')
				or (supp_nation = 'CANADA' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'JORDAN')
				or (supp_nation = 'JORDAN' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'ROMANIA')
				or (supp_nation = 'ROMANIA' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'GERMANY')
				or (supp_nation = 'GERMANY' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'SAUDI ARABIA' and cust_nation = 'IRAN')
				or (supp_nation = 'IRAN' and cust_nation = 'SAUDI ARABIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'VIETNAM' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'VIETNAM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'PERU' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'PERU')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED STATES' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'UNITED STATES')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ARGENTINA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'ARGENTINA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAN' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'IRAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ALGERIA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'ALGERIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'UNITED KINGDOM' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'UNITED KINGDOM')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'BRAZIL' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'BRAZIL')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'INDIA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'INDIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOZAMBIQUE' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'MOZAMBIQUE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'RUSSIA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'RUSSIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'KENYA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'KENYA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'JAPAN' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'JAPAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'INDONESIA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'INDONESIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'IRAQ' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'IRAQ')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'CANADA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'CANADA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'JORDAN' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'JORDAN')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ROMANIA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'ROMANIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'GERMANY' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'GERMANY')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'SAUDI ARABIA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'SAUDI ARABIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'VIETNAM')
				or (supp_nation = 'VIETNAM' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'PERU')
				or (supp_nation = 'PERU' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'UNITED STATES')
				or (supp_nation = 'UNITED STATES' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'ARGENTINA')
				or (supp_nation = 'ARGENTINA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'IRAN')
				or (supp_nation = 'IRAN' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'ALGERIA')
				or (supp_nation = 'ALGERIA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'BRAZIL')
				or (supp_nation = 'BRAZIL' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'INDIA')
				or (supp_nation = 'INDIA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'MOZAMBIQUE')
				or (supp_nation = 'MOZAMBIQUE' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'RUSSIA')
				or (supp_nation = 'RUSSIA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'ETHIOPIA')
				or (supp_nation = 'ETHIOPIA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'FRANCE')
				or (supp_nation = 'FRANCE' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'MOROCCO')
				or (supp_nation = 'MOROCCO' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'KENYA')
				or (supp_nation = 'KENYA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'JAPAN')
				or (supp_nation = 'JAPAN' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'INDONESIA')
				or (supp_nation = 'INDONESIA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'IRAQ')
				or (supp_nation = 'IRAQ' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'CANADA')
				or (supp_nation = 'CANADA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'JORDAN')
				or (supp_nation = 'JORDAN' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'ROMANIA')
				or (supp_nation = 'ROMANIA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'GERMANY')
				or (supp_nation = 'GERMANY' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'EGYPT' and cust_nation = 'SAUDI ARABIA')
				or (supp_nation = 'SAUDI ARABIA' and cust_nation = 'EGYPT')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'VIETNAM')
				or (supp_nation = 'VIETNAM' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'PERU')
				or (supp_nation = 'PERU' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'UNITED STATES')
				or (supp_nation = 'UNITED STATES' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'ARGENTINA')
				or (supp_nation = 'ARGENTINA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'IRAN')
				or (supp_nation = 'IRAN' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'ALGERIA')
				or (supp_nation = 'ALGERIA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'BRAZIL')
				or (supp_nation = 'BRAZIL' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'INDIA')
				or (supp_nation = 'INDIA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'MOZAMBIQUE')
				or (supp_nation = 'MOZAMBIQUE' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'RUSSIA')
				or (supp_nation = 'RUSSIA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'ETHIOPIA')
				or (supp_nation = 'ETHIOPIA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'FRANCE')
				or (supp_nation = 'FRANCE' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'EGYPT')
				or (supp_nation = 'EGYPT' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'KENYA')
				or (supp_nation = 'KENYA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'JAPAN')
				or (supp_nation = 'JAPAN' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'INDONESIA')
				or (supp_nation = 'INDONESIA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'IRAQ')
				or (supp_nation = 'IRAQ' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'CANADA')
				or (supp_nation = 'CANADA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'JORDAN')
				or (supp_nation = 'JORDAN' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'ROMANIA')
				or (supp_nation = 'ROMANIA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'GERMANY')
				or (supp_nation = 'GERMANY' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'MOROCCO' and cust_nation = 'SAUDI ARABIA')
				or (supp_nation = 'SAUDI ARABIA' and cust_nation = 'MOROCCO')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'VIETNAM')
				or (supp_nation = 'VIETNAM' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'PERU')
				or (supp_nation = 'PERU' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'UNITED STATES')
				or (supp_nation = 'UNITED STATES' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'ARGENTINA')
				or (supp_nation = 'ARGENTINA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'IRAN')
				or (supp_nation = 'IRAN' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'ALGERIA')
				or (supp_nation = 'ALGERIA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'BRAZIL')
				or (supp_nation = 'BRAZIL' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'INDIA')
				or (supp_nation = 'INDIA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'MOZAMBIQUE')
				or (supp_nation = 'MOZAMBIQUE' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'RUSSIA')
				or (supp_nation = 'RUSSIA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'ETHIOPIA')
				or (supp_nation = 'ETHIOPIA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'MOROCCO')
				or (supp_nation = 'MOROCCO' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'EGYPT')
				or (supp_nation = 'EGYPT' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'KENYA')
				or (supp_nation = 'KENYA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'JAPAN')
				or (supp_nation = 'JAPAN' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'INDONESIA')
				or (supp_nation = 'INDONESIA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'IRAQ')
				or (supp_nation = 'IRAQ' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'CANADA')
				or (supp_nation = 'CANADA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'JORDAN')
				or (supp_nation = 'JORDAN' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'ROMANIA')
				or (supp_nation = 'ROMANIA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'GERMANY')
				or (supp_nation = 'GERMANY' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'FRANCE' and cust_nation = 'SAUDI ARABIA')
				or (supp_nation = 'SAUDI ARABIA' and cust_nation = 'FRANCE')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'VIETNAM')
				or (supp_nation = 'VIETNAM' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'PERU')
				or (supp_nation = 'PERU' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'ARGENTINA')
				or (supp_nation = 'ARGENTINA' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'IRAN')
				or (supp_nation = 'IRAN' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'ALGERIA')
				or (supp_nation = 'ALGERIA' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'UNITED KINGDOM')
				or (supp_nation = 'UNITED KINGDOM' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'BRAZIL')
				or (supp_nation = 'BRAZIL' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'INDIA')
				or (supp_nation = 'INDIA' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'MOZAMBIQUE')
				or (supp_nation = 'MOZAMBIQUE' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'RUSSIA')
				or (supp_nation = 'RUSSIA' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'FRANCE')
				or (supp_nation = 'FRANCE' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'MOROCCO')
				or (supp_nation = 'MOROCCO' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'EGYPT')
				or (supp_nation = 'EGYPT' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'CHINA')
				or (supp_nation = 'CHINA' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'KENYA')
				or (supp_nation = 'KENYA' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'JAPAN')
				or (supp_nation = 'JAPAN' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'INDONESIA')
				or (supp_nation = 'INDONESIA' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
	"""
		select supp_nation, cust_nation, l_year, sum(volume) as revenue
		from L0FullView_Q234
		where (
				(supp_nation = 'ETHIOPIA' and cust_nation = 'IRAQ')
				or (supp_nation = 'IRAQ' and cust_nation = 'ETHIOPIA')
			)
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SUADI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SUADI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SUADI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SUADI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SUADI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SUADI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS' ) as all_nations
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
			where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' 
		group by o_year 
		order by o_year;
	"""  
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'ECONOMY ANODIZED STEEL'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED STEEL' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'PROMO BRUSHED BRASS'
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'MEDIUM BURNISHED COPPER' 
		group by o_year 
		order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'LARGE PLATED BRASS'
		group by o_year 
		order by o_year;
		
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from L0FullView_MERGED_Q445
		where p_type = 'SMALL BRUSHED TIN' 
		group by o_year 
		order by o_year;
	"""
    ,
    """
	select nation, o_year, sum(amount) as sum_profit
	from(
    select n_name as nation, extract(year from o_orderdate) as o_year,
	l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
	from part, supplier, lineitem, partsupp, orders, nation
	where s_suppkey = l_suppkey
		and ps_suppkey = l_suppkey
		and ps_partkey = l_partkey
		and p_partkey = l_partkey
		and o_orderkey = l_orderkey
		and s_nationkey = n_nationkey
		and p_name like '%black%') as profit
	group by nation, o_year
	order by nation, o_year desc;
	"""
	,
	"""
	select nation, o_year, sum(amount) as sum_profit
	from(
    select n_name as nation, extract(year from o_orderdate) as o_year,
	l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
	from part, supplier, lineitem, partsupp, orders, nation
	where s_suppkey = l_suppkey
		and ps_suppkey = l_suppkey
		and ps_partkey = l_partkey
		and p_partkey = l_partkey
		and o_orderkey = l_orderkey
		and s_nationkey = n_nationkey
		and p_name like '%white%') as profit
	group by nation, o_year
	order by nation, o_year desc;
	"""
	,
	"""
	select nation, o_year, sum(amount) as sum_profit
	from(
    select n_name as nation, extract(year from o_orderdate) as o_year,
	l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
	from part, supplier, lineitem, partsupp, orders, nation
	where s_suppkey = l_suppkey
		and ps_suppkey = l_suppkey
		and ps_partkey = l_partkey
		and p_partkey = l_partkey
		and o_orderkey = l_orderkey
		and s_nationkey = n_nationkey
		and p_name like '%red%') as profit
	group by nation, o_year
	order by nation, o_year desc;
	"""
	,
	"""
	select nation, o_year, sum(amount) as sum_profit
	from(
    select n_name as nation, extract(year from o_orderdate) as o_year,
	l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
	from part, supplier, lineitem, partsupp, orders, nation
	where s_suppkey = l_suppkey
		and ps_suppkey = l_suppkey
		and ps_partkey = l_partkey
		and p_partkey = l_partkey
		and o_orderkey = l_orderkey
		and s_nationkey = n_nationkey
		and p_name like '%blue%') as profit
	group by nation, o_year
	order by nation, o_year desc;
	"""
	,
	"""
	select nation, o_year, sum(amount) as sum_profit
	from(
    select n_name as nation, extract(year from o_orderdate) as o_year,
	l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
	from part, supplier, lineitem, partsupp, orders, nation
	where s_suppkey = l_suppkey
		and ps_suppkey = l_suppkey
		and ps_partkey = l_partkey
		and p_partkey = l_partkey
		and o_orderkey = l_orderkey
		and s_nationkey = n_nationkey
		and p_name like '%pink%') as profit
	group by nation, o_year
	order by nation, o_year desc;
	"""
	,
	"""
	select nation, o_year, sum(amount) as sum_profit
	from(
    select n_name as nation, extract(year from o_orderdate) as o_year,
	l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
	from part, supplier, lineitem, partsupp, orders, nation
	where s_suppkey = l_suppkey
		and ps_suppkey = l_suppkey
		and ps_partkey = l_partkey
		and p_partkey = l_partkey
		and o_orderkey = l_orderkey
		and s_nationkey = n_nationkey
		and p_name like '%yellow%') as profit
	group by nation, o_year
	order by nation, o_year desc;
	"""
	,
	"""
	select nation, o_year, sum(amount) as sum_profit
	from(
    select n_name as nation, extract(year from o_orderdate) as o_year,
	l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
	from part, supplier, lineitem, partsupp, orders, nation
	where s_suppkey = l_suppkey
		and ps_suppkey = l_suppkey
		and ps_partkey = l_partkey
		and p_partkey = l_partkey
		and o_orderkey = l_orderkey
		and s_nationkey = n_nationkey
		and p_name like '%green%') as profit
	group by nation, o_year
	order by nation, o_year desc;
	"""
	,
	"""
	select nation, o_year, sum(amount) as sum_profit
	from(
    select n_name as nation, extract(year from o_orderdate) as o_year,
	l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
	from part, supplier, lineitem, partsupp, orders, nation
	where s_suppkey = l_suppkey
		and ps_suppkey = l_suppkey
		and ps_partkey = l_partkey
		and p_partkey = l_partkey
		and o_orderkey = l_orderkey
		and s_nationkey = n_nationkey
		and p_name like '%purple%') as profit
	group by nation, o_year
	order by nation, o_year desc;
	"""
	,
	"""
	select nation, o_year, sum(amount) as sum_profit
	from(
    select n_name as nation, extract(year from o_orderdate) as o_year,
	l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
	from part, supplier, lineitem, partsupp, orders, nation
	where s_suppkey = l_suppkey
		and ps_suppkey = l_suppkey
		and ps_partkey = l_partkey
		and p_partkey = l_partkey
		and o_orderkey = l_orderkey
		and s_nationkey = n_nationkey
		and p_name like '%grey%') as profit
	group by nation, o_year
	order by nation, o_year desc;
	"""
	,
	"""
	select nation, o_year, sum(amount) as sum_profit
	from(
    select n_name as nation, extract(year from o_orderdate) as o_year,
	l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
	from part, supplier, lineitem, partsupp, orders, nation
	where s_suppkey = l_suppkey
		and ps_suppkey = l_suppkey
		and ps_partkey = l_partkey
		and p_partkey = l_partkey
		and o_orderkey = l_orderkey
		and s_nationkey = n_nationkey
		and p_name like '%brown%') as profit
	group by nation, o_year
	order by nation, o_year desc;
	"""
]