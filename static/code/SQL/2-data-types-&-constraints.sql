-- ------------ Date Types in SQL --------------
--
-- Data types define the type of data that can be stored in a column of a table.

-- Common data types include:
 
-- INT: Integer type, used for whole numbers.
-- VARCHAR(n): Variable-length character string with a maximum length of n characters, used for text data.
-- ENUM('value1', 'value2', 'value3'): Used to define a set of predefined-permitted values.
-- DATE: Used for storing date values.
-- DATETIME: Used for storing date and time values.
-- TIMESTAMP: Stores date and time, automatically set to current timestamp when a row is created.


-- ------------ Constraints in SQL --------------
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

-- ----------------------- Create a Table ------------------------

CREATE TABLE IF NOT EXISTS users (
-- key name,       data type,                        constraints
    id             INT                               AUTO_INCREMENT PRIMARY KEY,
    name           VARCHAR(100)                      NOT NULL,
    email          VARCHAR(100)                      UNIQUE NOT NULL,
    gender         ENUM('Male', 'Female', 'Other'),
    date_of_birth  DATE,
    created_at     DATETIME                          DEFAULT CURRENT_TIMESTAMP
);


-- ----------------------- Show Tables ------------------------

-- Show All tables in selected database
SHOW TABLES;

-- Show columns in users table
SELECT * FROM users;
