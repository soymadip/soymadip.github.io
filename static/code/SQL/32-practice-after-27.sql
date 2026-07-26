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

-- Q30
-- Create a student label in this shape:
-- STUDENT_ID - STUDENT_NAME - CITY

-- Q31
-- Display each student's name and the number of characters in the name.
-- Sort from the longest name to the shortest.

-- Q32
-- Display each scholarship name in uppercase and each amount rounded to the
-- nearest thousand.

-- Q33
-- Display each student and a department label. Students without a department
-- must show 'Unassigned' instead of NULL.

-- Q34
-- Find students whose name contains at least five characters and whose marks
-- are at least 80.

-- Q35
-- Display each scholarship application with a label of 'Large' when its
-- amount is at least 40000 and 'Regular' otherwise.

-- Q36
-- Display every student and classify marks as follows:
--   90 or above: 'Excellent'
--   75 through 89.99: 'Good'
--   below 75: 'Needs Improvement'
-- Use a scalar conditional function.

-- Q37
-- Count students by the first letter of their names. Extract the letter
-- before grouping.

-- Q38
-- Display each alumni record with a label combining the person's name,
-- department, and graduation year.

-- Q39
-- Display the average scholarship amount rounded to two decimal places for
-- each scholarship name.

-- Q40
-- Create a report showing student name, uppercase city, rounded marks, and
-- an assigned/unassigned department label. Use at least four scalar
-- functions in the query.


-- ===================== UNION AND UNION ALL =====================

-- Q1
-- Produce one list of names containing both current students and alumni.
-- Remove duplicate names.

-- Q2
-- Produce the same list, but preserve duplicate names this time.
-- Observe the difference between UNION and UNION ALL.

-- Q3
-- Create one two-column list containing every current student and alumni:
-- person_name and source ('Student' or 'Alumni').
-- The two SELECT statements must have compatible column types.

-- Q4
-- Find every city represented by either current students or alumni.
-- Alumni do not have a city, so decide what comparable data should be
-- returned and explain the limitation in a comment.

-- Q5
-- Return the names that appear in both students and alumni.
-- Use UNION or UNION ALL as part of your reasoning, not a new topic.

-- Q6
-- Build a single department-name list from departments and alumni.
-- Keep duplicates in one query and remove them in another query.


-- ===================== SUBQUERIES IN WHERE =====================

-- Q7
-- Find students whose marks are greater than the average marks of all
-- students. Do not calculate the average manually.

-- Q8
-- Find students whose marks equal the highest mark in the table.
-- Return the student's name and marks.

-- Q9
-- Find students who applied for a scholarship worth more than the average
-- scholarship amount.

-- Q10
-- Find students who have submitted at least one scholarship application.
-- Use an IN subquery and return each student only once.

-- Q11
-- Find departments that have at least one student whose marks are above 90.
-- Return department names, not only department IDs.

-- Q12
-- Find students who are not from the department with the highest average
-- marks. Use a subquery for the highest average department result.


-- ===================== SUBQUERIES IN FROM =====================

-- Q13
-- Create a temporary result inside the FROM clause containing only students
-- with marks of 80 or above. From that result, display the average marks
-- by department.
-- Give the derived table an alias.

-- Q14
-- Use a derived table to calculate the highest mark in each department,
-- then display only departments whose highest mark is above 85.

-- Q15
-- Use a derived table to count applications per student. Include the
-- student's name in the final result and show students with no applications.
-- Do not use a view for this question.

-- Q16
-- Find the department with the highest average student marks by first
-- creating a grouped derived table and then filtering that result.


-- ===================== SUBQUERIES IN SELECT =====================

-- Q17
-- Display every student and the highest mark in the entire students table
-- beside each row.

-- Q18
-- Display every department and the number of students in that department
-- using a scalar subquery in the SELECT list. Departments with no students
-- must still appear.


-- ===================== VIEWS =====================

-- Q19
-- Create a view named student_details that exposes student ID, student name,
-- department name, city, and marks. Query the view as if it were a table.

-- Q20
-- Create a view named department_summary that shows every department and
-- its student count, including departments with zero students.

-- Q21
-- Query department_summary to find departments with at least two students.

-- Q22
-- Replace student_details so that it exposes only student name,
-- department name, and marks. Query the updated view.

-- Q23
-- Update one student's marks, then query student_details again. Confirm
-- that a normal view reflects current table data.

-- Q24
-- Drop student_details without dropping the students table. Verify that
-- querying the view fails while querying students still works.


-- ===================== MIXED CHALLENGES =====================

-- Q25
-- Find students who scored above the average mark of their own department.
-- This requires comparing each student with a grouped result.

-- Q26
-- Create a view named scholarship_report that shows each student name,
-- department name, total scholarship amount, and application count.
-- Students without applications must remain visible with zero amount and
-- zero applications.

-- Q27
-- Use scholarship_report to find students whose total scholarship amount
-- is greater than the overall average scholarship amount.

-- Q28
-- Combine current students and alumni into one view with columns:
-- person_name, academic_group, and year_value. Query the view ordered by
-- person_name and year_value.
