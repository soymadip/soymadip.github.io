
-- =================== INSERT DATA ====================

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
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


-- ===================== QUESTION SET ====================

-- Q1
-- Display every employee.
SELECT * FROM employees;

-- Q2
-- Display only the name and salary of every employee.
SELECT name, salary FROM employees;

-- Q3
-- Display the name, department and city of every employee.
SELECT name, department, city FROM employees;

-- Q4
-- Find all employees who work in the Engineering department.
SELECT * FROM employees WHERE department = 'Engineering';

-- Q5
-- Find all employees who live in Kolkata.
SELECT * FROM employees WHERE city = 'Kolkata';


-- Q6
-- Find employees whose salary is greater than 60000.
SELECT * FROM employees WHERE salary > 60000 ORDER BY salary DESC;

-- Q7
-- Find employees whose salary is less than or equal to 50000.
SELECT * FROM employees WHERE salary <= 50000;

-- Q8
-- Find employees whose age is exactly 28.
SELECT * FROM employees WHERE age = 28;

-- Q9
-- Find employees who have more than 5 years of experience.
SELECT * FROM employees WHERE experience > 5;

-- Q10
-- Find employees who are younger than 25 AND earn more than 40000.
SELECT * FROM employees WHERE age < 25 AND salary > 40000;


-- Q11
-- Find employees who work in Engineering OR Finance.
SELECT * FROM employees WHERE department = 'Finance' OR department = 'Engineering';


-- Q12
-- Find employees who live in Kolkata AND work in Engineering.
SELECT * FROM employees WHERE city = 'Kolkata' AND department = 'Engineering';

-- Q13
-- Find employees who live in Delhi OR Mumbai.
SELECT * FROM employees WHERE city = 'Delhi' OR city = 'Mumbai';

-- Q14
-- Find employees whose salary is greater than 50000
-- AND whose experience is at least 5 years.
SELECT * FROM employees WHERE salary > 50000 AND experience >= 5;

-- Q15
-- Find employees who are NOT from Kolkata.
SELECT * FROM employees WHERE city != 'Kolkata';

-- Q16
-- Find employees who do NOT work in HR.
SELECT * FROM employees WHERE department != 'HR';

-- Q17
-- Find employees whose salary is between 50000 and 70000.
-- (Think carefully about whether BETWEEN includes the boundaries.)
SELECT *  FROM employees WHERE salary BETWEEN 50000 AND 70000;

-- Q18
-- Find employees whose age is between 25 and 30.
SELECT * FROM  employees WHERE age BETWEEN 25 AND 30;

-- Q19
-- Find employees whose salary is NOT between 50000 and 70000.
SELECT * FROM employees WHERE salary NOT BETWEEN 50000 AND 70000;

-- Q20
-- Find employees whose department is either HR or Marketing.
-- Use an operator specifically designed for checking multiple values.
SELECT * FROM employees WHERE department IN ('HR', 'Marketing' );

-- Q21
-- Find employees whose city is NOT Delhi and NOT Mumbai.
SELECT * FROM employees WHERE city NOT IN ('Delhi', 'Mumbai');

-- Q22
-- Find the first 5 employees.
SELECT * FROM employees LIMIT 5;

-- Q23
-- Find the first 3 employees whose salary is greater than 60000.
SELECT * FROM employees WHERE salary > 60000 LIMIT 3;

-- Q24
-- Find the names and salaries of employees earning
-- at least 55000.
SELECT name, salary FROM employees WHERE salary >= 55000;

-- Q25
-- Find employees who are either:
--   - from Kolkata and work in Engineering
-- OR
--   - from Mumbai and work in Finance
--
-- Be careful with AND/OR precedence.
SELECT * FROM employees WHERE 
    (city = 'Kolkata' AND department = 'Engineering')
    OR
    (city = 'Mumbai' AND department = 'Finance');


-- Q26
-- Find employees who are:
--   - younger than 25
-- OR
--   - older than 30.
SELECT * FROM employees WHERE age < 25 OR age > 30;


-- Q27
-- Find employees whose name starts with 'A'.
SELECT * FROM employees WHERE name LIKE 'A%';


-- Q28
-- Find employees whose name ends with 'a'.
SELECT * FROM employees WHERE name LIKE '%a';

-- Q29
-- Find employees whose name contains 'i'.
SELECT * FROM employees WHERE name LIKE '%i%';

-- Q30
-- Find employees whose email contains 'example.com'.
SELECT * FROM employees WHERE email LIKE '%example.com';

-- Q31
-- Display only the name and department of employees
-- whose salary is NOT 50000.
SELECT name, department FROM employees WHERE  salary != 50000;

-- Q32
-- Find the 5 employees with salary greater than 45000.
SELECT * FROM employees WHERE salary > 45000 LIMIT 5;

-- Q33
-- Find employees whose age is NOT 28.
SELECT * FROM employees WHERE age != 28;

-- Q34
-- Find employees whose experience is 0.
SELECT * FROM employees WHERE experience = 0;

-- Q35
-- Find employees whose experience is greater than or equal to 5
-- AND whose salary is less than 70000.
SELECT * FROM employees WHERE experience >= 5 AND salary < 70000;

-- ============================================================
-- UPDATE / DELETE PRACTICE
-- ============================================================

-- Q36
-- Give Amit a salary of 50000.


-- Q37
-- Increase Rahul's salary to 65000.


-- Q38
-- Change Sneha's city from Kolkata to Delhi.


-- Q39
-- Give every Engineering employee 5000 more salary.
--
-- WARNING:
-- Think about the WHERE clause before executing this.


-- Q40
-- Change the department of employee with id 14 to Marketing.


-- Q41
-- Delete the employee whose id is 11.


-- Q42
-- Delete all employees who have less than 2 years of experience.
--
-- WARNING:
-- This deletes multiple rows.


-- ============================================================
-- MIXED / THINKING QUESTIONS
-- ============================================================

-- Q43
-- Find the names of employees from Kolkata
-- who earn more than 45000.
SELECT name FROM employees WHERE salary > 45000 AND city = 'Kolkata';

-- Q44
-- Find the first 3 Engineering employees
-- who earn more than 50000.
SELECT * FROM employees WHERE salary > 50000  AND department = 'Engineering' LIMIT 3;

-- Q45
-- Find employees who are between 25 and 30 years old
-- AND earn at least 50000.
SELECT * FROM employees WHERE (age BETWEEN 25 AND 30) AND salary >= 50000;

-- Q46
-- Find employees from Delhi whose salary is
-- either below 50000 OR above 65000.
SELECT * FROM employees WHERE city = 'Delhi' AND (salary < 50000 OR salary > 65000);

-- Q47
-- Find employees who are NOT in Engineering
-- and earn more than 55000.
SELECT * FROM employees WHERE department != 'Engineering' AND salary > 55000;

-- Q48
-- Find employees whose name contains the letter 'a'
-- and who have at least 3 years of experience.
SELECT * FROM employees WHERE name LIKE '%a%' AND experience >= 3;

-- Q49
-- Find the first 5 employees whose salary is
-- between 45000 and 70000.
SELECT * FROM employees WHERE salary BETWEEN 45000 AND 70000 LIMIT 5;

-- Q50
-- Find employees who satisfy either of these:
--
--   1. Engineering employees with salary >= 70000
--   2. Finance employees with experience >= 5
--
-- Use parentheses where appropriate.
SELECT * FROM employees WHERE (department = 'Engineering' AND salary >=70000) OR (department = 'Finance' AND experience >= 5);


-- ============================================================
-- CONSTRAINT / DATA-MODIFICATION PRACTICE
-- ============================================================

-- Q51
-- Try inserting an employee without providing an id.
-- What happens?
INSERT INTO employees(name, age, city, department, email, experience, salary) VALUES
    ('Rohit', 26, 'Delhi', 'Engineering', 'rohit@example.com', 3, 60000);

-- Gives error: ERR_NO_DEFAULT_FOR_FIELD. Field 'id' doesn't have a default value    


-- Q52
-- Try inserting another employee with id = 1.
-- What happens and why?
INSERT INTO employees(id, name, age, city, department, email, experience, salary) VALUES
    (1, 'poor boy', 45, 'Pune', 'HR', 'rohit@example.com', 3, 60000);

-- ERR_DUP_ENTRY: Duplicate entry '1' for key 'PRIMARY'. Because id is primary key and it should be unique.



-- Q53
-- Try inserting another employee using:
-- email = 'amit@example.com'
-- What happens and why?
INSERT INTO employees(id, name, age, city, department, email, experience, salary) VALUES
    (2, 'Amit', 30, 'Mumbai', 'Finance', 'amit@example.com', 5, 70000);

-- ERR_DUP_ENTRY: Duplicate entry 'amit@example.com' class='link' target='_blank'>amit@example.com for key 'email'.
-- Because email is unique and it should be unique. We already have an employee with email '

-- Q54
-- Try inserting an employee without a name.
-- What happens and why?


-- Q55
-- Insert a new employee while leaving out
-- the experience column.
-- What value does experience get?


-- Q56
-- Try inserting NULL into the name column.
-- What happens and why?


-- ============================================================
-- LIMIT PRACTICE
-- ============================================================

-- Q57
-- Return only 1 employee.
SELECT * FROM employees LIMIT 1;

-- Q58
-- Return only 10 employees whose department is Engineering.
SELECT * FROM employees WHERE department = 'Engineering' LIMIT 10;

-- Q59
-- Return only 2 employees whose salary is greater than 60000.
SELECT * FROM employees WHERE salary > 60000 LIMIT 2;

-- Q60
-- Return only 4 employees from Kolkata
-- whose age is greater than 20.
SELECT * FROM employees WHERE city = 'Kolkata' AND age > 20 LIMIT 4;
