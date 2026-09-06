-- ------------- UPDATE clause -------------------

-- Changes the existing records in a table. 

-- Ex: Change marks of student with rollno 101 to 12
UPDATE student SET marks = '12' WHERE rollno = 101;

-- Now set grade to F
UPDATE student SET grade = 'F' WHERE rollno = 101;

-- Increase all student's marks by 1
UPDATE student SET marks  = marks + 1;

