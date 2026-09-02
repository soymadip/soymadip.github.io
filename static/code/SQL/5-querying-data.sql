-- ------------------ simple query --------------------

-- Only name, gender. In which order we want..

-- select all columns
SELECT * FROM users;

-- select specific columns
SELECT gender, name FROM users;



-- ------------------- Filtering data --------------------
--
-- We use WHERE caluse to filter data.
--
-- BETWEEN  between range of values
-- OR       either one or another condition is true
-- AND      both conditions are true
-- IN       value is in a list of values
-- >        greater than
-- <        less than
-- =        equal to
-- !=       not equal to
-- >=       greater than or equal to
-- <=       less than or equal to

-- Only females
SELECT * FROM users WHERE gender = 'Female';

-- Only not female
SELECT * FROM users WHERE gender != 'Female';

-- dob before 1995-09-09
SELECT * FROM users WHERE date_of_birth < '1995-09-09';

-- Id Greater greater than 10
SELECT * FROM users WHERE id > 10;

-- Select rows where dob is null
SELECT * FROM users WHERE date_of_birth IS NULL;

-- Select rows where dob between 1990-09-09 and 1993-09-09
SELECT * FROM users WHERE date_of_birth BETWEEN '1990-09-09' AND '1993-09-09';

-- gender in male/female
SELECT * FROM users where gender IN ( 'Male', "Female" );

-- Select users where gender is female or salary is greater than 60000
SELECT * FROM users WHERE gender = 'Male' OR salary > 60000;



-- --------------------------- Sorting Data --------------------
--
-- We use ORDER BY clause to sort data in ascending(ASC) or descending(DESC) order.


-- users, order by salary descending
SELECT * FROM users ORDER BY salary DESC;

-- sort by salary asc/dsc
SELECT * FROM users WHERE salary > 70000 ORDER BY salary ASC;  -- ascending
SELECT * FROM users WHERE salary > 70000 ORDER BY salary DESC; -- descending

-- users with salary between 60000 and 70000, order by dob descending
SELECT * FROM users WHERE salary BETWEEN 60000 AND 70000 ORDER BY date_of_birth DESC;




-- --------------------------- Limiting Data --------------------
--
-- We use LIMIT clause to limit the number of rows returned by a query.


-- LImit data to 5 rows
SELECT * FROM users LIMIT 5;

-- select only id, name, salary. limit result to 5 rows
SELECT id, name, salary FROM users LIMIT 5; 

-- whose salary is greater than 70000, order by salary descending, limit results to 5 rows
SELECT * FROM users WHERE salary > 70000 ORDER BY salary DESC LIMIT 5; 

-- seelct id, name, salary, gender, created_at columns, where salary > 60000, order descending by creaated at, limit to 10 rows
SELECT id, name, salary, gender, created_at FROM users WHERE salary > 60000 ORDER BY created_at DESC LIMIT 10;

