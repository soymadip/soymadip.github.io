---
id: unit-2
title: Unit 2
description: "Introduction to Data Mining, KDD process, and core mining tasks (predictive and descriptive)."
---

# Data Mining Introduction

**Data Mining** is the process of extracting hidden, valid, and actionable patterns from large datasets. It is often referred to as **Knowledge Discovery in Databases (KDD)**.

## The KDD Process

The KDD process consists of several iterative steps to transform raw data into useful knowledge:

1.  **Data Cleaning:** Removing noise and inconsistent data.
2.  **Data Integration:** Combining data from multiple sources (databases, files).
3.  **Data Selection:** Choosing relevant data for the analysis task.
4.  **Data Transformation:** Converting data into appropriate forms for mining (e.g., normalization).
5.  **Data Mining:** Applying intelligent methods to extract patterns.
6.  **Pattern Evaluation:** Identifying truly interesting patterns based on knowledge measures.
7.  **Knowledge Presentation:** Visualizing and presenting the mined knowledge to the user.

## Data Mining Tasks

Data mining tasks are generally divided into two categories:

### 1. Descriptive Tasks
These tasks characterize the general properties of the data in the database.
- **Clustering:** Grouping similar data points together without predefined labels (unsupervised learning).
- **Association Rule Mining:** Finding interesting relationships between variables (e.g., Market Basket Analysis: "People who buy bread also buy butter").
- **Summarization:** Providing a compact description of the dataset.

### 2. Predictive Tasks
These tasks perform inference on the current data to make predictions about future or unknown values.
- **Classification:** Predicting the class label of new data based on a training set (supervised learning).
- **Regression:** Predicting continuous numeric values (e.g., predicting the price of a house or tomorrow's temperature).
- **Time-Series Analysis:** Analyzing data points indexed in time order to identify trends.

## Key Concepts

- **Outliers:** Data points that deviate significantly from the rest of the dataset. Often treated as noise but can be useful for fraud detection.
- **Decision Trees:** A flow-chart-like structure used for classification and regression, consisting of nodes (decisions) and branches (outcomes).
- **Ethics & Privacy:** Data mining raises concerns about the misuse of personal data and the need for privacy-preserving techniques.

## Data Mining Trends

- **Multimedia Data Mining:** Mining patterns from non-textual data like images, audio, and video.
- **Web Mining:** Extracting useful information from the web (content, structure, and usage).
- **Spatial Data Mining:** Mining data with geographical or location components.
