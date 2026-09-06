-- ---------------------- HAVING Clause ------------------------

-- Similar to WHERE caluse, aplies some conditions to rows.
-- But when we want to apply any condition AFTER GROUPING


SELECT city, COUNT(rollno) FROM student GROUP BY city HAVING MAX(marks) > 90;
