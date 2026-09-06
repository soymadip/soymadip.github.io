-- ----------------- FOREIGN KEY ----------------

-- makes a column in one table refer to the primary key of another table. This is used to link two tables together.
-- When inserting data into child table, the fk's value should be present in the parent table's primary key.

-- Syntax: FOREIGN KEY (column_name) REFERENCES other_table(column_name)

CREATE TABLE emp (
    emp_id int PRIMARY KEY,
     
    -- We add foreign key at end
    FOREIGN KEY (cust_id) REFERENCES customer(cust_id)
);  



-- -------------- Visualize ---------------

CREATE TABLE dept (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE teacher (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    dept_id INT,
    
    -- Foreign key to the dept table's primary key
    FOREIGN KEY (dept_id) REFERENCES dept(id)
);

-- To visualize it, use ER diagram.
-- In phpmyadmin, db -> Designer

-- Here dept is Parent table & teacher is child table.
-- This is called referential integrity.

-- We can not delete any record from dept table if it is being used in teacher table.



-- -------------------- Cascading for Foreign Key -------------------

-- Cascading means that when we perform an action on the parent table, it will also affect the child table.

-- ------- On Delete Cascade ------------

-- When we create a foreign key using this option, it deletes the referencing rows in the child table
--  when the referenced row in the parent table which has a primary key.

-- For Example:
-- In a college we have IT department.
-- If we delete the dept name from dept table,
-- then all teacher rows whose dept_id references IT are also deleted.


-- ------- On Update Cascade ------------

-- When we create a foreign key using UPDATE CASCADE, the referencing rows are updated in the child table
-- when the referenced row is updated in the parent table which has a primary key.

-- For example:
-- In a college we have IT department.
-- If we change the dept name in dept table to computer science,
-- then all teachers' dept should also be updated to computer science.


CREATE TABLE dept (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE teacher (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,

    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES dept(id) ON DELETE CASCADE ON UPDATE CASCADE,

    rating INT CHECK (rating BETWEEN 1 AND 5)
);

INSERT INTO dept(id, name) values (2, 'CSE');
INSERT INTO teacher(id, name, dept_id, rating) values (1, 'soymadip das1', 2, 5);



-- ------------ On delete Setting NULL -----------------

-- In this option, when we delete the referenced row in the parent table, the referencing rows in the child table are set to NULL.
