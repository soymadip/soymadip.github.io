-- ------------------------------ SQL Sub Queries ---------------------------------

-- A subquery or inner query or Nested Query is a query within another sql query.
-- It involves 2 select statements.

-- There are some ways to write subquery:
--  - Inside SELECT
--  - Inside FROM
--  - Inside WHERE (most used)


-- Syntax:
SELECT column(s)
FROM table_name
WHERE col_name operator
( subquery );



CREATE TABLE stdnts (
    rollno INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    marks DECIMAL(5,2) CHECK (marks >= 0.00 AND marks <= 100.00)
);

INSERT INTO stdnts(rollno, name, marks) VALUES 
    (101, 'soymadip', 99.0),
    (102, 'boby', 77.6),
    (103,'googly', 45.0);


-- Ex: PICK students who have more than average marks
-- 1. find avg
-- 2. compare it with each student's marks
SELECT name, marks FROM stdnts WHERE marks > (SELECT AVG(marks) FROM stdnts); 


-- Find the students with even roll numbers
SELECT name, rollno FROM stdnts WHERE rollno % 2 = 0;

-- with subquery
SELECT name, rollno FROM stdnts WHERE rollno IN(SELECT rollno FROM stdnts WHERE rollno % 2 = 0);


-- --------- Inside FROM clause ---------------

-- We can use sub query in from statement to create a sub table from big table.
-- WE MUST GIVE THE SUB TABLE AN ALIAS

drop table stdnts;
CREATE TABLE stdnts(
    rollno int primary KEY AUTO_INCREMENT,
    name VARCHAR(50) not null,
    marks int DEFAULT 0,
    city VARCHAR(50) not null
) AUTO_INCREMENT=101;

INSERT INTO stdnts(name,  marks, city) VALUES 
    ('anil', 78, 'Pune'),
    ('bhumika', 93, 'Mumbai'),
    ('chetan', 85, 'Mumbai'),
    ('dhrub',96, 'Delhi'),
    ('emanuel', 92, 'Delhi'),
    ('farah', 82, 'Delhi');


-- find out max marks from the students of delhi
SELECT MAX(marks) FROM (SELECT * FROM stdnts WHERE city = 'Delhi') AS temp;

-- normally
SELECT MAX(marks) FROM stdnts WHERE city = 'Delhi'

-- where subquery
SELECT marks FROM stdnts WHERE marks = (SELECT MAX(marks) FROM stdnts) AND city = 'Delhi';



-- ------------- SELECT squpuery -----------------

-- we can also use subquery in select statement.

-- not very usefull though
SELECT name, (SELECT MAX(marks) FROM stdnts) AS max FROM stdnts;
