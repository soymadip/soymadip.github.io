-- ------------------ LIMIT Clause -----------------
-- 
-- Used to specify the number of records/rows to return from a query.

-- Eg: list students, limit to 5 rows
SELECT * FROM student LIMIT 5;

-- We can put conditions in limit clause too.

-- Eg: list 4 students whose marks > 56
SELECT * FROM student WHERE marks > 56 LIMIT 5;


-- --------------------- Setting Offset --------------------

-- We use OFFSET option to set an offset.
-- generally this is used with order by clause to skip rows.

-- List second and third highest marks of students
SELECT * FROM student ORDER BY grade DESC LIMIT 2 OFFSET 1; -- skips 1st result

