-- --------------------- INDEXES ---------------------


-- when we run
SELECT * FROM users WHERE email = 'soymadip@example.com';

-- Postgres has to check every single row in the table, one by one, to find matches.
-- This is called a sequential scan (Seq Scan). Fine for 100 rows. Genuinely slow for 10 million rows.

-- So we create an index:
CREATE INDEX idx_users_email ON users(email);

-- This builds a separate data structure (a B-tree, by default) that's essentially a sorted lookup — like an index at the back of a book.
-- Instead of scanning every row, Postgres can jump almost directly to matching rows.
-- Same query, now uses an index scan instead of a sequential scan.


-- Use EXPLAIN to see how it is executing the query
EXPLAIN SELECT * FROM users WHERE email = 'soymadip@example.com';


-- ------- BUT THERE ARE TRADEOFFS -----------

-- Every index speeds up reads but slows down writes (insert, update, delete).
-- Because every write also have to update the index, not just table.

-- We should only use indexes on Columns:
--
-- 1. we filter frequently (eg WHERE email = '...'),
-- 2. we sort by often (eg ORDER BY name).
-- 3. we join on, specially foreign key columns (eg JOIN ON users.id = orders.user_id).
