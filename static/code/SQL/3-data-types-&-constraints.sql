-- ------------ Date Types in SQL --------------
--
-- Data types define the type of data that can be stored in a column of a table.

-- Common data types include:
 
-- VARCHAR(n):      string(0-255), Variable-length character string with a maximum length of n characters, used for text data. (0-255)
-- BLOB:            string(0-65,535), Can store Binary Large Object, used for storing large binary data such as images or files.
-- BIT(n):          Stores x-bit values, x can range upto 64. usage: BIT(2) can store 00, 01, 10, 11. BIT(4) can store 0000, 0001, 0010, 0011, 0100, ....
-- INT:             string(-2,147,483,648 to 2,147,483,647), used for whole numbers.
-- DECIMAL(M,D):    Stores exact Decimal Numbers, What we put in is what we get. M is digits before . and D is after point
-- FLOAT:           Decimal Numbers, with precision to 23 digits. Used for storing approximate numeric values.
-- DOUBLE:          Decimal Numbers, with precision to 53 digits.
-- BOOLEAN:         Stores TRUE(0) or FALSE(1) values. In MySQL, it is a synonym for TINYINT(1).
-- DATE:            stores date in format 'YYYY-MM-DD'.
-- YEAR:            stores year in format 'YYYY'.
-- DATETIME:        Used for storing date and time values.
-- TIMESTAMP:       Stores date and time, automatically set to current timestamp when a row is created.
-- ENUM('val1', 'val'):  Used to define a set of predefined-permitted values.


-- --------------- Diff between DECMIMAL & FLOAT type -----------------

-- Decimal is more precise, flaot is approximate value. 
-- Decimal slightly slower for calculation

-- We sholdn't use = operator in float at all, instead we should use BETWEEN clause


-- --------------- Signed vs Unsigned Data Types -----------------
--
-- By default, numeric data types are signed, meaning they can store both positive and negative values
-- Unsigned data types can only store non-negative values (0 and positive numbers).
-- This increases the range of positive values that can be stored in the column.

-- TINYINT (signed) (-128 to 127)
-- TINYINT UNSIGNED (0 to 255) 


-- ---------------- Using BOOL Type ------------------

CREATE TABLE a_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(200) UNIQUE NOT NULL,
    is_active BOOL DEFAULT TRUE
);


INSERT INTO a_table (username, is_active) VALUES 
    ('soymadip', FALSE),
    ('sonaii', TRUE),
    ('guddu', 1);  -- we can use int 0/1 too. 1 means TRUE and 0 means FALSE


INSERT INTO a_table (username) VALUES 
    ('another_user'); -- relying on default value


-- Select records where is_active is TRUE
SELECT * FROM a_table WHERE is_active;

-- Or equal opwerator
SELECT * FROM a_table WHERE is_active = TRUE;

-- We can also use 1/0 instead of TRUE/FALSE in the WHERE clause.
SELECT * FROM a_table WHERE is_active = 0;

-- Choose False
SELECT * FROM a_table WHERE NOT is_active;

