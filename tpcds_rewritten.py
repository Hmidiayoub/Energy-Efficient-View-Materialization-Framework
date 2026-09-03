from tpcds_workload import workload_1 as _source_workload


workload_1 = list(_source_workload)

workload_1[0] = """
SELECT *
FROM "L0-FULLVIEW_Q0"
ORDER BY 1;
"""

workload_1[8] = """
SELECT *
FROM "L0-FULLVIEW_Q8"
ORDER BY 1, 2, 3;
"""

workload_1[16] = """
SELECT *
FROM "L0-FULLVIEW_Q16"
ORDER BY 5 DESC, 2, 1, 3, 4;
"""

workload_1[23] = """
SELECT *
FROM "L0-FULLVIEW_Q23"
ORDER BY 1, 2, 3, 4;
"""

workload_1[24] = """
SELECT *
FROM "L0-FULLVIEW_Q24"
ORDER BY 1, 2, 3, 4;
"""

workload_1[25] = """
SELECT *
FROM "L0-FULLVIEW_Q25"
ORDER BY 1, 2, 3, 4;
"""

workload_1[31] = """
SELECT *
FROM "L0-FULLVIEW_Q31"
ORDER BY 1, 2, 3, 4;
"""

workload_1[121] = """
SELECT *
FROM "L0-FULLVIEW_Q121"
ORDER BY 1, 4 DESC, 2;
"""