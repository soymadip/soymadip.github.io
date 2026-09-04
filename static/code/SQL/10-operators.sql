-- --------------- Using Operators -----------------

-- We can use many operators with WHERE clause to filter records based on a condition.
--
-- Arithmetic Operators: +, -, *, /, %
-- Comparison Operators: =, <>, !=, >, <, >=, <=
-- Logical Operators:    AND, OR, NOT, IN, BETWEEN, ALL, LIKE, ANY
-- Bitwise Operators:    &, |, ^, ~, <<, >>


-- Eg: Select students with marks greater than 80 and city Mumbai
SELECT * FROM student WHERE marks > 80 AND city = 'Mumbai';

-- Eg: list students with marks + 10 greater than 100
SELECT * FROM student WHERE marks+10 > 100;


-- ----- AND Operator ---------
--
-- Used to check if both conditions are true

-- Eg: students with marks > 80 and city Delhi
SELECT * FROM student WHERE marks > 80 AND city = 'Delhi';


-- ------- OR Operator ---------
--  
-- Used to check if either of the conditions is true

-- EG: students with marks > 80 or city Delhi
SELECT * FROM student WHERE marks > 80 OR city = 'Delhi';


-- ----------- BETWEEN Operator -----------
-- 
-- Used to filter values within a certain range. (Inclusive of the range values)
-- The values can be numbers, text, or dates.

-- Eg: Select students with marks between 40 and 80
SELECT * FROM student WHERE marks BETWEEN 40 AND 80;


-- ----------- IN Operator -----------
-- 
-- Used to filter values based on a list of values.
-- It is a shorthand for multiple OR conditions.

-- Eg: list students with city in Delhi/Mumbai
SELECT * FROM student WHERE city IN ('Delhi', 'Bengal');


-- -------------- NOT Operator -------------
-- 
-- Negates a condition.
-- It is used to filter records that do not match the specified condition.

-- Eg: list students with marks not equal to 80
SELECT * FROM student WHERE NOT marks = 80;

