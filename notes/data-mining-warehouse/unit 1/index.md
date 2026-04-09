---
id: unit-1
title: Unit 1
description: "Foundational definitions, features, and core architecture of Data Warehousing."
source_filename: "questions.pdf"
---

# Data Warehouse Basics

A **Data Warehouse (DW)** is a centralized system used to store large amounts of data from different sources for analysis and decision-making. It is optimized for reading and querying rather than day-to-day transactions.

## Key Features

- **Subject-Oriented:** Organized by subject (e.g., sales, customers) rather than by department or application.
- **Integrated:** Combines data from multiple sources (databases, flat files) into a consistent format.
- **Time-Variant:** Stores historical data (e.g., 5-10 years) to analyze trends over time.
- **Non-Volatile:** Data is stable and not frequently changed; once entered, it is read-only.

## Operational Database vs. Data Warehouse

| Feature       | Operational Database (OLTP)     | Data Warehouse (OLAP)      |
| :------------ | :------------------------------ | :------------------------- |
| **Purpose**   | Daily operations (transactions) | Analytical decision-making |
| **Data Type** | Current, up-to-date data        | Historical + Current data  |
| **Usage**     | Insert, update, delete          | Mainly read and analyze    |
| **Users**     | Clerks, applications            | Managers, data analysts    |
| **Speed**     | Fast transaction processing     | Fast query and reporting   |

## Data Warehouse Models

1.  **Enterprise Data Warehouse (EDW):** A centralized warehouse for the entire organization, storing data from all departments.
2.  **Data Mart:** A small part of the warehouse focused on a single department (e.g., Sales, HR). Faster to implement.
3.  **Virtual Warehouse:** A view of data from operational databases; not physically stored separately.

## Core Concepts

### Concept Hierarchies
A way of organizing data into different levels of detail (low level to high level).
- **Location:** City → State → Country
- **Time:** Day → Month → Year

### Fact and Dimension
- **Fact:** Numerical measurements (e.g., sales amount, quantity sold, profit).
- **Dimension:** Descriptive data that gives context (e.g., customer name, product, city, date).

## OLAP Operations
OLAP (Online Analytical Processing) uses multi-dimensional data models to perform complex queries and analysis.

1.  **Roll-Up (Summarize):** Moves from detailed data to a higher-level summary (e.g., Sales of Kolkata → West Bengal → India).
2.  **Drill-Down (Detailed View):** The opposite of roll-up; moves from summary to more detailed data (e.g., Sales of India → West Bengal → Kolkata).
3.  **Slice (One Dimension):** Selects one specific value from a dimension (e.g., Sales data for ONLY the year 2024).
4.  **Dice (Multiple Dimensions):** Selects multiple conditions (e.g., Sales for 2024 AND West Bengal AND Electronics).
5.  **Pivot (Rotate):** Changes the perspective of the data (rows become columns and vice versa).

## Steps in Designing and Implementing a DW

1.  **Requirement Analysis:** Understand business needs and goals.
2.  **Data Source Identification:** Identify where data comes from (databases, files, apps).
3.  **Data Design (Schema):** Choose a structure like Star or Snowflake.
4.  **ETL Process:** Extract, Transform, and Load data into the warehouse.
5.  **Data Storage:** Store processed data.
6.  **OLAP & Tools Setup:** Setup tools for reporting and dashboards.
7.  **Testing:** Verify the data and system performance.
8.  **Deployment & Maintenance:** Go-live and regular updates.

## Schema Models

### Star Schema
The simplest structure where one central **Fact Table** is connected to multiple **Dimension Tables**, forming a star shape. It is denormalized and optimized for fast queries.

### Snowflake Schema
An extension of the Star Schema where dimension tables are **normalized** (broken down into smaller sub-tables). This reduces redundancy but makes queries slower due to multiple joins.

### Galaxy Schema (Fact Constellation)
A complex design where multiple fact tables share common dimension tables. It looks like a collection of star schemas connected together. Used in large, enterprise-level systems with multiple business processes.

---

_Source file: questions.pdf_
