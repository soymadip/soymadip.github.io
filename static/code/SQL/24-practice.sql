-- =================== INSERT DATA ====================

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    salary INTEGER,
    city TEXT,
    email TEXT UNIQUE,
    experience INTEGER DEFAULT 0
);


INSERT INTO employees (id, name, age, department, salary, city, email, experience) VALUES
    (1,  'Amit',    22, 'Engineering', 45000, 'Kolkata',  'amit@example.com',    1),
    (2,  'Priya',   28, 'HR',          52000, 'Delhi',    'priya@example.com',   5),
    (3,  'Rahul',   25, 'Engineering', 60000, 'Mumbai',   'rahul@example.com',   3),
    (4,  'Sneha',   31, 'Marketing',   58000, 'Kolkata',  'sneha@example.com',   7),
    (5,  'Arjun',   24, 'Engineering', 48000, 'Delhi',    'arjun@example.com',   2),
    (6,  'Neha',    29, 'Finance',     65000, 'Mumbai',   'neha@example.com',    6),
    (7,  'Vikram',  35, 'Engineering', 85000, 'Bangalore','vikram@example.com',  10),
    (8,  'Riya',    23, 'Marketing',   42000, 'Delhi',    'riya@example.com',    1),
    (9,  'Karan',   27, 'Finance',     55000, 'Kolkata',  'karan@example.com',   4),
    (10, 'Ananya',  30, 'HR',          70000, 'Mumbai',   'ananya@example.com',  8),
    (11, 'Sourav',  21, 'Engineering', 40000, 'Kolkata',  'sourav@example.com',  0),
    (12, 'Meera',   26, 'Marketing',   51000, 'Bangalore','meera@example.com',   3),
    (13, 'Dev',     33, 'Finance',     72000, 'Delhi',    'dev@example.com',     9),
    (14, 'Pooja',   28, 'HR',          49000, 'Kolkata',  'pooja@example.com',   4),
    (15, 'Aditya',  32, 'Engineering', 78000, 'Mumbai',   'aditya@example.com',  8);

SELECT * FROM employees;


-- Q1
-- The HR team needs a complete employee directory.
-- Display every column for every employee.
SELECT * FROM employees;

-- Q2
-- The company directory should show only each employee's name,
-- email, department, and city. Display those columns.
SELECT name, email, department, city FROM employees;

-- Q3
-- A manager wants to know which cities have employees.
-- Return each city only once.
SELECT DISTINCT city FROM employees;


-- Q4
-- Find employees who work in Engineering or Finance and do not live
-- in Kolkata.
SELECT * FROM employees WHERE department IN('Engineering', 'Finance') AND city != 'Kolkata' ORDER BY department;

-- Q5
-- Find employees aged from 25 through 30 whose salary is at least 50000.
SELECT * FROM employees WHERE age BETWEEN 25 AND 30 AND salary >= 50000;

-- Q6
-- Find employees whose names contain the letter 'a' and whose email
-- address ends with 'example.com'.
SELECT * FROM employees WHERE name LIKE '%a%' AND email LIKE '%example.com';

-- Q7
-- The promotion team needs employees from Delhi, Mumbai, or Bangalore
-- who have more than 3 years of experience.
SELECT * FROM employees WHERE city IN ('Delhi', 'Mumbai', 'Bangalore') AND experience > 3 ORDER BY experience DESC;

-- Q8
-- Display employees from the highest salary to the lowest salary.
-- When salaries are equal, show the more experienced employee first.
SELECT id, name, department, salary, experience FROM employees ORDER BY salary DESC, experience DESC;

-- Q9
-- Show the three youngest employees, displaying only their name, age,
-- and city.
SELECT name, age, city FROM employees ORDER BY age LIMIT 3;

-- Q10
-- The payroll team wants the second and third highest salaries.
-- Return the employee names and salaries using LIMIT with an offset.
SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 2 OFFSET 1;

-- Q11
-- Count the total number of employees and calculate the average salary.
SELECT COUNT(id), AVG(salary) FROM employees;

-- Q12
-- Find the lowest salary, highest salary, and total salary for the company.
SELECT MIN(salary), MAX(salary), SUM(salary) FROM employees;

-- Q13
-- Count the employees in each department.
SELECT department, COUNT(id) FROM employees GROUP BY department;

-- Q14
-- Calculate the average salary for each department and sort the result
-- from the highest average to the lowest average.
SELECT department, AVG(salary) FROM employees GROUP BY department ORDER BY AVG(salary) DESC;

-- Q15
-- Find departments with at least three employees.
SELECT department FROM employees GROUP BY department HAVING COUNT(id) >= 3;

-- Q16
-- For each city, display the number of employees and the highest salary.
-- Show the cities with the most employees first.
SELECT city, COUNT(id) AS emp_count, MAX(salary) AS max_salary FROM employees GROUP BY city ORDER BY COUNT(id) DESC;

-- Q17
-- The company hired Kunal for the IT department in Pune.
-- Insert him with a salary of 55000, 2 years of experience, and a
-- unique email address.
INSERT INTO employees(name, city, department, email, experience, salary) VALUES
    ('Kunal', 'Pune', 'IT','kunal@example.com', 2, 55000);


-- Q18
-- Insert a new employee while leaving out the experience column.
-- Check which default value the database assigns.
INSERT INTO employees(name, city, department, email, salary) VALUES
('solid employee', 'Non Existent City', 'IT', 'sss@email.com', 29999);


-- Q19
-- Try inserting another employee with an email already used by Amit.
-- Observe the constraint error and explain why it occurs.
INSERT INTO employees(name, city, department, email, salary) VALUES
    ('crapper', 'Finanance', 'IT', 'amit@example.com', 29999);

-- Q20
-- Amit received a promotion. Update his salary to 50000.
UPDATE employees SET salary = 50000 WHERE name = 'Amit';

-- Q21
-- Give every Marketing employee a 10 percent salary increase.
UPDATE employees SET salary = salary * 1.10 WHERE department = 'Marketing';

-- Q22
-- Give a 5000 raise to Finance employees with at least 5 years of
-- experience, and Engineering employees earning less than 60000.
-- Use parentheses so the conditions are grouped correctly.
UPDATE employees SET salary = salary + 5000
WHERE (experience >= 5 AND department = 'Finance') OR (department = "Engineering" AND salary < 60000);

-- Q23
-- Before deleting anything, preview employees who have less than
-- 2 years of experience and earn less than 45000.
SELECT * FROM employees WHERE experience < 2 AND salary < 45000;

-- Q24
-- Delete the employees identified in the previous question.
DELETE FROM employees WHERE experience < 2 AND salary < 45000;

-- Q25
-- Create a departments table with an automatically numbered primary key,
-- a required unique department name, and a city column defaulting to
-- 'Kolkata'.
CREATE TABLE departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL,
    city VARCHAR(100) DEFAULT 'Kolkata'
);


-- Q26
-- Insert Engineering, Finance, and HR into the departments table.
INSERT INTO departments(name) VALUES
    ('Engineering'),
    ('Finance'),
    ('HR');

-- Q27
-- Add a phone column to employees that can store up to 15 characters.
ALTER TABLE employees ADD COLUMN phone VARCHAR(15);

-- Q28
-- Fill in phone numbers for all employees, then change the phone column
-- so it cannot contain NULL values.
UPDATE employees SET phone = '0000000000';
ALTER TABLE employees MODIFY COLUMN phone VARCHAR(15) NOT NULL;

-- Q29
-- Rename the phone column to phone_number.
ALTER TABLE employees RENAME COLUMN phone TO phone_number;

-- Q30
-- Remove the phone_number column from employees.
ALTER TABLE employees DROP COLUMN phone_number;

-- Q31
-- Create an employees_backup table containing the same structure and
-- current rows as employees.

CREATE TABLE employees_backup LIKE employees;
INSERT INTO employees_backup SELECT * FROM employees;

-- Q34
-- A report currently uses this condition:
-- city = 'Delhi' OR city = 'Mumbai' AND experience < 5.
-- Write a query that returns employees from either Delhi or Mumbai
-- who have less than 5 years of experience.
SELECT * FROM employees WHERE city in('Delhi', 'Mumbai') AND experience < 5;

-- Q35
-- Empty the employees table while keeping its structure.
-- Then explain how TRUNCATE differs from DROP TABLE and DELETE.
TRUNCATE TABLE employees;
