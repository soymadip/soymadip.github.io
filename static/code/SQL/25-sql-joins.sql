
-- ------------------------- Types of Joins -------------------------

-- Creating two tables.
DROP DATABASE IF EXISTS join_ex;
CREATE DATABASE join_ex;
USE join_ex;


CREATE TABLE students(
    student_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE courses(
    student_id INT PRIMARY KEY,
    course VARCHAR(100)
);


INSERT INTO students(student_id, name) VALUES
    (101, 'amit'),
    (102, 'rohit'),
    (103, 'sita'),
    (104, 'john tucker');


INSERT INTO courses(student_id, course) VALUES
    (102, 'english'),
    (105, 'science'),
    (103, 'math'),
    (107, 'computer science');

SELECT * FROM courses;
SELECT * FROM students;


-- ================== SQL Joins ==================

-- Join is used to combine rows from two or more tables based on a related column between them.

-- Foreign Key is not required to perform a join, but it is a good practice to have one.

-- For example:
-- We have employee table with id, name.
-- We have salary table with id,salary.
-- We can join these two tables to get id, name, salary of employees. The join happens on the id column (the common of both tables).


-- ------------------------- Types of Joins -------------------------


-- --------------- Inner Join ---------------

-- Returns records that have matching values in both tables.
-- 
-- As we get common data, A/B table directions doesn't matter.

-- Syntax:
SELECT columns FROM tableA
INNER JOIN tableB
ON tableA.column_name = tableB.column_name;

-- Ex: Get name of students and their courses (common in both tables).
SELECT * FROM students AS st
INNER JOIN courses AS crs
ON st.student_id = crs.student_id;

-- Only students which aare in both tables are printed.


-- --------------- Left Join ---------------

-- Returns all records from the LEFT table, and the matched records from the right table.
-- If there is no match, the result is NULL on the right side.

-- Syntax:
SELECT columns
FROM tableA
LEFT JOIN tableB
ON tableA.column_name = tableB.column_name;

-- Ex:
SELECT *
FROM students
LEFT JOIN courses
ON students.student_id = courses.student_id;

-- right student_id & course column will be NULL for students who are not in the course table.
 

-- --------------- Right Join ---------------

-- Returns all records from the RIGHT table, and the matched records from the left table.
-- If there is no match, the result is NULL on the left side.

-- Syntax:
SELECT columns
FROM tableA  -- LEFT TABLE. this table gets all rows
RIGHT JOIN tableB  -- RIGHT TABLE, only mutual rows with left table are printed
ON tableA.column_name = tableB.column_name;

-- Ex:
SELECT *
FROM students
RIGHT JOIN courses
ON students.student_id = courses.student_id;

-- left student_id & name column will be NULL for students who are not in the student table.


-- --------------- FULL Join ---------------

-- Returns all records when there is a match in either left or right table.
-- MySQL doesn't have native FULL JOIN.
-- So we take left join & right join and UNION them.

     SELECT *
     FROM students 
     LEFT JOIN courses  
     ON students.student_id = courses.student_id
UNION         -- gives unique values
     SELECT *
     FROM students 
     RIGHT JOIN courses 
     ON students.student_id = courses.student_id;


-- ---------------------- LEFT Exclusive JOIN -----------------------------

-- When we want to get records that exist ONLY in the left table and have no matching record in the right table.

-- Ex:
SELECT * 
FROM students 
LEFT JOIN courses 
ON students.student_id = courses.student_id 
WHERE courses.student_id IS NULL;

-- ---------------------- RIGHT Exclusive JOIN -----------------------------

-- When we want to get records that exist ONLY in the right table and have no matching record in the left table.

-- Ex:
SELECT * 
FROM students 
RIGHT JOIN courses 
ON students.student_id = courses.student_id 
WHERE students.student_id IS NULL;


-- ---------------------- FULL Exclusive JOIN -----------------------------

-- When we want to get records that are unique to EITHER the left table OR the right table, excluding any records they have in common.

-- Ex (Standard SQL):
SELECT * 
FROM students
FULL OUTER JOIN courses 
ON students.student_id = courses.student_id 
WHERE students.student_id IS NULL OR courses.student_id IS NULL;

-- Ex (MariaDB / MySQL Workaround):
-- Note: MySQL and MariaDB do not support `FULL OUTER JOIN` directly.
-- You achieve it by combining a LEFT Exclusive JOIN and a RIGHT Exclusive JOIN using UNION:
    SELECT * FROM students AS stu
    LEFT JOIN courses AS crs
    ON stu.student_id = crs.student_id
    WHERE crs.student_id IS NULL
UNION
    SELECT * FROM students AS stu
    RIGHT JOIN courses AS crs
    ON stu.student_id = crs.student_id 
    WHERE stu.student_id IS NULL;


-- ------------------- Self Join ----------------------
-- A regular join where a table is joined with itself.
-- 
-- Used when:
--   1. Comparing rows within the same table.
--   2. Querying hierarchical data in one table (e.g., Employee -> Manager).
-- 
-- Note: Table aliases (AS table1, AS table2) are REQUIRED so SQL can treat them as two distinct instances.

-- Ex:
CREATE TABLE  employee(
    id int PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    manager_id int 
) AUTO_INCREMENT=101;

INSERT INTO employee(id,name, manager_id) VALUES
    (101, 'adam', 103),
    (102, 'bob', 104),
    (103, 'casey', null),
    (104, 'donald', 103);


-- Find out which employee has which manager.
SELECT emp.name, mgr.name 
FROM employees AS emp
LEFT JOIN employees AS mgr
ON emp.manager_id = mgr.id;

