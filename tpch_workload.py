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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
	    and r_name = 'EUROPE'
	    and ps_supplycost = (
		    select min(ps_supplycost)
		    from partsupp, supplier, nation, region
		    where p_partkey = ps_partkey
			and s_suppkey = ps_suppkey
			and s_nationkey = n_nationkey
			and n_regionkey = r_regionkey
			and r_name = 'EUROPE')
        order by s_acctbal desc, n_name, s_name, p_partkey;
            """
            ,
            """
        select s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'ECONOMY ANODIZED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED STEEL'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'PROMO BRUSHED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'MEDIUM BURNISHED COPPER'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'LARGE PLATED BRASS'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 10
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 14
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 30
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 3
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 16
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
        from part, supplier, partsupp, nation, region
        where p_partkey = ps_partkey
	    and s_suppkey = ps_suppkey
	    and p_size = 22
	    and p_type like 'SMALL BRUSHED TIN'
	    and s_nationkey = n_nationkey
	    and n_regionkey = r_regionkey
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'PERU')
				or (n1.n_name = 'PERU' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'ALGERIA')
				or (n1.n_name = 'ALGERIA' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'VIETNAM' and n2.n_name = 'UNITED STATES')
				or (n1.n_name = 'UNITED STATES' and n2.n_name = 'VIETNAM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'ARGENTINA')
				or (n1.n_name = 'ARGENTINA' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'CHINA')
				or (n1.n_name = 'CHINA' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'IRAN')
				or (n1.n_name = 'IRAN' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'UNITED KINGDOM')
				or (n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'BRAZIL')
				or (n1.n_name = 'BRAZIL' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'INDIA')
				or (n1.n_name = 'INDIA' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'MOZAMBIQUE')
				or (n1.n_name = 'MOZAMBIQUE' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'RUSSIA')
				or (n1.n_name = 'RUSSIA' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'MOROCCO')
				or (n1.n_name = 'MOROCCO' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'EGYPT')
				or (n1.n_name = 'EGYPT' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'KENYA')
				or (n1.n_name = 'KENYA' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'JAPAN')
				or (n1.n_name = 'JAPAN' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'INDONESIA')
				or (n1.n_name = 'INDONESIA' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'IRAQ')
				or (n1.n_name = 'IRAQ' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'CANADA')
				or (n1.n_name = 'CANADA' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'JORDAN')
				or (n1.n_name = 'JORDAN' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'ROMANIA')
				or (n1.n_name = 'ROMANIA' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'GERMANY')
				or (n1.n_name = 'GERMANY' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED STATES' and n2.n_name = 'SAUDI ARABIA')
				or (n1.n_name = 'SAUDI ARABIA' and n2.n_name = 'UNITED STATES')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'VIETNAM' and n2.n_name = 'KENYA')
				or (n1.n_name = 'KENYA' and n2.n_name = 'VIETNAM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'ALGERIA')
				or (n1.n_name = 'ALGERIA' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'UNITED STATES')
				or (n1.n_name = 'UNITED STATES' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'ARGENTINA')
				or (n1.n_name = 'ARGENTINA' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'KENYA' and n2.n_name = 'CHINA')
				or (n1.n_name = 'CHINA' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'IRAN')
				or (n1.n_name = 'IRAN' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'UNITED KINGDOM')
				or (n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'KENYA' and n2.n_name = 'BRAZIL')
				or (n1.n_name = 'BRAZIL' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'INDIA')
				or (n1.n_name = 'INDIA' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'MOZAMBIQUE')
				or (n1.n_name = 'MOZAMBIQUE' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'RUSSIA')
				or (n1.n_name = 'RUSSIA' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'KENYA' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'MOROCCO')
				or (n1.n_name = 'MOROCCO' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'EGYPT')
				or (n1.n_name = 'EGYPT' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'PERU' and n2.n_name = 'KENYA')
				or (n1.n_name = 'KENYA' and n2.n_name = 'PERU')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'KENYA' and n2.n_name = 'JAPAN')
				or (n1.n_name = 'JAPAN' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'INDONESIA')
				or (n1.n_name = 'INDONESIA' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'IRAQ')
				or (n1.n_name = 'IRAQ' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'CANADA')
				or (n1.n_name = 'CANADA' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'KENYA' and n2.n_name = 'JORDAN')
				or (n1.n_name = 'JORDAN' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'ROMANIA')
				or (n1.n_name = 'ROMANIA' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'GERMANY')
				or (n1.n_name = 'GERMANY' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'KENYA' and n2.n_name = 'SAUDI ARABIA')
				or (n1.n_name = 'SAUDI ARABIA' and n2.n_name = 'KENYA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'PERU')
				or (n1.n_name = 'PERU' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'ALGERIA')
				or (n1.n_name = 'ALGERIA' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'UNITED STATES')
				or (n1.n_name = 'UNITED STATES' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'VIETNAM' and n2.n_name = 'UNITED KINGDOM')
				or (n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'VIETNAM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'CHINA')
				or (n1.n_name = 'CHINA' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'IRAN')
				or (n1.n_name = 'IRAN' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ARGENTINA' and n2.n_name = 'UNITED KINGDOM')
				or (n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'ARGENTINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'BRAZIL')
				or (n1.n_name = 'BRAZIL' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'INDIA')
				or (n1.n_name = 'INDIA' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'MOZAMBIQUE')
				or (n1.n_name = 'MOZAMBIQUE' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'RUSSIA')
				or (n1.n_name = 'RUSSIA' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'MOROCCO')
				or (n1.n_name = 'MOROCCO' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'EGYPT')
				or (n1.n_name = 'EGYPT' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'KENYA')
				or (n1.n_name = 'KENYA' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'JAPAN')
				or (n1.n_name = 'JAPAN' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'INDONESIA')
				or (n1.n_name = 'INDONESIA' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'IRAQ')
				or (n1.n_name = 'IRAQ' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'CANADA')
				or (n1.n_name = 'CANADA' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'JORDAN')
				or (n1.n_name = 'JORDAN' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'ROMANIA')
				or (n1.n_name = 'ROMANIA' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'GERMANY')
				or (n1.n_name = 'GERMANY' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'SAUDI ARABIA')
				or (n1.n_name = 'SAUDI ARABIA' and n2.n_name = 'UNITED KINGDOM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'VIETNAM' and n2.n_name = 'IRAN')
				or (n1.n_name = 'IRAN' and n2.n_name = 'VIETNAM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'PERU' and n2.n_name = 'IRAN')
				or (n1.n_name = 'IRAN' and n2.n_name = 'PERU')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'UNITED STATES')
				or (n1.n_name = 'UNITED STATES' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'ARGENTINA')
				or (n1.n_name = 'ARGENTINA' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'IRAN' and n2.n_name = 'CHINA')
				or (n1.n_name = 'CHINA' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ALGERIA' and n2.n_name = 'IRAN')
				or (n1.n_name = 'IRAN' and n2.n_name = 'ALGERIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'UNITED KINGDOM')
				or (n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'IRAN' and n2.n_name = 'BRAZIL')
				or (n1.n_name = 'BRAZIL' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'INDIA')
				or (n1.n_name = 'INDIA' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'MOZAMBIQUE')
				or (n1.n_name = 'MOZAMBIQUE' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'RUSSIA')
				or (n1.n_name = 'RUSSIA' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'IRAN' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'MOROCCO')
				or (n1.n_name = 'MOROCCO' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'EGYPT')
				or (n1.n_name = 'EGYPT' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'IRAN' and n2.n_name = 'KENYA')
				or (n1.n_name = 'KENYA' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'IRAN' and n2.n_name = 'JAPAN')
				or (n1.n_name = 'JAPAN' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'INDONESIA')
				or (n1.n_name = 'INDONESIA' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'IRAQ')
				or (n1.n_name = 'IRAQ' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'CANADA')
				or (n1.n_name = 'CANADA' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'IRAN' and n2.n_name = 'JORDAN')
				or (n1.n_name = 'JORDAN' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'ROMANIA')
				or (n1.n_name = 'ROMANIA' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'GERMANY')
				or (n1.n_name = 'GERMANY' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'IRAN' and n2.n_name = 'SAUDI ARABIA')
				or (n1.n_name = 'SAUDI ARABIA' and n2.n_name = 'IRAN')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'VIETNAM' and n2.n_name = 'CHINA')
				or (n1.n_name = 'CHINA' and n2.n_name = 'VIETNAM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'PERU' and n2.n_name = 'CHINA')
				or (n1.n_name = 'CHINA' and n2.n_name = 'PERU')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'UNITED STATES')
				or (n1.n_name = 'UNITED STATES' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'ARGENTINA')
				or (n1.n_name = 'ARGENTINA' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'CHINA' and n2.n_name = 'IRAN')
				or (n1.n_name = 'IRAN' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ALGERIA' and n2.n_name = 'CHINA')
				or (n1.n_name = 'CHINA' and n2.n_name = 'ALGERIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'UNITED KINGDOM')
				or (n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'CHINA' and n2.n_name = 'BRAZIL')
				or (n1.n_name = 'BRAZIL' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'INDIA')
				or (n1.n_name = 'INDIA' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'MOZAMBIQUE')
				or (n1.n_name = 'MOZAMBIQUE' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'RUSSIA')
				or (n1.n_name = 'RUSSIA' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'CHINA' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'MOROCCO')
				or (n1.n_name = 'MOROCCO' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'EGYPT')
				or (n1.n_name = 'EGYPT' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'CHINA' and n2.n_name = 'KENYA')
				or (n1.n_name = 'KENYA' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'CHINA' and n2.n_name = 'JAPAN')
				or (n1.n_name = 'JAPAN' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'INDONESIA')
				or (n1.n_name = 'INDONESIA' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'IRAQ')
				or (n1.n_name = 'IRAQ' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'CANADA')
				or (n1.n_name = 'CANADA' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'CHINA' and n2.n_name = 'JORDAN')
				or (n1.n_name = 'JORDAN' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'ROMANIA')
				or (n1.n_name = 'ROMANIA' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'GERMANY')
				or (n1.n_name = 'GERMANY' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'SAUDI ARABIA')
				or (n1.n_name = 'SAUDI ARABIA' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'VIETNAM' and n2.n_name = 'EGYPT')
				or (n1.n_name = 'EGYPT' and n2.n_name = 'VIETNAM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'PERU' and n2.n_name = 'EGYPT')
				or (n1.n_name = 'EGYPT' and n2.n_name = 'PERU')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'UNITED STATES')
				or (n1.n_name = 'UNITED STATES' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'ARGENTINA')
				or (n1.n_name = 'ARGENTINA' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'IRAN')
				or (n1.n_name = 'IRAN' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ALGERIA' and n2.n_name = 'EGYPT')
				or (n1.n_name = 'EGYPT' and n2.n_name = 'ALGERIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'UNITED KINGDOM')
				or (n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'BRAZIL')
				or (n1.n_name = 'BRAZIL' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'INDIA')
				or (n1.n_name = 'INDIA' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'MOZAMBIQUE')
				or (n1.n_name = 'MOZAMBIQUE' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'RUSSIA')
				or (n1.n_name = 'RUSSIA' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'MOROCCO')
				or (n1.n_name = 'MOROCCO' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'EGYPT')
				or (n1.n_name = 'EGYPT' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'KENYA')
				or (n1.n_name = 'KENYA' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'JAPAN')
				or (n1.n_name = 'JAPAN' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'INDONESIA')
				or (n1.n_name = 'INDONESIA' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'IRAQ')
				or (n1.n_name = 'IRAQ' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'CANADA')
				or (n1.n_name = 'CANADA' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'JORDAN')
				or (n1.n_name = 'JORDAN' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'ROMANIA')
				or (n1.n_name = 'ROMANIA' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'GERMANY')
				or (n1.n_name = 'GERMANY' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'SAUDI ARABIA')
				or (n1.n_name = 'SAUDI ARABIA' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	,
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
				(n1.n_name = 'VIETNAM' and n2.n_name = 'MOROCCO')
				or (n1.n_name = 'MOROCCO' and n2.n_name = 'VIETNAM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'PERU' and n2.n_name = 'MOROCCO')
				or (n1.n_name = 'MOROCCO' and n2.n_name = 'PERU')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'UNITED STATES')
				or (n1.n_name = 'UNITED STATES' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'ARGENTINA')
				or (n1.n_name = 'ARGENTINA' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'IRAN')
				or (n1.n_name = 'IRAN' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ALGERIA' and n2.n_name = 'MOROCCO')
				or (n1.n_name = 'MOROCCO' and n2.n_name = 'ALGERIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'UNITED KINGDOM')
				or (n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'BRAZIL')
				or (n1.n_name = 'BRAZIL' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'INDIA')
				or (n1.n_name = 'INDIA' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'MOZAMBIQUE')
				or (n1.n_name = 'MOZAMBIQUE' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'RUSSIA')
				or (n1.n_name = 'RUSSIA' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'MOROCCO')
				or (n1.n_name = 'MOROCCO' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'MOROCCO')
				or (n1.n_name = 'MOROCCO' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'KENYA')
				or (n1.n_name = 'KENYA' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'JAPAN')
				or (n1.n_name = 'JAPAN' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'INDONESIA')
				or (n1.n_name = 'INDONESIA' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'IRAQ')
				or (n1.n_name = 'IRAQ' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'CANADA')
				or (n1.n_name = 'CANADA' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'JORDAN')
				or (n1.n_name = 'JORDAN' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'ROMANIA')
				or (n1.n_name = 'ROMANIA' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'GERMANY')
				or (n1.n_name = 'GERMANY' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'SAUDI ARABIA')
				or (n1.n_name = 'SAUDI ARABIA' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'VIETNAM' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'VIETNAM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'PERU' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'PERU')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'UNITED STATES')
				or (n1.n_name = 'UNITED STATES' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'ARGENTINA')
				or (n1.n_name = 'ARGENTINA' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'IRAN')
				or (n1.n_name = 'IRAN' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ALGERIA' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'ALGERIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'UNITED KINGDOM')
				or (n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'BRAZIL')
				or (n1.n_name = 'BRAZIL' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'INDIA')
				or (n1.n_name = 'INDIA' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'MOZAMBIQUE')
				or (n1.n_name = 'MOZAMBIQUE' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'RUSSIA')
				or (n1.n_name = 'RUSSIA' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'FRANCE')
				or (n1.n_name = 'FRANCE' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'KENYA')
				or (n1.n_name = 'KENYA' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'JAPAN')
				or (n1.n_name = 'JAPAN' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'INDONESIA')
				or (n1.n_name = 'INDONESIA' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'IRAQ')
				or (n1.n_name = 'IRAQ' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'CANADA')
				or (n1.n_name = 'CANADA' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'JORDAN')
				or (n1.n_name = 'JORDAN' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'ROMANIA')
				or (n1.n_name = 'ROMANIA' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'GERMANY')
				or (n1.n_name = 'GERMANY' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'SAUDI ARABIA')
				or (n1.n_name = 'SAUDI ARABIA' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'VIETNAM' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'VIETNAM')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'PERU' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'PERU')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ETHIOPIA' and n2.n_name = 'UNITED STATES')
				or (n1.n_name = 'UNITED STATES' and n2.n_name = 'ETHIOPIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ETHIOPIA' and n2.n_name = 'ARGENTINA')
				or (n1.n_name = 'ARGENTINA' and n2.n_name = 'ETHIOPIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'ETHIOPIA' and n2.n_name = 'IRAN')
				or (n1.n_name = 'IRAN' and n2.n_name = 'ETHIOPIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ALGERIA' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'ALGERIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ETHIOPIA' and n2.n_name = 'UNITED KINGDOM')
				or (n1.n_name = 'UNITED KINGDOM' and n2.n_name = 'ETHIOPIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'ETHIOPIA' and n2.n_name = 'BRAZIL')
				or (n1.n_name = 'BRAZIL' and n2.n_name = 'ETHIOPIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ETHIOPIA' and n2.n_name = 'INDIA')
				or (n1.n_name = 'INDIA' and n2.n_name = 'ETHIOPIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ETHIOPIA' and n2.n_name = 'MOZAMBIQUE')
				or (n1.n_name = 'MOZAMBIQUE' and n2.n_name = 'ETHIOPIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ETHIOPIA' and n2.n_name = 'RUSSIA')
				or (n1.n_name = 'RUSSIA' and n2.n_name = 'ETHIOPIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'FRANCE' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'FRANCE')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'MOROCCO' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'MOROCCO')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'EGYPT' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'EGYPT')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'CHINA' and n2.n_name = 'ETHIOPIA')
				or (n1.n_name = 'ETHIOPIA' and n2.n_name = 'CHINA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
				(n1.n_name = 'ETHIOPIA' and n2.n_name = 'KENYA')
				or (n1.n_name = 'KENYA' and n2.n_name = 'ETHIOPIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	, 
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
	"""
 	,
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
				(n1.n_name = 'ETHIOPIA' and n2.n_name = 'INDONESIA')
				or (n1.n_name = 'INDONESIA' and n2.n_name = 'ETHIOPIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
 	,
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
				(n1.n_name = 'ETHIOPIA' and n2.n_name = 'IRAQ')
				or (n1.n_name = 'IRAQ' and n2.n_name = 'ETHIOPIA')
			)
			and l_shipdate between date '1992-01-01' and date '1992-12-31'
		) as shipping
		group by supp_nation, cust_nation, l_year
		order by supp_nation, cust_nation, l_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ETHIOPIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SAUDI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SAUDI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SAUDI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SAUDI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SAUDI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'SAUDI ARABIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'RUSSIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'PERU' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'GERMANY' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDONESIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOZAMBIQUE' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'KENYA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'IRAQ' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'JORDAN' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'ROMANIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'INDIA' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'VIETNAM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'EGYPT' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'MOROCCO' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED STATES' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'ECONOMY ANODIZED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED STEEL' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'PROMO BRUSHED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'MEDIUM BURNISHED COPPER' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'LARGE PLATED BRASS' ) as all_nations
			group by o_year 
			order by o_year;
	"""
	,
	"""
		select o_year, sum(case when nation = 'UNITED KINGDOM' then volume 
  						else 0 end) / sum(volume) as mkt_share
		from (
			select extract(year from o_orderdate) as o_year,
				l_extendedprice * (1 - l_discount) as volume,
				n2.n_name as nation
			from part, supplier, lineitem, orders, customer, nation n1,
				nation n2, region
			where p_partkey = l_partkey
				and s_suppkey = l_suppkey
				and l_orderkey = o_orderkey
				and o_custkey = c_custkey
				and c_nationkey = n1.n_nationkey
				and n1.n_regionkey = r_regionkey
				and s_nationkey = n2.n_nationkey
				and o_orderdate between date '1992-01-01' and date '1992-12-31'
				and p_type = 'SMALL BRUSHED TIN' ) as all_nations
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