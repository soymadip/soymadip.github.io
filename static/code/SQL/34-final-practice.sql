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
SELECT *
FROM employees as em
LEFT JOIN departments as dept
ON em.department_id = dept.department_id
WHERE 
    em.active 
    AND 
    dept.office_city IN('Kolkata', 'Delhi')
    AND
    em.salary BETWEEN 60000 AND 90000;


-- Q2
-- Display the third and fourth highest-paid active employees using ORDER BY,
-- LIMIT, and OFFSET.
SELECT * FROM employees ORDER BY salary DESC LIMIT 2 OFFSET 2;

-- Q3
-- Return each client city only once, then return the cities in alphabetical
-- order.
SELECT DISTINCT city from clients ORDER BY city;

-- Q4
-- Find projects whose names contain the word 'Platform' or 'Research'.
SELECT * FROM projects WHERE project_name LIKE '%Platrofm%' OR project_name LIKE '%Research%';


-- Q5
-- Show each department's employee count, average salary, minimum salary,
-- and maximum salary. Include departments with no employees.
SELECT
    dept.department_name,
    COUNT(emp.employee_id) AS employee_count1,
    AVG(emp.salary) AS avg_salary,
    MIN(emp.salary) AS min_salary,
    MAX(emp.salary) AS max_salary
FROM departments as dept
LEFT JOIN employees as emp
ON emp.department_id = dept.department_id
GROUP BY dept.department_id, dept.department_name;

-- Q6
-- Find departments with at least two active employees and an average salary
-- above 60000. Use HAVING for group-level conditions.
SELECT  dept.department_name, COUNT(emp.employee_id)
FROM departments as dept
LEFT JOIN  employees as emp
ON emp.department_id = dept.department_id
WHERE emp.active
GROUP BY dept.department_id, dept.department_name
HAVING COUNT(emp.employee_id) >= 2 AND AVG(emp.salary) > 60000;

-- Q7
-- Show each client and the total amount of successful payments received.
-- Clients without successful payments must remain visible with total 0.
SELECT 
    clnt.client_id,
    clnt.client_name,
    COALESCE(
    SUM(
        CASE
          WHEN pmt.payment_status = 'paid' THEN pmt.amount
          ELSE 0
        END
    ),
    0
    ) AS total_payed
FROM clients as clnt 
LEFT JOIN payments as pmt 
ON pmt.client_id = clnt.client_id
GROUP BY clnt.client_id, clnt.client_name
ORDER BY total_payed;

-- Q8
-- Show each project and total assigned hours. Include projects with no
-- assignments and replace NULL totals with 0.
SELECT 
    prj.project_id,
    prj.project_name,
    COALESCE(SUM(asg.hours_worked),0) AS total_hours_worked
FROM projects as prj
LEFT JOIN project_assignments as asg
ON asg.project_id = prj.project_id
GROUP BY prj.project_id, prj.project_name;


-- Q9
-- Find departments whose projects have a combined budget greater than
-- 300000. Do not count a department's employee salary budget here.
SELECT
    dept.department_id,
    dept.department_name,
    SUM(prj.budget) AS total_budget
FROM departments as dept
LEFT JOIN projects as prj
ON prj.department_id = dept.department_id
GROUP BY dept.department_id, dept.department_name
HAVING SUM(prj.budget) > 300000;

-- Q10
-- Display every project with its client name, department name, budget, and
-- office city.
SELECT 
    prj.project_id,
    prj.project_name,
    cln.client_name,
    dept.department_name,
    prj.budget,
    dept.office_city
FROM projects as prj
LEFT JOIN clients as cln 
ON prj.client_id = cln.client_id
LEFT JOIN departments AS dept
ON prj.department_id = dept.department_id

-- Q11
-- Display every employee with their manager's name. Employees without a
-- manager and employees without a department must still appear.
SELECT
    emp.employee_id,
    emp.employee_name,
    mgr.employee_name AS manager_name
FROM employees as emp
LEFT JOIN employees AS mgr
ON emp.manager_id = mgr.employee_id;

-- Q12
-- Find employees assigned to more than one project. Return each employee
-- once with their assignment count.
SELECT
    emp.employee_id,
    emp.employee_name,
    COUNT(asg.project_id) AS assigned_projects
FROM employees AS emp
LEFT JOIN project_assignments as asg
ON asg.employee_id = emp.employee_id
WHERE asg.project_id IS NOT NULL
GROUP BY emp.employee_id, emp.employee_name
HAVING assigned_projects > 1;

-- Q13
-- Find projects that have no assigned employees.
SELECT 
    prj.project_id,
    prj.project_name,
    COUNT(asg.employee_id) AS assigned_employees
FROM projects as prj
LEFT JOIN project_assignments as asg
ON asg.project_id = prj.project_id
WHERE asg.employee_id IS NULL
GROUP BY prj.project_id, prj.project_name;

-- Q14
-- Find active employees who are not assigned to any project.
SELECT
    emp.employee_id,
    emp.employee_name
FROM employees as emp
LEFT JOIN project_assignments as asg
ON asg.employee_id = emp.employee_id
WHERE emp.active AND asg.project_id IS NULL


-- Q15
-- Display employee name, project name, role, and hours worked for every
-- assignment. Sort by project name and hours descending.
SELECT
    emp.employee_name,
    prj.project_name,
    asg.role_name,
    asg.hours_worked
FROM project_assignments as asg
LEFT JOIN employees as emp 
ON asg.employee_id = emp.employee_id
LEFT JOIN projects as prj
ON asg.project_id = prj.project_id
ORDER BY prj.project_name, asg.hours_worked DESC;

-- Q16
-- Generate every possible department-project pair for departments whose
-- annual budget is at least 500000. How many rows should be returned?
SELECT
    dept.department_name,
    proj.project_name
FROM departments as dept
LEFT JOIN projects as proj
ON proj.department_id = dept.department_id
WHERE dept.annual_budget >= 500000;

-- Q17
-- List every employee who earns more than their manager. Return both names
-- and both salaries.
SELECT emp.employee_name, emp.salary
FROM employees AS emp
LEFT JOIN employees AS mgr
ON emp.manager_id = mgr.employee_id
WHERE mgr.employee_id IS NOT NULL AND emp.salary > mgr.salary;

-- Q18
-- Insert a new client and project for that client. Leave the client status
-- out of the INSERT and observe the default value.
INSERT INTO clients(client_name, city) VALUES ('soymadip', 'Kolkata');
INSERT INTO projects(project_name, client_id, department_id, budget) VALUES(
    'Fuck Toy',6, 4, 100000
);

SELECT * FROM clients where client_name = 'soymadip'

-- Q19
-- Attempt to insert an employee with an email already in use. Explain the
-- constraint error in a comment, then remove the failed statement so the
-- rest of this file can run.

-- gives duplicate error because it's unique

-- Q20
-- Give all active Engineering employees a 7 percent raise, then display the
-- changed rows before and after the update.
SELECT * 
FROM employees as emp 
LEFT JOIN departments AS dept
ON emp.department_id = dept.department_id
WHERE emp.active AND dept.department_name = 'Engineering';

UPDATE employees SET salary = salary * 1.07 WHERE department_id = (select department_id from departments WHERE department_name = 'Engineering');

-- Q21
-- Delete failed payments
DELETE FROM payments WHERE payment_status = 'failed';

-- Q22
-- Add a phone_number column to clients, populate every existing row, change
-- it to NOT NULL, rename it to contact_number, then remove it.
ALTER TABLE clients ADD COLUMN phone_number INT CHECK(CHAR_LENGTH(phone_number) = 10);

UPDATE clients SET phone_number = 1234856902;

ALTER TABLE clients RENAME COLUMN phone_number TO contact_number;
ALTER TABLE clients MODIFY COLUMN contact_number INT NOT NULL;

ALTER TABLE clients DROP COLUMN contact_number;

-- Q23
-- Create a backup table containing the current projects structure and rows.
-- Verify that the backup has the same number of rows as projects.
CREATE TABLE prj_cp LIKE projects;
INSERT INTO prj_cp select * FROM projects;

-- Q24
-- Create a temporary practice table, insert a few rows, and TRUNCATE it.
-- Confirm that the table still exists but contains no rows.

CREATE TABLE temp_practice (
    id INT PRIMARY KEY,
    item_name VARCHAR(50)
);

INSERT INTO temp_practice (id, item_name)
VALUES 
    (1, 'Notebook'),
    (2, 'Pen'),
    (3, 'Eraser');

TRUNCATE TABLE temp_practice;
SELECT * FROM temp_practice;

-- Q25
-- Return one unique list of people made from employees and contractors.
-- The result must contain person_name and source_type.
SELECT employee_name as person_name, 'employee' AS source_type FROM employees
UNION
SELECT person_name, 'contractor' AS source_type FROM contractors;

-- Q26
-- Return the same people list while preserving duplicate names.
-- Explain why UNION ALL returns a different row count.
SELECT employee_name as person_name, 'employee' AS source_type FROM employees
UNION ALL
SELECT person_name, 'contractor' AS source_type FROM contractors;

-- there are no way duplicates because of source_type so giving same?

-- Q27
-- Return one unique list of department names appearing in departments or
-- contractors.
SELECT department_name FROM departments
UNION
SELECT department_name FROM contractors;

-- Q28
-- Find employees whose salary is above the average salary of all employees.
SELECT * FROM employees where salary > (SELECT AVG(salary) FROM employees);

-- Q29
-- Find projects whose budget is greater than the average project budget.
SELECT * FROM projects WHERE budget > (SELECT AVG(budget) FROM projects);

-- Q30
-- Find clients who have at least one paid payment. Use an IN subquery and
-- return each client once.
SELECT * FROM clients WHERE client_id IN(
    SELECT clnt.client_id 
    FROM clients as clnt
    LEFT JOIN payments as pmt
    ON pmt.client_id = clnt.client_id
    WHERE pmt.payment_status = 'paid'
    GROUP BY clnt.client_id
    HAVING COUNT(pmt.payment_id)
);

-- Q31
-- Find employees who work in the department with the highest annual budget.
SELECT * FROM employees  WHERE department_id IN(
    SELECT department_id FROM departments WHERE annual_budget = (SELECT MAX(annual_budget) FROM departments)
)

-- Q32
-- Using a derived table in FROM, calculate the average salary by department,
-- then return only departments whose average is above 70000.
SELECT * FROM (
    SELECT dept.department_name,  avg(emp.salary) AS avg_salary
    FROM departments as dept
    LEFT JOIN employees as emp
    ON emp.department_id = dept.department_id
    GROUP BY emp.department_id, dept.department_name
) AS tmp
WHERE avg_salary > 70000;


-- Q33
-- Display every employee and the highest salary in the entire employees
-- table beside each employee using a scalar subquery in SELECT.
SELECT *,(SELECT MAX(salary) FROM employees) AS highes_salary FROM employees;

-- Q34
-- Find projects whose budget is higher than every project in the Marketing
-- department. Use a subquery and make the empty-result behavior sensible.
SELECT * FROM projects WHERE budget > (
    SELECT COALESCE(MAX(proj.budget), 0) 
    FROM projects as proj 
    JOIN departments as dept 
    ON projects.department_id = dept.department_id
    where dept.department_name = 'Marketing'
)

-- Q35
-- Find the highest-paid employee in each department. Return the department,
-- employee name, and salary. Employees tied for highest salary should all
-- be returned.
SELECT emp1.department_id, emp1.employee_name, emp1.employee_name FROM employees as emp1 WHERE salary = (
    SELECT MAX(emp2.salary) FROM employees as emp2 where emp2.department_id = emp1.department_id
);

-- Q36
-- Create a view named project_report containing project name, client name,
-- department name, budget, and total assigned hours. Projects with no
-- assignments must show zero hours.
-- CREATE VIEW project_report AS
CREATE VIEW project_report AS 
SELECT
    prj.project_name,
    clnt.client_name,
    dept.department_name,
    prj.budget,
    asg.total_hours
FROM projects as prj
LEFT JOIN clients as clnt 
ON prj.client_id = clnt.client_id
LEFT JOIN departments as dept
ON prj.department_id = dept.department_id
LEFT JOIN (
    SELECT DISTINCT project_id, SUM(hours_worked) AS total_hours
    FROM project_assignments 
    GROUP BY project_id
) AS asg
ON asg.project_id = prj.project_id;


-- Q37
-- Query project_report to find projects with budget above 150000 and total
-- assigned hours below 50.
SELECT * FROM project_report WHERE budget > 150000 AND total_hours < 50;

-- Q38
-- Create a view named employee_workload containing every employee's name,
-- department name, project count, and total project hours. Employees with no
-- projects must remain visible.
CREATE VIEW employee_workload AS 
SELECT
    emp.employee_name,
    dept.department_name,
    COALESCE(asg.project_count, 0) AS project_count,
    COALESCE(asg.total_hours,0) AS total_hours
FROM employees as emp 
LEFT JOIN departments as dept
ON emp.department_id = dept.department_id
LEFT JOIN (
    SELECT employee_id, SUM(hours_worked) AS total_hours, COUNT(project_id) AS project_count
    FROM project_assignments 
    GROUP BY employee_id
) AS asg
ON emp.employee_id = asg.employee_id;


-- Q39
-- Use employee_workload to find active employees with no project assignments.
SELECT * FROM employee_workload WHERE project_count > 0;

-- Q40
-- Replace project_report so it also exposes client city and payment total.
-- Keep projects visible even when they have no payments.
-- CREATE OR REPLACE VIEW project_report AS 
SELECT
    prj.project_name,
    clnt.client_name,
    clnt.city,
    dept.department_name,
    pymt.total_payment,
    prj.budget,
    asg.total_hours
FROM projects as prj
LEFT JOIN clients as clnt 
ON prj.client_id = clnt.client_id
LEFT JOIN departments as dept
ON prj.department_id = dept.department_id
LEFT JOIN (
    SELECT DISTINCT project_id, SUM(hours_worked) AS total_hours
    FROM project_assignments 
    GROUP BY project_id
) AS asg
ON asg.project_id = prj.project_id
LEFT JOIN (
    SELECT client_id, SUM(amount) AS total_payment
    FROM payments
    GROUP BY client_id
) AS pymt
ON clnt.client_id = pymt.client_id;


-- Q41
-- Update a source table, query the view again, and verify that the view
-- reflects current data.
UPDATE clients SET client_name = 'soymadip' WHERE client_name = 'Northwind Labs';
SELECT * FROM  project_report;

-- Q42
-- Drop employee_workload, then verify that employees still exists and that
-- only the view has been removed.
DROP VIEW employee_workload;
SELECT * FROM employees;

-- Q43
-- Produce a department performance report containing:
-- department name, employee count, active employee count, project count,
-- total project budget, and total assigned hours. Include empty departments.

CREATE VIEW department_performance AS 
SELECT 
    dept.department_name,
    emps.emp_count,
    emps.active_emp_count,
    prjt.project_count,
    prjt.total_prj_budget,
    asg.total_hours
FROM departments as dept
LEFT JOIN (
    SELECT
        dt.department_id,
        COALESCE(COUNT(ep.employee_id),0) AS emp_count,
        COALESCE(COUNT(
            CASE WHEN ep.active THEN ep.employee_id ELSE NULL END
        ), 0) AS active_emp_count
    FROM departments as dt
    LEFT JOIN  employees as ep
    ON ep.department_id = dt.department_id
    GROUP BY dt.department_id
) AS emps
ON dept.department_id = emps.department_id
LEFT JOIN  (
    SELECT 
        dp.department_id,
        COALESCE(COUNT(prj.project_id), 0) AS project_count,
        COALESCE(SUM(prj.budget), 0) AS total_prj_budget
    FROM departments as dp 
    LEFT JOIN  projects as prj
    ON dp.department_id = prj.department_id
    GROUP BY dp.department_id
) AS prjt
ON dept.department_id = prjt.department_id
LEFT JOIN  (
    SELECT 
        pj2.project_id, 
        pj2.department_id, 
        COALESCE(sum(pa.hours_worked), 0) AS total_hours
    FROM projects as pj2
    LEFT JOIN  project_assignments as pa 
    ON pj2.project_id = pa.project_id
    GROUP BY pj2.project_id
) AS asg
ON dept.department_id = asg.department_id;


-- Q44
-- Find clients whose paid payments are greater than the average paid amount
-- per client. Clients with no paid payments should not qualify.
SELECT 
    clnts.client_id,
    clnts.client_name,
    pymt.total_paid
FROM clients as clnts
LEFT JOIN (
    SELECT    
        ct.client_id,
        COALESCE(SUM(pt.amount), 0) AS total_paid,
        AVG(pt.amount)
    FROM clients as ct
    LEFT JOIN payments as pt
    ON ct.client_id = pt.client_id
    GROUP BY ct.client_id
) AS pymt
ON pymt.client_id = clnts.client_id
WHERE pymt.total_paid > (
    SELECT AVG(amount)
    FROM payments WHERE payment_status = 'paid'
) AND pymt.total_paid > 0
ORDER BY clnts.client_id;


-- Q45
-- Return the top two projects by budget, but only among projects with at
-- least one assignment. Use grouping, HAVING, ORDER BY, and LIMIT.
SELECT * 
FROM projects AS prj
WHERE prj.project_id in (
    select 
        pr.project_id
    from projects AS pr
    LEFT JOIN project_assignments as asg
    ON asg.project_id = pr.project_id
    GROUP BY pr.project_id
    HAVING count(*) > 0
)
ORDER BY prj.budget DESC 
LIMIT 2;

-- Q46
-- Return employees who are assigned to a project owned by a client from a
-- different city than the employee's department office city.
SELECT DISTINCT
    emp.*,
    dept.office_city,
    clnt.city
FROM employees as emp
LEFT JOIN (
    SELECT prj.project_id, asg.employee_id, prj.client_id
    FROM projects as prj
    LEFT JOIN  project_assignments as asg
    ON prj.project_id = asg.project_id
) AS pri
ON emp.employee_id = pri.employee_id
LEFT JOIN  departments as dept 
ON emp.department_id = dept.department_id
LEFT JOIN clients as clnt 
ON pri.client_id = clnt.client_id
WHERE dept.office_city != clnt.city
ORDER BY emp.employee_id;

-- Q47
-- Build a unique people report by combining employees and contractors, then
-- identify names that occur in both source tables.

CREATE OR REPLACE VIEW  combined AS 
SELECT employee_name AS person_name, 'employee' AS source
FROM employees
UNION 
SELECT person_name AS person_name, 'contractor' AS job
FROM contractors;

SELECT DISTINCT person_name
FROM combined WHERE 
    combined.person_name IN(SELECT employees.employee_name  FROM employees) 
    AND 
    combined.person_name IN(SELECT contractors.person_name from contractors)

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
