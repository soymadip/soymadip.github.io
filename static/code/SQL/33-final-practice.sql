-- ===================== FINAL SQL PRACTICE =====================
-- This is a cumulative challenge for everything learned through views:
-- database and table creation, constraints, keys, INSERT/UPDATE/DELETE,
-- ALTER/TRUNCATE, filtering, ordering, LIMIT/OFFSET, aggregates, GROUP BY,
-- HAVING, joins, COALESCE, UNION, subqueries, and views.
--
-- Do not solve the questions in this file. Build each query yourself.

DROP DATABASE IF EXISTS final_sql_practice;
CREATE DATABASE final_sql_practice;
USE final_sql_practice;


-- ===================== DATABASE SETUP =====================

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(60) NOT NULL UNIQUE,
    office_city VARCHAR(60) NOT NULL,
    annual_budget INT NOT NULL CHECK (annual_budget > 0)
);

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department_id INT,
    manager_id INT,
    email VARCHAR(150) NOT NULL UNIQUE,
    salary INT NOT NULL CHECK (salary > 0),
    active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL UNIQUE,
    city VARCHAR(60) NOT NULL,
    status VARCHAR(20) DEFAULT 'active'
);

CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL UNIQUE,
    client_id INT NOT NULL,
    department_id INT NOT NULL,
    budget INT NOT NULL CHECK (budget > 0),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE project_assignments (
    employee_id INT,
    project_id INT,
    role_name VARCHAR(60) NOT NULL,
    hours_worked INT DEFAULT 0 CHECK (hours_worked >= 0),
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE contractors (
    contractor_id INT AUTO_INCREMENT PRIMARY KEY,
    person_name VARCHAR(100) NOT NULL,
    department_name VARCHAR(60) NOT NULL,
    hourly_rate INT NOT NULL CHECK (hourly_rate > 0)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    amount INT NOT NULL CHECK (amount > 0),
    payment_status VARCHAR(20) DEFAULT 'pending',
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);


INSERT INTO departments (department_name, office_city, annual_budget) VALUES
    ('Engineering', 'Kolkata', 900000),
    ('Finance', 'Delhi', 650000),
    ('Marketing', 'Mumbai', 500000),
    ('Human Resources', 'Kolkata', 350000),
    ('Research', 'Bangalore', 800000);

INSERT INTO employees
    (employee_name, department_id, manager_id, email, salary, active) VALUES
    ('Amit', 1, NULL, 'amit@company.test', 95000, TRUE),
    ('Priya', 1, 1, 'priya@company.test', 72000, TRUE),
    ('Rahul', 2, NULL, 'rahul@company.test', 88000, TRUE),
    ('Sneha', 3, NULL, 'sneha@company.test', 76000, TRUE),
    ('Arjun', 1, 1, 'arjun@company.test', 61000, TRUE),
    ('Neha', 2, 3, 'neha@company.test', 69000, TRUE),
    ('Riya', 4, NULL, 'riya@company.test', 56000, TRUE),
    ('Karan', NULL, NULL, 'karan@company.test', 50000, TRUE),
    ('Meera', 3, 4, 'meera@company.test', 59000, FALSE),
    ('Dev', 5, NULL, 'dev@company.test', 83000, TRUE);

INSERT INTO clients (client_name, city, status) VALUES
    ('Northwind Labs', 'Delhi', 'active'),
    ('Bluebird Retail', 'Mumbai', 'active'),
    ('Orbit Finance', 'Kolkata', 'paused'),
    ('Greenfield Health', 'Pune', 'active'),
    ('Unassigned Client', 'Chennai', 'active');

INSERT INTO projects
    (project_name, client_id, department_id, budget) VALUES
    ('Website Redesign', 1, 1, 180000),
    ('Payment Platform', 2, 1, 320000),
    ('Annual Audit', 3, 2, 110000),
    ('Recruitment Drive', 4, 4, 75000),
    ('Market Expansion', 2, 3, 210000),
    ('Research Prototype', 1, 5, 275000);

INSERT INTO project_assignments
    (employee_id, project_id, role_name, hours_worked) VALUES
    (1, 1, 'Lead Engineer', 35),
    (2, 1, 'Developer', 48),
    (2, 2, 'Developer', 30),
    (5, 1, 'Developer', 25),
    (5, 2, 'Tester', 40),
    (3, 3, 'Audit Lead', 42),
    (6, 3, 'Analyst', 38),
    (4, 5, 'Campaign Lead', 50),
    (9, 5, 'Campaign Analyst', 20),
    (10, 6, 'Research Lead', 44),
    (7, 4, 'Recruiter', 36);

INSERT INTO contractors
    (person_name, department_name, hourly_rate) VALUES
    ('Gopal', 'Engineering', 950),
    ('Hina', 'Finance', 850),
    ('Ira', 'Research', 1100),
    ('Priya', 'Engineering', 900);

INSERT INTO payments (client_id, amount, payment_status) VALUES
    (1, 80000, 'paid'),
    (1, 45000, 'pending'),
    (2, 120000, 'paid'),
    (3, 50000, 'failed'),
    (4, 30000, 'paid');


-- ===================== BASIC QUERY CONTROL =====================

-- Q1
-- Display active employees from Kolkata or Delhi whose salary is between
-- 60000 and 90000. Sort by salary descending, then name ascending.

-- Q2
-- Display the third and fourth highest-paid active employees using ORDER BY,
-- LIMIT, and OFFSET.

-- Q3
-- Return each client city only once, then return the cities in alphabetical
-- order.

-- Q4
-- Find projects whose names contain the word 'Platform' or 'Research'.


-- ===================== AGGREGATES AND GROUPING =====================

-- Q5
-- Show each department's employee count, average salary, minimum salary,
-- and maximum salary. Include departments with no employees.

-- Q6
-- Find departments with at least two active employees and an average salary
-- above 60000. Use HAVING for group-level conditions.

-- Q7
-- Show each client and the total amount of successful payments received.
-- Clients without successful payments must remain visible with total 0.

-- Q8
-- Show each project and total assigned hours. Include projects with no
-- assignments and replace NULL totals with 0.

-- Q9
-- Find departments whose projects have a combined budget greater than
-- 300000. Do not count a department's employee salary budget here.


-- ===================== RELATIONSHIPS AND JOINS =====================

-- Q10
-- Display every project with its client name, department name, budget, and
-- office city.

-- Q11
-- Display every employee with their manager's name. Employees without a
-- manager and employees without a department must still appear.

-- Q12
-- Find employees assigned to more than one project. Return each employee
-- once with their assignment count.

-- Q13
-- Find projects that have no assigned employees.

-- Q14
-- Find active employees who are not assigned to any project.

-- Q15
-- Display employee name, project name, role, and hours worked for every
-- assignment. Sort by project name and hours descending.

-- Q16
-- Generate every possible department-project pair for departments whose
-- annual budget is at least 500000. How many rows should be returned?

-- Q17
-- List every employee who earns more than their manager. Return both names
-- and both salaries.


-- ===================== DML AND CONSTRAINT PRACTICE =====================

-- Q18
-- Insert a new client and project for that client. Leave the client status
-- out of the INSERT and observe the default value.

-- Q19
-- Attempt to insert an employee with an email already in use. Explain the
-- constraint error in a comment, then remove the failed statement so the
-- rest of this file can run.

-- Q20
-- Give all active Engineering employees a 7 percent raise, then display the
-- changed rows before and after the update.

-- Q21
-- Delete failed payments, but first preview exactly which rows will be
-- removed.

-- Q22
-- Add a phone_number column to clients, populate every existing row, change
-- it to NOT NULL, rename it to contact_number, then remove it.

-- Q23
-- Create a backup table containing the current projects structure and rows.
-- Verify that the backup has the same number of rows as projects.

-- Q24
-- Create a temporary practice table, insert a few rows, and TRUNCATE it.
-- Confirm that the table still exists but contains no rows.


-- ===================== UNION AND UNION ALL =====================

-- Q25
-- Return one unique list of people made from employees and contractors.
-- The result must contain person_name and source_type.

-- Q26
-- Return the same people list while preserving duplicate names.
-- Explain why UNION ALL returns a different row count.

-- Q27
-- Return one unique list of department names appearing in departments or
-- contractors.


-- ===================== SUBQUERIES =====================

-- Q28
-- Find employees whose salary is above the average salary of all employees.

-- Q29
-- Find projects whose budget is greater than the average project budget.

-- Q30
-- Find clients who have at least one paid payment. Use an IN subquery and
-- return each client once.

-- Q31
-- Find employees who work in the department with the highest annual budget.

-- Q32
-- Using a derived table in FROM, calculate the average salary by department,
-- then return only departments whose average is above 70000.

-- Q33
-- Display every employee and the highest salary in the entire employees
-- table beside each employee using a scalar subquery in SELECT.

-- Q34
-- Find projects whose budget is higher than every project in the Marketing
-- department. Use a subquery and make the empty-result behavior sensible.

-- Q35
-- Find the highest-paid employee in each department. Return the department,
-- employee name, and salary. Employees tied for highest salary should all
-- be returned.


-- ===================== VIEWS =====================

-- Q36
-- Create a view named project_report containing project name, client name,
-- department name, budget, and total assigned hours. Projects with no
-- assignments must show zero hours.

-- Q37
-- Query project_report to find projects with budget above 150000 and total
-- assigned hours below 50.

-- Q38
-- Create a view named employee_workload containing every employee's name,
-- department name, project count, and total project hours. Employees with no
-- projects must remain visible.

-- Q39
-- Use employee_workload to find active employees with no project assignments.

-- Q40
-- Replace project_report so it also exposes client city and payment total.
-- Keep projects visible even when they have no payments.

-- Q41
-- Update a source table, query the view again, and verify that the view
-- reflects current data.

-- Q42
-- Drop employee_workload, then verify that employees still exists and that
-- only the view has been removed.


-- ===================== FINAL REPORTING CHALLENGES =====================

-- Q43
-- Produce a department performance report containing:
-- department name, employee count, active employee count, project count,
-- total project budget, and total assigned hours. Include empty departments.

-- Q44
-- Find clients whose paid payments are greater than the average paid amount
-- per client. Clients with no paid payments should not qualify.

-- Q45
-- Return the top two projects by budget, but only among projects with at
-- least one assignment. Use grouping, HAVING, ORDER BY, and LIMIT.

-- Q46
-- Return employees who are assigned to a project owned by a client from a
-- different city than the employee's department office city.

-- Q47
-- Build a unique people report by combining employees and contractors, then
-- identify names that occur in both source tables.

-- Q48
-- Explain in comments why each of these needs a different SQL feature:
--   a) filtering individual payments
--   b) filtering grouped client totals
--   c) finding employees above the company average
--   d) preserving departments with no employees

-- Q49
-- Design a view for a manager that hides employee email and salary but shows
-- employee name, department, manager, active status, and assignment count.

-- Q50
-- Final challenge: create a single report for each department showing the
-- highest-paid employee, number of projects, total project hours, and total
-- project budget. Preserve departments with no employees or projects.
