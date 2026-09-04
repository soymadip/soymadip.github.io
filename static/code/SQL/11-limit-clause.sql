-- ------------------ LIMIT Clause -----------------
-- 
-- Used to specify the number of records/rows to return from a query.

-- Eg: list students, limit to 5 rows
SELECT * FROM student LIMIT 5;

-- We can put conditions in limit clause too.

-- Eg: list 4 students whose marks > 56
SELECT * FROM student WHERE marks > 56 LIMIT 5;

