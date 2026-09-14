-- --------------------- Aggregate Functions ---------------------

-- Aggregate functions perform colculation on a set of values & return a single value.

-- Common aggregate functions include:
--
-- COUNT: Counts the number of rows in a result set.
-- SUM: Calculates the sum of a numeric column.
-- AVG: Calculates the average of a numeric column.
-- MAX: Finds the maximum value in a column.
-- MIN: Finds the minimum value in a column.


-- Most simple way to use aggregate functions is to use them in SELECT statement.

-- Count how many students are in the student table.
SELECT COUNT(name) FROM student;

-- Find the maximum marks in the student table.
SELECT MAX(marks) FROM student;

-- Average marks of students in the student table.
SELECT AVG(marks) FROM student;

SELECT SUM(ammount) FROM sales;



-- we can't use these in where clause,
-- because where is evaluated before table is aggregated..
-- where filters by applying condition each row by row.
-- so when where asks like more than AVG(marks), all the rows and avg is not yet calculated.

