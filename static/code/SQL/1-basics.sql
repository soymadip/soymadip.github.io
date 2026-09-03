-- ----------------- What is a database? ---------------------
-- A database is a container that stores related data in an organized way.
-- It allows for efficient retrieval, manipulation, and storage of data.

-- A DataBase is like a folder.
-- Each TABLE is a file in that folder
-- The ROWS in the table are like the content inside each file

-- ----------------- What is query? ---------------------
-- A query is a request/command for data or information from a database. 
-- It is typically written in a specific language, such as SQL (Structured Query Language), and allows users to retrieve, update, or manipulate data stored in the database. Queries can be simple, retrieving specific records, or complex, involving multiple tables and conditions.
-- sql is all about writing efficient queries

-- --------------------- What is DBMS? ---------------------
-- A DBMS or Database Management System is a software application that allows users to create, manage, and interact with databases. It provides an interface for users to perform various operations on the data, such as querying, updating, and deleting records.
-- A DBMS ensures data integrity, security, and efficient data management.
-- Examples: PostgreSQL, MySQL, Oracle Database, Microsoft SQL Server, MongoDB, etc.


-- ------------- Relational vs Non-Relational Databases -----------------
-- Relational Databases:
-- Relational databases organize data into tables (also known as relations) with rows and columns.
-- Each table has a unique identifier called a primary key, and relationships between tables are established using foreign keys.
-- Examples: MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server. 

-- Non-Relational Databases:
-- Non-relational databases, also known as NoSQL databases, store data in a more flexible and scalable way.
-- They do not use the traditional table-based structure of relational databases.
-- Examples: MongoDB, Cassandra, Redis, etc.

-- ---------------------- Create a Database ------------------------j

-- We run a query
-- btw, sql keywords are case insensitive

CREATE DATABASE IF NOT EXISTS startersql;
USE startersql;

-- ----------------------- Drop Database ------------------------

DROP DATABASE IF EXISTS startersql;