-- ===================== SCALAR FUNCTIONS =====================

-- A scalar function receives a value from one row and returns one value.
-- It runs once for each row in the result.
--
-- This is different from an aggregate function:
--   UPPER(name) changes one name at a time.
--   AVG(salary) combines many rows into one result.

DROP DATABASE IF EXISTS scalar_functions_ex;
CREATE DATABASE scalar_functions_ex;
USE scalar_functions_ex;


CREATE TABLE employees (
	employee_id INT PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	department VARCHAR(50) NOT NULL,
	salary DECIMAL(10, 2) NOT NULL,
	bonus DECIMAL(10, 2),
	joined_on DATE NOT NULL
);

CREATE TABLE orders (
	order_id INT PRIMARY KEY,
	customer_name VARCHAR(100) NOT NULL,
	order_total DECIMAL(10, 2) NOT NULL,
	ordered_on DATE NOT NULL,
	delivered_on DATE
);


INSERT INTO employees
	(employee_id, first_name, last_name, department, salary, bonus, joined_on)
VALUES
	(101, 'Amit', 'Sen', 'Engineering', 85000.00, 5000.00, '2021-04-12'),
	(102, 'priya', 'Das', 'Engineering', 72000.00, NULL, '2022-08-20'),
	(103, 'Rahul', 'Roy', 'Finance', 78000.00, 3500.00, '2020-01-05'),
	(104, 'Sneha', 'Ghosh', 'Marketing', 68500.50, NULL, '2023-06-17'),
	(105, 'Arjun', 'Bose', 'Engineering', 61000.00, 1800.00, '2024-02-29'),
	(106, 'neha', 'Khan', 'Finance', 69500.75, NULL, '2022-11-03');

INSERT INTO orders
	(order_id, customer_name, order_total, ordered_on, delivered_on)
VALUES
	(201, 'Asha Sen', 1250.75, '2025-01-10', '2025-01-14'),
	(202, 'Boby Das', 899.00, '2025-02-18', '2025-02-23'),
	(203, 'Chirag Roy', 2400.50, '2025-03-02', NULL),
	(204, 'Diya Ghosh', 450.25, '2025-03-15', '2025-03-17'),
	(205, 'Eshan Bose', 3100.00, '2025-04-01', '2025-04-11');


-- ===================== TEXT FUNCTIONS =====================

-- UPPER and LOWER change the letter case of text.
SELECT first_name, UPPER(first_name) AS uppercase_name, LOWER(last_name) AS lowercase_name
FROM employees;

-- CONCAT combines multiple values into one string.
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;

-- CONCAT_WS combines values with a separator.
SELECT CONCAT_WS(' - ', employee_id, first_name, department) AS employee_label
FROM employees;

-- CHAR_LENGTH counts characters. It is useful when validating text values.
SELECT first_name, CHAR_LENGTH(first_name) AS name_length
FROM employees;

-- LEFT and RIGHT take characters from the beginning or end of a string.
SELECT customer_name,
	   LEFT(customer_name, 4) AS name_prefix,
	   RIGHT(customer_name, 3) AS name_suffix
FROM orders;

-- SUBSTRING extracts part of a string. Positions start at 1 in MySQL.
SELECT customer_name, SUBSTRING(customer_name, 1, 4) AS short_name FROM orders;

-- TRIM removes leading and trailing spaces.
SELECT TRIM('   SQL practice   ') AS cleaned_text;


-- ===================== NUMERIC FUNCTIONS =====================

-- ROUND rounds a decimal value to the requested number of places.
SELECT order_id, order_total, 
    ROUND(order_total) AS rounded_total,
	  ROUND(order_total, 1) AS one_decimal_total
FROM orders;

-- CEIL rounds upward and FLOOR rounds downward.
SELECT order_total, CEIL(order_total) AS rounded_up, FLOOR(order_total) AS rounded_down
FROM orders;

-- ABS returns the positive distance from zero.
SELECT ABS(-25) AS positive_value;

-- MOD returns the remainder after division.
SELECT order_id, MOD(order_id, 2) AS odd_or_even_remainder
FROM orders;

-- Scalar numeric functions can be used in filters and sorting.
SELECT order_id, order_total
FROM orders
WHERE ROUND(order_total) >= 900
ORDER BY ROUND(order_total) DESC;


-- ===================== DATE FUNCTIONS =====================

-- YEAR, MONTH, and DAY extract parts of a date.
SELECT order_id, ordered_on,
	   YEAR(ordered_on) AS order_year,
	   MONTH(ordered_on) AS order_month,
	   DAY(ordered_on) AS order_day
FROM orders;

-- DATEDIFF returns the number of days between two dates.
-- A NULL delivered_on means the order has not been delivered.
SELECT order_id, DATEDIFF(delivered_on, ordered_on) AS delivery_days
FROM orders;

-- CURDATE returns the database server's current date.
SELECT CURDATE() AS today;

-- Date functions can also be used in a WHERE condition.
SELECT order_id, ordered_on
FROM orders
WHERE YEAR(ordered_on) = 2025
  AND MONTH(ordered_on) <= 3;


-- ===================== NULL AND CONDITIONAL FUNCTIONS =====================

-- COALESCE returns the first non-NULL value.
SELECT first_name, bonus,
	   COALESCE(bonus, 0) AS displayed_bonus
FROM employees;

-- IFNULL is a two-value alternative to COALESCE in MySQL.
SELECT order_id, delivered_on,
	   IFNULL(delivered_on, 'Not delivered') AS delivery_status
FROM orders;

-- NULLIF returns NULL when its two arguments are equal.
-- Otherwise it returns the first argument.
SELECT NULLIF(10, 10) AS equal_values,
	   NULLIF(10, 5) AS different_values;

-- IF chooses one value when a condition is true and another when false.
SELECT order_id, order_total,
	   IF(order_total >= 2000, 'Large', 'Regular') AS order_size
FROM orders;


-- ===================== COMBINING FUNCTIONS =====================

-- Functions can be nested. Read the expression from the inside outward.
SELECT CONCAT(UPPER(LEFT(first_name, 1)), LOWER(SUBSTRING(first_name, 2)))
	   AS formatted_first_name
FROM employees;

-- Scalar functions can be used before grouping. The grouped value is then
-- calculated from the transformed rows.
SELECT UPPER(department) AS department_name,
	   ROUND(AVG(salary), 2) AS average_salary
FROM employees
GROUP BY UPPER(department);

-- Calculate total compensation while treating a missing bonus as zero.
SELECT CONCAT(first_name, ' ', last_name) AS full_name,
	   salary + COALESCE(bonus, 0) AS total_compensation
FROM employees
ORDER BY total_compensation DESC;


