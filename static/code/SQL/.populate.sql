CREATE DATABASE IF NOT EXISTS college;
USE college;


-- DROP TABLE IF EXISTS student;

CREATE TABLE IF NOT EXISTS student (
    rollno INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    marks INT NOT NULL,
    grade ENUM('A', 'B', 'C', 'D', 'E', 'F'),
    city VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    department VARCHAR(100) NOT NULL,
    salesperson VARCHAR(100) NOT NULL,
    ammount DECIMAL(10, 2) DEFAULT 0
);



INSERT INTO student (rollno, name, marks, grade, city) VALUES
    (101, 'anil', 75, 'C', 'Mumbai'),
    (102, 'bhumika', 93, 'A', 'Mumbai'),
    (103, 'chetan', 85, 'B', 'Mumbai'),
    (104, 'dhruv', 96, 'A', 'Delhi'),
    (105, 'emanuel', 12, 'F', 'Delhi'),
    (106, 'farah', 82, 'B', 'Bengal'),
    (107, 'geeta', 45, 'E', 'Pune'),
    (108, 'hari', 68, 'D', 'Bangalore'),
    (109, 'ishaan', 99, 'A', 'Mumbai'),
    (110, 'jia', 35, 'F', 'Chennai'),
    (111, 'karan', 72, 'C', 'Kolkata'),
    (112, 'lata', 88, 'B', 'Delhi'),
    (113, 'mohit', 55, 'E', 'Pune'),
    (114, 'neha', 91, 'A', 'Bangalore'),
    (115, 'omkar', 79, 'C', 'Mumbai'),
    (116, 'priya', 62, 'D', 'Chennai'),
    (117, 'qasim', 84, 'B', 'Kolkata'),
    (118, 'rohit', 28, 'F', 'Jaipur'),
    (119, 'sneha', 95, 'A', 'Jaipur'),
    (120, 'tanya', 74, 'C', 'Delhi');



INSERT INTO sales(department, salesperson, ammount) VALUES
    ('Electronics', 'Alice', 500.00),
    ('Electronics', 'Bob', 300.00),
    ('Clothing', 'Charlie', 100.00),
    ('Electronics', 'Alice', 200.00),
    ('Clothing', 'Bob', 150.00);

SELECT * FROM sales;