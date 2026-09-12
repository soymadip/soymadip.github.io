-- ===================== JOIN PRACTICE =====================

DROP DATABASE IF EXISTS join_practice;
CREATE DATABASE join_practice;
USE join_practice;


-- The exercises use four related tables:
--   departments  -> employees
--   employees    -> employee_projects <- projects

CREATE TABLE departments (
	department_id INT PRIMARY KEY,
	department_name VARCHAR(50) NOT NULL,
	location VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
	employee_id INT PRIMARY KEY,
	employee_name VARCHAR(100) NOT NULL,
	department_id INT,
	manager_id INT,
	salary INT NOT NULL,
	FOREIGN KEY (department_id) REFERENCES departments(department_id),
	FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

CREATE TABLE projects (
	project_id INT PRIMARY KEY,
	project_name VARCHAR(100) NOT NULL,
	budget INT NOT NULL
);

CREATE TABLE employee_projects (
	employee_id INT,
	project_id INT,
	hours_worked INT NOT NULL,
	PRIMARY KEY (employee_id, project_id),
	FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
	FOREIGN KEY (project_id) REFERENCES projects(project_id)
);


INSERT INTO departments (department_id, department_name, location) VALUES
	(1, 'Engineering', 'Kolkata'),
	(2, 'Finance', 'Delhi'),
	(3, 'Marketing', 'Mumbai'),
	(4, 'Human Resources', 'Kolkata'),
	(5, 'Research', 'Bangalore');

INSERT INTO employees
	(employee_id, employee_name, department_id, manager_id, salary) VALUES
	(101, 'Amit', 1, NULL, 85000),
	(102, 'Priya', 1, 101, 65000),
	(103, 'Rahul', 2, NULL, 78000),
	(104, 'Sneha', 3, NULL, 72000),
	(105, 'Arjun', 1, 101, 60000),
	(106, 'Neha', 2, 103, 68000),
	(107, 'Riya', 4, NULL, 55000),
	(108, 'Karan', NULL, NULL, 50000),
	(109, 'Meera', 3, 104, 58000);

INSERT INTO projects (project_id, project_name, budget) VALUES
	(201, 'Website Redesign', 120000),
	(202, 'Payment System', 250000),
	(203, 'Recruitment Drive', 80000),
	(204, 'Sales Dashboard', 150000),
	(205, 'Internal Audit', 90000);

INSERT INTO employee_projects (employee_id, project_id, hours_worked) VALUES
	(101, 201, 30),
	(102, 201, 42),
	(102, 202, 25),
	(103, 202, 35),
	(104, 204, 40),
	(105, 201, 28),
	(105, 202, 32),
	(106, 205, 45),
	(107, 203, 38);


-- ===================== BASIC JOINS =====================


-- Q1
-- Display each employee together with the name of their department.
SELECT emp.employee_id, emp.employee_name, dept.department_name FROM employees as emp 
LEFT JOIN departments as dept 
ON emp.department_id = dept.department_id;

-- Q2
-- Display each employee's name, department, location, and salary.
SELECT emp.employee_name, dept.department_name,dept.location, emp.salary FROM employees as emp 
LEFT JOIN departments as dept 
ON emp.department_id = dept.department_id;

-- Q3
-- Find employees who work in the Engineering department.
SELECT emp.employee_name, dept.department_name FROM employees AS emp
LEFT JOIN departments AS dept
ON emp.department_id = dept.department_id
WHERE dept.department_name = 'Engineering';


-- Q4
-- Display every department, including departments that have no employees.
SELECT dept.department_name, COUNT(emp.employee_id) AS employee_count FROM departments as dept
LEFT JOIN employees as emp 
ON emp.department_id = dept.department_id
GROUP BY dept.department_id;

-- Q5
-- Find departments that currently have no employees.
select dept.department_name, count(emp.department_id) AS emp_count from departments as dept
left join employees as emp
ON emp.department_id = dept.department_id
group by dept.department_id
HAVING count(emp.department_id) = 0;

-- Q6
-- Display every employee, including employees who have not been assigned
-- to a department.
SELECT * FROM employees as emp;

-- Q7
-- Display every project, including projects with no assigned employees.
SELECT * FROM projects;


-- ===================== MULTIPLE-TABLE JOINS =====================

-- Q8
-- Display each employee's name and the projects they work on.
SELECT emp.employee_id, emp.employee_name, proj.project_name 
FROM employees as emp 
LEFT JOIN  employee_projects as eproj
ON emp.employee_id = eproj.employee_id
LEFT JOIN projects as proj
ON  proj.project_id = eproj.project_id;


-- Q9
-- Display the employee name, project name, and hours worked for every
-- employee-project assignment.
SELECT emp.employee_name, proj.project_name, epj.hours_worked 
FROM employees as emp
join employee_projects as epj
ON epj.employee_id = emp.employee_id
 JOIN  projects as proj
ON epj.project_id = proj.project_id;

-- Q10
-- Find employees who work on the Payment System project.
SELECT emp.employee_name FROM employees as emp 
JOIN employee_projects as epj 
ON epj.employee_id = emp.employee_id
JOIN projects as proj 
ON epj.project_id = proj.project_id
where proj.project_name = 'Payment System';

-- Q11
-- Find employees who are not assigned to any project.
SELECT * FROM employees as emp 
LEFT JOIN  employee_projects as epoj 
ON epoj.employee_id = emp.employee_id
where epoj.employee_id IS NULL;

-- Q12
-- Find projects that have no employees assigned to them.
SELECT proj.project_name 
FROM projects as proj
LEFT JOIN employee_projects as empj 
ON empj.project_id = proj.project_id
GROUP BY proj.project_name
HAVING COUNT(empj.employee_id) = 0;


-- ===================== AGGREGATE JOINS =====================

-- Q13
-- Count the employees in each department, including empty departments.
SELECT dpts.department_name, COUNT(emp.employee_id) AS employee_count
FROM departments as dpts
LEFT JOIN  employees as emp 
ON dpts.department_id = emp.department_id
GROUP BY dpts.department_name
ORDER BY COUNT(emp.employee_id) DESC;

-- Q14
-- Calculate the average salary for each department. Include empty
-- departments, but show NULL for a department without employees.
SELECT depts.department_name, ROUND(AVG(emp.salary))
FROM departments as depts
LEFT JOIN  employees as emp
ON emp.department_id = depts.department_id
GROUP BY depts.department_name
ORDER BY AVG(emp.salary) DESC;

-- Q15
-- Calculate the total hours worked on each project. Include projects
-- with no assignments and show zero instead of NULL.
SELECT prj.project_name, COALESCE(SUM(epj.hours_worked),0) AS total_hours_worked FROM projects as prj
LEFT JOIN employee_projects as epj
ON epj.project_id = prj.project_id
GROUP BY prj.project_name, prj.project_id
ORDER BY total_hours_worked DESC;


-- Q16
-- Find projects with at least two assigned employees.
SELECT prj.project_name, COUNT(epj.employee_id) AS assigned_employees
FROM projects as prj
JOIN employee_projects as epj
ON epj.project_id = prj.project_id
GROUP BY prj.project_name, prj.project_id
HAVING assigned_employees >= 2;

-- Q17
-- Find the total project hours for each department.
SELECT dept.department_name, COALESCE(SUM(epj.hours_worked), 0) AS total_hours
FROM departments as dept
LEFT JOIN employees as emp
ON emp.department_id = dept.department_id
LEFT JOIN employee_projects as epj
ON epj.employee_id = emp.employee_id
GROUP BY dept.department_name, dept.department_id
ORDER BY total_hours DESC;


-- ===================== SELF JOIN =====================

-- Q18
-- Display each employee together with their manager's name.
-- Employees without managers should still appear.
SELECT emp.employee_name, mgr.employee_name AS manager_name
FROM employees as emp
LEFT JOIN employees as mgr
ON emp.manager_id = mgr.employee_id
ORDER BY manager_name;

-- Q19
-- Find employees who earn more than their manager.
SELECT emp.employee_name, emp.salary, mgr.employee_name AS manager_name, mgr.salary
FROM employees as emp
JOIN employees as mgr
ON emp.manager_id = mgr.employee_id
WHERE emp.salary > mgr.salary;


-- ===================== CROSS JOIN =====================

-- Q20
-- Generate every possible department-project pair.
-- How many rows should this query return?


-- Q21
-- Generate every possible pair of different employees.
-- Do not pair an employee with themselves, and do not repeat a pair
-- in the opposite order.


-- ===================== JOIN THINKING =====================

-- Q22
-- Find the highest-paid employee in each department.


-- Q23
-- List employees who work on a project with a budget greater than 100000.
-- Return each employee only once, even if they work on multiple matching
-- projects.
SELECT DISTINCT emp.employee_name, prj.budget 
FROM employees as emp
JOIN employee_projects as eprj
ON eprj.employee_id = emp.employee_id
JOIN projects as prj
ON eprj.project_id = prj.project_id
WHERE prj.budget > 100000
ORDER BY prj.budget DESC;


-- Q24
-- Display every employee and the number of projects assigned to them.
-- Employees with no projects must show zero.
SELECT emp.employee_id ,emp.employee_name, COALESCE(COUNT(epj.project_id), 0) AS assigned_projects
FROM employees as emp 
LEFT JOIN  employee_projects as epj 
ON epj.employee_id = emp.employee_id
GROUP BY emp.employee_name, emp.employee_id
ORDER BY assigned_projects DESC;

