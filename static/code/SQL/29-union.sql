-- ------------------- UNION ----------------------- 

-- It is used to combine result-set of two or more SLEECT statements. 
-- Gives Unique records

-- To Use it:
--  - Every SELECT should have same number of columns.
--  - Columns must have similar data types.
--  - Columns in every SELECT should be in same order.


-- Syntax:
SELECT column(s) FROM table_A
UNION 
SELECT column(s) FROM table_B

-- --------- UNION ALL ---------------- 
-- Gives duplicates in tables.

-- Syntax:    
SELECT column(s) FROM table_A
UNION ALL
SELECT column(s) FROM table_B;



-- ----------------------------------- Usage Example ----------------------------

DROP DATABASE IF EXISTS union_ex;
CREATE DATABASE IF NOT EXISTS union_ex;
USE DATABASE union_ex;
    
-- Table 1: Employees
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50)
);

-- Table 2: Contractors
CREATE TABLE contractors (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50)
);

-- Insert data into employees
INSERT INTO employees (id, name, department) VALUES
(1, 'Alice Smith', 'Engineering'),
(2, 'Bob Jones', 'Marketing'),
(3, 'Charlie Brown', 'Sales');

-- Insert data into contractors (Note: 'Bob Jones' exists in both tables)
INSERT INTO contractors (id, name, department) VALUES
(101, 'David Miller', 'Engineering'),
(102, 'Bob Jones', 'Marketing'),
(103, 'Emma Watson', 'HR');


-- It checks name & department columns to be same for duplicates
SELECT name, department FROM employees
UNION
SELECT name, department FROM contractors


-- Keep Duplicates
SELECT name, department FROM employees
UNION ALL
SELECT name, department FROM contractors
