-- ------------ Date Types in SQL --------------
--
-- Data types define the type of data that can be stored in a column of a table.

-- Common data types include:
 
-- VARCHAR(n):      string(0-255), Variable-length character string with a maximum length of n characters, used for text data. (0-255)
-- BLOB:            string(0-65,535), Can store Binary Large Object, used for storing large binary data such as images or files.
-- BIT(n):          Stores x-bit values, x can range upto 64. usage: BIT(2) can store 00, 01, 10, 11. BIT(4) can store 0000, 0001, 0010, 0011, 0100, ....
-- INT:             string(-2,147,483,648 to 2,147,483,647), used for whole numbers.
-- FLOAT:           Decimal Numbers, with precision to 23 digits. Used for storing approximate numeric values.
-- DOUBLE:          Decimal Numbers, with precision to 53 digits.
-- BOOLEAN:         Stores TRUE(0) or FALSE(1) values. In MySQL, it is a synonym for TINYINT(1).
-- DATE:            stores date in format 'YYYY-MM-DD'.
-- YEAR:            stores year in format 'YYYY'.
-- DATETIME:        Used for storing date and time values.
-- TIMESTAMP:       Stores date and time, automatically set to current timestamp when a row is created.
-- ENUM('val1', 'val'):  Used to define a set of predefined-permitted values.


-- Signed vs Unsigned Data Types:
-- By default, numeric data types are signed, meaning they can store both positive and negative values
-- Unsigned data types can only store non-negative values (0 and positive numbers).
-- This increases the range of positive values that can be stored in the column.

-- TINYINT (signed) (-128 to 127)
-- TINYINT UNSIGNED (0 to 255) 



-- -------------------- Constraints in SQL ----------------------
--
-- Contraints are rules applied to columns in a table to enforce data integrity and consistency.

-- AUTO_INCREMENT: Automatically generates a unique for each row.
-- PRIMARY KEY:    Uniquely identifies each row in a table. primary key must be unique
-- NOT NULL:       Ensures that a column cannot have a NULL value.
-- UNIQUE:         Ensures that all values in a column are different.
-- DEFAULT:        Specifies a default value for a column when no value is provided.
--                 eg, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, is_active BOOLEAN DEFAULT TRUE 


-- In Vscode we are using startersql db for connection.
-- But in MySQL Workbench we need to create a database first and then use it. 
-- USE startersql;
