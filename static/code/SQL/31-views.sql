-- -------------------------------- SQL Views -----------------------------------

-- a view is a virtual table based on the result-set of an SQL statement.

-- Used For:
-- 1. Simplify complex queries
-- 2. Security & Data hiding - We can restrict columns/data by creating view only what a user should view.
-- 3. Consistency: If bussiness defination changes, we change view defination and applications using the view remains same.

-- *A view always shows uptodate data. 
-- The database engine recreates the view every time a user queries it.


CREATE DATABASE views_ex;

CREATE TABLE departments (dept_id INT PRIMARY KEY, dept_name VARCHAR(50));
CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(50), marks DECIMAL(5,2), dept_id INT);

INSERT INTO departments VALUES (1, 'Computer Science'), (2, 'Electrical');
INSERT INTO students VALUES 
(101, 'Soumadip', 95.50, 1),
(102, 'Boby', 82.00, 1),
(103, 'Googly', 45.00, 2);


-- Create a view
-- that shows how many depts are there and student count in that dept
CREATE VIEW dept_summary AS 
SELECT dept.dept_id, dept.dept_name, COUNT(st.id) AS student_count
FROM departments AS dept 
LEFT JOIN students AS st 
ON dept.dept_id = st.dept_id
GROUP BY dept.dept_id, dept.dept_name;
