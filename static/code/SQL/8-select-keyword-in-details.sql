-- --------- SELECT KEYWORD IN DETAILS -----------

-- Used to select any data from a table in a database.


-- Select name and marks columns from student table
SELECT name, marks FROM student;

-- Select all columns from student table
SELECT * FROM student;



-- --- DISTINCT keyword --------

-- Only show unique values in the selected column.
-- It will remove duplicate values from the result set.

-- list cities, ommit duplicates
SELECT DISTINCT city FROM student;

