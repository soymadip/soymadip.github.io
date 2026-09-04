-- ----------------- What is a database? ---------------------
--
-- A database is a container that stores related data in an organized way.
-- It allows for efficient retrieval, manipulation, and storage of data.

-- A DataBase is like a folder.
-- Each TABLE is a file in that folder
-- The ROWS in the table are like the content inside each file


-- --------------------- What is DBMS? ---------------------
--
-- A DBMS or Database Management System is a software application that allows users to create, manage, and interact with databases. It provides an interface for users to perform various operations on the data, such as querying, updating, and deleting records.
-- A DBMS ensures data integrity, security, and efficient data management.
-- Examples: PostgreSQL, MySQL, Oracle Database, Microsoft SQL Server, MongoDB, etc.


-- ----------------- What is query? ---------------------
--
-- A query is a request/command for data or information from a database.
-- It is typically written in a specific language, such as SQL (Structured Query Language), and allows users to retrieve, update, or manipulate data stored in the database.
-- Queries can be simple, retrieving specific records, or complex, involving multiple tables and conditions.
--
-- sql is all about writing efficient queries

-- We perform  CRUD operations using queries
-- C - Create
-- R - Read
-- U - Update
-- D - Delete


-- ------------- Relational vs Non-Relational Databases -----------------
--
-- Relational Databases (SQL):
-- Relational databases organize data into tables (also known as relations) with rows and columns.
-- Each table has a unique identifier called a primary key, and relationships between tables are established using foreign keys.
-- Examples: MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server.

-- Non-Relational Databases (NoSQL):
-- Non-relational databases, also known as NoSQL databases, store data in a more flexible and scalable way.
-- They do not use the traditional table-based structure of relational databases.
-- Examples: MongoDB, Cassandra, Redis, etc.
-- 


-- ---------------------- Database Structure ------------------------
--
-- A database is organized into tables, which consist of rows and columns.
--
-- Each table represents a specific entity or concept, and each row represents a record or instance of that entity.
--
-- Columns define the attributes or properties of the entity, and each column has a specific data type
-- that determines the kind of data it can hold (e.g., integer, string, date).

-- Rows tell about a specific instance of the entity, and each row contains values for the corresponding columns.


-- ---------------------- Create a Database ------------------------

-- We run a query
-- btw, sql keywords are case insensitive

-- Syntax:
-- CREATE DATABASE database_name;
CREATE DATABASE IF NOT EXISTS college;

-- If not using a db selected qpp, select the database
USE college;


-- ----------------------- Drop/Delete Database ------------------------

-- Syntax:
-- DROP DATABASE database_name;
DROP DATABASE IF EXISTS college;
