-- ---------------------------- CTE -----------------------------

-- A CTE is just a named, temporary result set  you define with WITH, then use like a table inside your main query.
-- It's mechanically identical to a subquery — same job, different readability.


-- ------- Without CTE ---------

SELECT * FROM users
WHERE id IN (
    SELECT user_id FROM posts
    GROUP BY user_id
    HAVING COUNT(*) > 5
);


-- ------- With CTE ---------

WITH
    active_authors AS (
        SELECT user_id, COUNT(*) AS post_count
        FROM posts
        GROUP BY user_id
        HAVING COUNT(*) > 5
    )
SELECT users.username, active_authors.post_count
FROM users
JOIN active_authors ON users.id = active_authors.user_id;


-- -------- Multiple CTEs -----------

WITH post_counts AS (
    SELECT user_id, COUNT(*) AS total
    FROM posts
    GROUP BY user_id
),
active_authors AS (
    SELECT * FROM post_counts WHERE total > 5
)
SELECT users.username, active_authors.total
FROM users
JOIN active_authors ON users.id = active_authors.user_id;


SELECT title FROM posts
WHERE user_id IN (
    SELECT id FROM users WHERE username = 'soymadip'
);
