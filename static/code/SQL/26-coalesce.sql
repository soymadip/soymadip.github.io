/*
  SQL COALESCE Function
  ============================================================
  - Purpose: Evaluates arguments in order and returns the 
    first non-NULL value it encounters.
  
  - Main Use Case: Replacing NULL with 0 (or a default value) 
    when performing aggregate functions like SUM() alongside 
    LEFT JOINs where missing records evaluate to NULL.
  
  - Syntax Example: 
    COALESCE(expression_to_check, replacement_value)
    COALESCE(SUM(w.hours), 0)

  - Compatibility: ANSI SQL standard (Works in PostgreSQL, 
    SQL Server, SQLite, MySQL, and Oracle).
  ============================================================
*/

-- Create sample tables
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50)
);

CREATE TABLE bonuses (
    emp_id INT,
    bonus_amount DECIMAL(10, 2)
);

-- Insert sample data
INSERT INTO employees VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');
INSERT INTO bonuses VALUES (1, 500.00), (3, 250.00); -- Bob has no bonus row

-- Query using COALESCE
SELECT 
    e.emp_name,
    e.emp_id,
    -- Without COALESCE: Bob's bonus would be NULL
    -- With COALESCE: Returns 0.00 instead of NULL
    COALESCE(b.bonus_amount, 0.00) AS final_bonus
FROM 
    employees e
LEFT JOIN 
    bonuses b ON e.emp_id = b.emp_id;
