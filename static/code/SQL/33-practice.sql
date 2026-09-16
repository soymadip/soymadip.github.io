-- ===================== POST-27 SQL PRACTICE =====================
-- Covered material:
--   scalar functions, UNION / UNION ALL, subqueries, and views.
--
-- Build the setup first, then solve the sections in any order.

DROP DATABASE IF EXISTS post_27_practice;
CREATE DATABASE post_27_practice;
USE post_27_practice;

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    department_id INT,
    marks DECIMAL(5, 2) NOT NULL CHECK (marks BETWEEN 0 AND 100),
    city VARCHAR(50) NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE alumni (
    alumni_id INT PRIMARY KEY,
    person_name VARCHAR(100) NOT NULL,
    department_name VARCHAR(50) NOT NULL,
    graduation_year INT NOT NULL
);

CREATE TABLE scholarship_applications (
    application_id INT PRIMARY KEY,
    student_id INT NOT NULL,
    scholarship_name VARCHAR(100) NOT NULL,
    amount INT NOT NULL CHECK (amount > 0),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

INSERT INTO departments (department_id, department_name) VALUES
    (1, 'Computer Science'),
    (2, 'Electrical'),
    (3, 'Mechanical'),
    (4, 'Civil');

INSERT INTO students
    (student_id, student_name, department_id, marks, city) VALUES
    (101, 'Asha', 1, 96.00, 'Kolkata'),
    (102, 'Boby', 1, 78.50, 'Delhi'),
    (103, 'Chirag', 2, 88.00, 'Mumbai'),
    (104, 'Diya', 2, 64.00, 'Kolkata'),
    (105, 'Eshan', 3, 91.00, 'Delhi'),
    (106, 'Farah', NULL, 72.00, 'Pune');

INSERT INTO alumni
    (alumni_id, person_name, department_name, graduation_year) VALUES
    (201, 'Asha', 'Computer Science', 2022),
    (202, 'Gopal', 'Electrical', 2021),
    (203, 'Hina', 'Civil', 2023),
    (204, 'Boby', 'Computer Science', 2024);

INSERT INTO scholarship_applications
    (application_id, student_id, scholarship_name, amount) VALUES
    (301, 101, 'Merit', 50000),
    (302, 103, 'Merit', 30000),
    (303, 105, 'Research', 45000),
    (304, 106, 'Need Based', 25000);


-- ===================== SCALAR FUNCTIONS =====================

-- Q29
-- Display every student name in uppercase and every city in lowercase.
SELECT UPPER(student_name) AS name, LOWER(city) AS city FROM students;

-- Q30
-- Create a student label in this shape:
-- STUDENT_ID - STUDENT_NAME - CITY
SELECT CONCAT_WS(' - ', student_id, student_name, city) AS student_label FROM students;

-- Q31
-- Display each student's name and the number of characters in the name.
-- Sort from the longest name to the shortest.
SELECT student_name, CHAR_LENGTH(student_name) AS name_len FROM students ORDER BY name_len DESC;

-- Q32
-- Display each scholarship name in uppercase and each amount rounded to the
-- nearest thousand.
SELECT UPPER(scholarship_name), ROUND(amount, -3) FROM scholarship_applications;

-- Q33
-- Display each student and a department label. Students without a department
-- must show 'Unassigned' instead of NULL.
SELECT st.student_name, COALESCE(depts.department_name, 'Unassigned')
FROM students as st
LEFT JOIN departments as depts
ON st.department_id = depts.department_id;

-- Q34
-- Find students whose name contains at least five characters and whose marks
-- are at least 80.
SELECT * FROM students WHERE CHAR_LENGTH(student_name) >= 5 AND marks >= 80;

-- Q35
-- Display each scholarship application with a label of 'Large' when its
-- amount is at least 40000 and 'Regular' otherwise.
SELECT 
    *,
    CASE
      WHEN amount >= 40000 THEN 'Large'
      ELSE 'Regular'
    END AS Label
FROM scholarship_applications;

-- Q36
-- Display every student and classify marks as follows:
--   90 or above: 'Excellent'
--   75 through 89.99: 'Good'
--   below 75: 'Needs Improvement'
-- Use a scalar conditional function.
SELECT 
    *,
    CASE
      WHEN marks >= 90 THEN 'Excellent'
      WHEN marks >= 75 AND marks <= 89.99 THEN 'Good'
      ELSE 'Needs Improvement'
    END AS Remarks
FROM students;

-- Q37
-- Count students by the first letter of their names. Extract the letter
-- before grouping.
SELECT LEFT(student_name, 1) AS first_letter, COUNT(student_name) FROM students GROUP BY first_letter;

-- LEFT is not supported everywhere, SUBSTRING with 1,1 is workover.
SELECT SUBSTRING(student_name, 1,1) AS first_letter, COUNT(student_name) FROM students GROUP BY first_letter;


-- Q38
-- Display each alumni record with a label combining the person's name,
-- department, and graduation year.
SELECT *, CONCAT_WS(' ', person_name, department_name, graduation_year) AS Label FROM alumni;

-- Q39
-- Display the average scholarship amount rounded to two decimal places for
-- each scholarship name.
SELECT ROUND(AVG(amount), 2) AS avg_scholarship FROM scholarship_applications;

-- Q40
-- Create a report showing student name, uppercase city, rounded marks, and
-- an assigned/unassigned department label. Use at least four scalar
-- functions in the query.
SELECT 
    st.student_name,
    UPPER(st.city) AS city,
    ROUND(st.marks) AS marks,
    CASE 
        WHEN st.department_id IS NULL THEN 'Unassigned'
        ELSE 'Assigned'
    END AS department
FROM students as st; 

-- ===================== UNION AND UNION ALL =====================

-- Q1
-- Produce one list of names containing both current students and alumni.
-- Remove duplicate names.
SELECT student_name FROM students
UNION 
SELECT person_name FROM alumni;

-- Q2
-- Produce the same list, but preserve duplicate names this time.
SELECT student_name FROM students
UNION ALL
SELECT person_name FROM alumni;


-- Q3
-- Create one two-column list containing every current student and alumni:
-- person_name and source ('Student' or 'Alumni').
-- The two SELECT statements must have compatible column types.
SELECT 
    person_name,
    CASE
      WHEN graduation_year IS NULL THEN 'Student'
      ELSE 'Alumni'
    END AS source
 FROM (
    SELECT student_name AS person_name, NULL AS graduation_year FROM students
    UNION 
    SELECT person_name, graduation_year FROM alumni
) as combined
ORDER BY source, person_name;

-- Better, without subquery 
SELECT student_name AS person_name, 'Student' AS source FROM students
UNION 
SELECT person_name, 'Alumni' AS source FROM alumni;


-- Q4
-- Find every city represented by either current students or alumni.
-- Alumni do not have a city, so decide what comparable data should be
-- returned and explain the limitation in a comment.
SELECT NULL AS city FROM alumni
UNION
SELECT city FROM students;


-- Q5
-- Return the names that appear in both students and alumni.
-- Use UNION or UNION ALL as part of your reasoning, not a new topic.
SELECT * FROM (
    SELECT student_name AS name FROM students
    UNION ALL
    SELECT person_name AS name FROM alumni
) as combined
GROUP BY name 
HAVING count(*) > 1
ORDER BY name;


-- Q6
-- Build a single department-name list from departments and alumni.
-- Keep duplicates in one query and remove them in another query.
SELECT department_name FROM departments
UNION
SELECT department_name FROM alumni;

SELECT department_name FROM departments
UNION ALL
SELECT department_name FROM alumni;


-- ===================== SUBQUERIES IN WHERE =====================

-- Q7
-- Find students whose marks are greater than the average marks of all
-- students. Do not calculate the average manually.
SELECT * FROM students WHERE marks > (SELECT AVG(marks) FROM students);

-- Q8
-- Find students whose marks equal the highest mark in the table.
-- Return the student's name and marks.
SELECT student_name, marks FROM students WHERE marks = (SELECT MAX(marks) FROM students);

-- Q9
-- Find students who applied for a scholarship worth more than the average
-- scholarship amount.
SELECT st.student_id, st.student_name, sca.scholarship_name, sca.amount
FROM students as st
LEFT JOIN  scholarship_applications sca
ON sca.student_id = st.student_id
where sca.amount > (SELECT AVG(amount) FROM scholarship_applications)


-- Q10
-- Find students who have submitted at least one scholarship application.
-- Use an IN subquery and return each student only once.
SELECT * FROM students where student_id IN(SELECT DISTINCT student_id from scholarship_applications);

-- Q11
-- Find departments that have at least one student whose marks are above 90.
-- Return department names, not only department IDs.
SELECT dept.department_id, dept.department_name
FROM students as st
LEFT JOIN departments AS dept
ON st.department_id = dept.department_id
where dept.department_id IS NOT NULL 
GROUP BY dept.department_id, dept.department_name
HAVING COUNT(st.student_id) >= 1

-- Q12
-- Find students who are not from the department with the highest average
-- marks. Use a subquery for the highest average department result.
SELECT * FROM students WHERE department_id != (
    SELECT st.department_id
    FROM students as st
    LEFT JOIN  departments as dept
    ON st.department_id = dept.department_id
    WHERE st.department_id IS NOT NULL
    GROUP BY dept.department_id
    ORDER BY AVG(st.marks) DESC
    LIMIT 1
);


-- ===================== SUBQUERIES IN FROM =====================

-- Q13
-- Create a temporary result inside the FROM clause containing only students
-- with marks of 80 or above. From that result, display the average marks
-- by department.
-- Give the derived table an alias.
SELECT department_id, round(avg(department_id)) AS avg_marks FROM (SELECT * FROM students WHERE marks >= 80) AS tmp GROUP BY department_id;

-- Q14
-- Use a derived table to calculate the highest mark in each department,
-- then display only departments whose highest mark is above 85.
SELECT department_name, MAX(marks) AS max_marks FROM (
    SELECT st.student_name, dept.department_name, st.marks 
    FROM students as st
    LEFT JOIN departments as dept
    ON dept.department_id = st.department_id
) as tmp
GROUP BY department_name
HAVING max_marks > 85;

    
-- Q15
-- Use a derived table to count applications per student. Include the
-- student's name in the final result and show students with no applications.
-- Do not use a view for this question.
SELECT student_name, COUNT(application_id) FROM (
    SELECT st.student_id, st.student_name, sa.application_id
    FROM students as st 
    JOIN scholarship_applications AS sa 
    ON st.student_id = sa.student_id
) as temp
GROUP BY student_id

-- Q16
-- Find the department with the highest average student marks by first
-- creating a grouped derived table and then filtering that result.
SELECT department_name, avg(marks) FROM (
    SELECT dept.department_id, dept.department_name, st.student_id, st.marks
    FROM departments as dept 
    JOIN students as st 
    ON st.department_id = dept.department_id
) as tmp
GROUP BY department_id, department_name
ORDER BY AVG(marks) DESC
LIMIT 1

-- ===================== SUBQUERIES IN SELECT =====================

-- Q17
-- Display every student and the highest mark in the entire students table
-- beside each row.
SELECT *, (SELECT MAX(marks) FROM students) AS highest_marks FROM students

-- Q18
-- Display every department and the number of students in that department
-- using a scalar subquery in the SELECT list. Departments with no students
-- must still appear.
SELECT *, (
    SELECT COUNT(st.student_id)
    FROM departments as dept
    LEFT JOIN students as st
    ON st.department_id = dept.department_id
) AS student_count FROM departments;


-- ===================== VIEWS =====================

-- Q19
-- Create a view named student_details that exposes student ID, student name,
-- department name, city, and marks. Query the view as if it were a table.
CREATE VIEW student_details AS 
SELECT st.student_id, st.student_name, dept.department_name, st.city, st.marks
FROM students as st 
LEFT JOIN  departments as dept
ON st.department_id = dept.department_id;

SELECT * FROM student_details;

-- Q20
-- Create a view named department_summary that shows every department and
-- its student count, including departments with zero students.
CREATE VIEW department_summary AS 
SELECT dept.department_id, dept.department_name, COUNT(st.student_id) AS student_count
FROM departments as dept
LEFT JOIN students as st 
ON st.department_id = dept.department_id
GROUP BY dept.department_id, dept.department_name;

SELECT * FROM department_summary;

-- Q21
-- Query department_summary to find departments with at least two students.
SELECT * FROM department_summary WHERE student_count >= 2;

-- Q22
-- Replace student_details so that it exposes only student name,
-- department name, and marks. Query the updated view.
CREATE OR REPLACE VIEW student_details AS
SELECT st.student_name, dept.department_name,  st.marks
FROM students as st 
LEFT JOIN  departments as dept
ON st.department_id = dept.department_id;

SELECT * FROM student_details;

-- Q23
-- Update one student's marks, then query student_details again. Confirm
-- that a normal view reflects current table data.
UPDATE student_details SET marks = 22.00 WHERE student_name = 'Boby'
 
SELECT * FROM student_details where student_name = 'boby';
SELECT * FROM students where student_name = 'boby';

-- Q24
-- Drop student_details without dropping the students table. Verify that
-- querying the view fails while querying students still works.
DROP VIEW student_details;


-- ===================== MIXED CHALLENGES =====================

-- Q25
-- Find students who scored above the average mark of their own department.
-- This requires comparing each student with a grouped result.
SELECT * FROM students AS st where marks > (SELECT avg(marks) FROM students where department_id = st.department_id)

SELECT *
FROM  students as st 
JOIN (
    SELECT department_id, AVG(marks)  as avg_dept_marks
    FROM students
    GROUP BY department_id
) as avg_dept
ON st.department_id = avg_dept.department_id
WHERE st.marks > avg_dept.avg_dept_marks;


-- Q26
-- Create a view named scholarship_report that shows each student name,
-- department name, total scholarship amount, and application count.
-- Students without applications must remain visible with zero amount and
-- zero applications.
-- CREATE VIEW scholarship_report AS
CREATE OR REPLACE VIEW scholarship_report AS 
SELECT
    st.student_name,
    dept.department_name,
    COALESCE(SUM(scr.amount), 0) AS total_scholarship_amount,
    COUNT(scr.application_id) AS application_count 
FROM students as st
LEFT JOIN departments as dept 
ON st.department_id = dept.department_id
LEFT JOIN scholarship_applications as scr
ON st.student_id = scr.student_id
GROUP BY st.student_id, st.student_name;

-- Q27
-- Use scholarship_report to find students whose total scholarship amount
-- is greater than the overall average scholarship amount.
SELECT * FROM scholarship_report WHERE total_scholarship_amount > (SELECT AVG(total_scholarship_amount) FROM scholarship_report)

-- Q28
-- Combine current students and alumni into one view with columns:
-- person_name, academic_group, and year_value. Query the view ordered by
-- person_name and year_value.
 
create OR REPLACE view student_record AS
SELECT
    st.student_name as person_name,
    'Student' AS academic_group,
    NULL AS year_value
FROM students as st
UNION
SELECT
    person_name,
    'Alumni' AS academic_group,
    graduation_year AS year_value
 FROM alumni
ORDER BY person_name, year_value;

