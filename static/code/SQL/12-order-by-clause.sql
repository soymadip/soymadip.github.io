
-- ---------------- ORDER BY Clause ------------------
--
-- Used to sort result in ascending(ASC) or descending(DESC) order.

-- Ascendint: 1, 2, 3, 4,....
-- Descending: ..., 4, 3, 2, 1

-- Eg: list students who have marks > 80 in descending order of marks.
SELECT * FROM student WHERE marks > 80 ORDER BY marks DESC;


-- Eg: List top 3 students
SELECT * FROM student ORDER BY marks DESC LIMIT 3;
