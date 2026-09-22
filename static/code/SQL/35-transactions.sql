-- ======================== Transactions =========================

-- A transaction groups multiple statements into a single 'all-or-nothing' unit.
-- Either all statements succeed, or none are.

-- So why need? This example:
-- Transfer funds from one account to another.
-- deduction from one account and credit to another both needs to be successful or none should be applied.

BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;


-- BEGIN starts the transaction, but nothing is permanent yet.
-- COMMIT makes the changes permanent, both changes visible together, atomically.
-- If anything happens between BEGIN and COMMIT, the transaction is rolled back. Neither change is applied.
-- Database remains exactly as it was before.


-- ---- NOTE -----
-- We can explicitely tell to rollback the transaction.

BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

ROLLBACK; -- Rollbacks the transaction. Neither change is applied.

-- WE SHOULD NEVER USE COMMIT & ROLLBACK TOGETHER.


-- ----------------------- SELECT with Transactions -----------------------

-- We use FOR UPDATE to lock the rows we are reading, preventing concurrent updates.
-- This ensures that the data we read is not modified by other transactions.
-- We can use this to implement read-write locking.

BEGIN;

SELECT * FROM accounts WHERE id = 1 FOR UPDATE;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;

COMMIT;
