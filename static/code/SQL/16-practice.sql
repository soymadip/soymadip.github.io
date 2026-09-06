
CREATE TABLE payment (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer VARCHAR(50) NOT NULL,
    mode ENUM('Netbanking', 'Debit Card', 'Credit Card', 'UPI', 'Cash') NOT NULL,
    city VARCHAR(50) NOT NULL
);


INSERT INTO payment(customer, mode, city) VALUE
    ('Hari', 'Credit Card', 'Delhi'),
    ('Chetan', 'Credit Card', 'Bangalore'),
    ('Emanuel', 'Cash', 'Delhi'),
    ('Jia', 'Cash', 'Mumbai'),
    ('Bhumika', 'Debit Card', 'Delhi'),
    ('Geeta', 'Debit Card', 'Mumbai'),
    ('Anil', 'Netbanking', 'Mumbai'),
    ('Farah', 'Netbanking', 'Bangalore'),
    ('Dhruv', 'UPI', 'Mumbai'),
    ('Ishaan', 'UPI', 'Bangalore'),
    ('google', 'UPI', 'Bangalore');

-- Find out total payment count according to each payment method.
SELECT mode, COUNT(customer) FROM payment GROUP BY mode ORDER BY mode ASC;

-- count how many students got each grade
SELECT grade, COUNT(rollno) FROM student GROUP BY grade;