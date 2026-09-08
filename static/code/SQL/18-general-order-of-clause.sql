

-- General order of clauses in SQL:

--  SELECT columns
--  FROM table
--  WHERE conditions
--  GROUP BY columns
--  HAVING conditions
--  ORDER BY columns
--  LIMIT number_of_rows


-- Execution Order (how SQL actually processes it):
--
-- 1. FROM     -> Fetch rows from the target table
-- 2. WHERE    -> Filter individual rows BEFORE grouping
-- 3. GROUP BY -> Bucket remaining rows into unique groups
-- 4. HAVING   -> Filter entire groups AFTER aggregation
-- 5. SELECT   -> Calculate aggregate functions (COUNT, SUM, AVG) per group
-- 6. ORDER BY -> Sort the final output dataset
