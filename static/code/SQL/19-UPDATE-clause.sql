-- ------------- UPDATE clause -------------------

-- Changes the existing records in a table. 

-- Syntax: UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;

-- Ex: Change marks of student with rollno 101 to 12
UPDATE student SET marks = '12' WHERE rollno = 101;

-- Now set grade to F
UPDATE student SET grade = 'F' WHERE rollno = 101;

-- Increase all student's marks by 1
UPDATE student SET marks  = marks + 1;


