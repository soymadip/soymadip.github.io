-- --------------------- Selecting Data from Table ------------------------
--

-- select all columns from users table
SELECT * FROM users;

-- select specific columns from users table
--
-- Syntax:
-- SELECT column1, column2 FROM table_name;

SELECT name, email FROM users;


-- --------------------- Renaming a table ------------------------

-- Syntax:
-- RENAME TABLE old_table_name TO new_table_name;

RENAME TABLE users TO programmers;
RENAME TABLE programmers TO users;


-- --------------------- Altering a table ------------------------

-- Add a new column to a table
-- Syntax:
-- ALTER TABLE table_name ADD COLUMN column_name column_type constraints;
ALTER TABLE users ADD COLUMN is_active BOOLEAN DEFAULT TRUE;

-- Drop/Delete a column from a table
-- ALTER TABLE table_name DROP COLUMN column_name;
ALTER TABLE users DROP COLUMN is_active;

-- Modify a column's data
ALTER TABLE users MODIFY COLUMN email VARCHAR(150);

-- reorder columns in a table
-- ALTER TABLE table_name MODIFY COLUMN column_name column_type FIRST
-- ALTER TABLE table_name MODIFY COLUMN column_name column_type AFTER column_name;

-- take email after id
ALTER TABLE users MODIFY COLUMN email varchar(100) AFTER id;

-- take dob at first
ALTER TABLE users MODIFY COLUMN dob DATE FIRST;

show tables;

