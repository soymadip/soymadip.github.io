-- ==================== ALTER Clause ====================

-- ALTER TABLE statement is used to change the schema of an existing table.
-- It can be used to add, drop, or modify columns in an existing table.


-- Syntax:
ALTER TABLE table_name action;


-- Action can be:

-- --------------- ADD COLUMN -----------------

-- Add a new column to the table.

ALTER TABLE table_name ADD COLUMN column_name datatype constraints;


-- --------------- DROP COLUMN -----------------

-- Drop a column from the table.

ALTER TABLE table_name DROP COLUMN column_name;


-- --------------- MODIFY COLUMN -----------------

-- Modify the definition of an existing column.

ALTER TABLE table_name MODIFY COLUMN column_name new_datatype constraints;


-- --------------- RENAME COLUMN -----------------

-- Rename a column in the table.

ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;


-- --------------- RENAME TO -----------------

-- Rename a table.

ALTER TABLE table_name RENAME TO new_table_name;


-- --------------- CHANGE COLUMN -----------------

-- Change the name and/or definition of an existing column.

ALTER TABLE table_name CHANGE COLUMN old_column_name new_column_name new_datatype constraints;






-- --------- Ex ------------

-- Add age column to student table
ALTER TABLE student ADD COLUMN age INT;  -- New column's values will be NULL by default

-- Modify age column to be varchat
ALTER TABLE student MODIFY COLUMN age VARCHAR(2);


-- Change age column name to stu_age and type to int
ALTER TABLE student CHANGE COLUMN age stu_age INT DEFAULT 20;

-- Drop stu_age column from student table
ALTER TABLE student DROP COLUMN stu_age;

-- Rename Table
ALTER TABLE student RENAME TO stu;

ALTER TABLE stu RENAME TO student;