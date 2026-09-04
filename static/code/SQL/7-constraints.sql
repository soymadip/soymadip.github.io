-------------------- Constraints --------------------

-- Constraints are used to specify  rules for data in tables.


----- NOT NULL --------
--
-- calumns can't have NULL value. 


----- UNIQUE --------
--
-- all values in the column must be unique/different. No duplicate values are allowed.


----- PRIMARY KEY --------
-- 
-- makes a column unique and not null. but can be only used for one

CREATE TABLE student (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE student (
    roll_no INT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE,
    
    -- We add primary key at end for making multiple columns as primary key 
    PRIMARY KEY (roll_no, email)
);


-- ---- FOREIGN KEY --------

-- makes a column in one table refer to the primary key of another table. This is used to link two tables together.

-- Syntax: FOREIGN KEY (column_name) REFERENCES other_table(column_name)

CREATE TABLE emp (
    emp_id int PRIMARY KEY,
     
    -- We add foreign key at end
    FOREIGN KEY (cust_id) REFERENCES customer(cust_id)
);  



-- ------ DEFAULT --------

-- sets a default value for a column when no value is specified during insertion.

CREATE TABLE student (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    status ENUM('active', 'inactive') DEFAULT 'active'
);


-- ------ CHECK ---------

-- it can limit the values (or range of values) that can be placed in a column.

CREATE TABLE city (
    id INT PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    
    -- Inline check
    age INT CHECK (age >= 18),

    -- Or dedicated
     -- Syntax: CONSTRAINT constraint_name CHECK (condition)
    CONSTRAINT age_check CHECK (age >= 18 AND city="Delhi")
);

