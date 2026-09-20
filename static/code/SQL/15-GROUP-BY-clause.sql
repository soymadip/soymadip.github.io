-- ------------------ GROUP BY Clause ------------------

-- Groups rows that have the same values into summary rows, like "find the number of customers in each country".
-- It collects data from multiple records and groups the results by one or more columns.

-- *Generally this is udes with some aggretation function.
-- Also, we shold atlaeast use the un aggregated column in group by clause.

-- make each query like this:
--      1. select key from table group by key
--      2. select key, func(key) from table group by key



-- Select city and count of roll numbers from the student table, grouped by city
SELECT city, count(rollno) FROM student GROUP BY city;


SELECT city,name, count(rollno) FROM student GROUP BY city, name;


-- avg marks each city, in ascending order
SELECT city, AVG(marks) FROM student GROUP BY city ORDER BY AVG(marks);



