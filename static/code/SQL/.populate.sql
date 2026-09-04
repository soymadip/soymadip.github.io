CREATE DATABASE IF NOT EXISTS college;
USE college;


DROP TABLE IF EXISTS student;

CREATE TABLE IF NOT EXISTS student (
    rollno INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    marks INT NOT NULL,
    grade ENUM('A', 'B', 'C', 'D', 'E', 'F'),
    city VARCHAR(20)
);

INSERT INTO student (rollno, name, marks, grade, city) VALUES
    (101, 'anil', 75, 'C', 'Mumbai'),
    (102, 'bhumika', 93, 'A', 'Mumbai'),
    (103, 'chetan', 85, 'B', 'Mumbai'),
    (104, 'dhruv', 96, 'A', 'Delhi'),
    (105, 'emanuel', 12, 'F', 'Delhi'),
    (106, 'farah', 82, 'B', 'Bengal');
    