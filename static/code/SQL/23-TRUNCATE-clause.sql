-- ------------------------- TRUNCATE Clause -------------------------

-- The TRUNCATE TABLE statement is used to delete all rows from a table.
-- It is faster than the DELETE statement because it does not generate individual row delete statements.

-- Syntax:
TRUNCATE TABLE table_name;

-- Turncate table sales
TRUNCATE TABLE sales;

SELECT * FROM sales;