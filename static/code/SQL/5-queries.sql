
-- ======================== Database Related Queries =======================

-- gives error if db already exists
CREATE DATABASE college;

-- Only create id db doesnn't exist
-- Just gives warning if db already exists
CREATE DATABASE IF NOT EXISTS college;


-- Same for drop, delete only if db exists
DROP DATABASE IF EXISTS college;


-- Show all databases in server
SHOW DATABASES;

-- Show tables in selected database
SHOW TABLES;




-- ====================== Table Related Queries ======================

-- ------------ Create Table -------------   

CREATE TABLE student (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);


-- ----------------------- Select & view all columns -----------------------

-- SELECT * FROM table_name;
SELECT * FROM student;


-- --------------------- Insert Data Into Table -------------------

INSERT INTO student(roll_no, name) VALUES 
    (1, 'soymadip das'),
    (2, 'sonaii'),
    (3, 'google is shit');

-- If we have small table, we can ommit keys

INSERT INTO student VALUES(4, 'ramen Ass');

