-- ----------------- CASE STATEMENT ----------------

-- Evaluates a list of conditions sequentially and returns a specific value when the first true condition is met (similar to if/else if/else).
-- If no condition is true, it returns the value in the ELSE clause. If ELSE is omitted and no conditions match, it returns NULL.

-- Syntax:
-- CASE
--     WHEN condition1 THEN result1
--     WHEN condition2 THEN result2
--     ELSE default_result
-- END AS alias_name

SELECT 
    scholarship_name,
    amount,
    CASE 
        WHEN amount >= 40000 THEN 'Large'
        ELSE 'Regular'
    END AS application_label
FROM scholarships;



-- -------------- Visualize / Practice ---------------

CREATE TABLE scholarships (
    id INT PRIMARY KEY,
    scholarship_name VARCHAR(100),
    amount INT
);

INSERT INTO scholarships (id, scholarship_name, amount) VALUES
(1, 'STEM Leaders Grant', 50000),
(2, 'Community Hope Award', 15000),
(3, 'Excellence Merit', 40000);

-- Querying with multiple condition tiers:
SELECT 
    scholarship_name,
    amount,
    CASE 
        WHEN amount >= 50000 THEN 'Full Ride'
        WHEN amount >= 20000 THEN 'Major'
        WHEN amount >= 5000  THEN 'Partial'
        ELSE 'Minor'
    END AS grant_tier
FROM scholarships;

-- Results:
-- STEM Leaders Grant | 50000 | Full Ride
-- Community Hope Award | 15000 | Partial
-- Excellence Merit     | 40000 | Major

-- Top-to-bottom evaluation rule:
-- Once a condition matches (e.g., amount >= 50000), SQL stops evaluating further WHEN clauses for that row.



-- -------------------- Handling NULLs in CASE -------------------

-- Standard equality checks (=) fail on NULL. Use IS NULL or IS NOT NULL inside WHEN conditions instead.

SELECT 
    scholarship_name,
    amount,
    CASE 
        WHEN amount IS NULL THEN 'Pending Review'
        WHEN amount >= 40000 THEN 'Large'
        ELSE 'Regular'
    END AS status_label
FROM scholarships;
