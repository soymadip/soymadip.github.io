---
id: exercise-19-student-grading-system
title: "Exercise 19: Student grading system"
sidebar_position: 1
description: "Practice nested function calls and return-based grading logic."
source_filename: "38.5 - Execise 19.py"
---

# Ex 19: Student Grading System

## Problem

Build an academic grading system that calculates a student's grade based on their score and generates a formatted report.

## Rules

- Define `calculate_grade(score: int | float) -> str`.
- Define `generate_student_report(name: str, score: int | float) -> str`.
- Ensure the name is properly capitalized in the final report.

## Boilerplate
Copy below code and paste to your IDE for head start.

```python
# Write your code inside this function
def calculate_grade(score: int | float) -> str:
    pass # remove this

def generate_student_report(name: str, score: int | float) -> str:
    pass # remove this

# Call with test data
print(generate_student_report("aman", 80))
```

## Expected Output
```python
Aman has scored 80 and received grade B
```

## Solution

Only view the solution after trying your best.

<details>
<summary>Show solution</summary>

```python
def calculate_grade(score: int | float) -> str:
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

def generate_student_report(name: str, score: int | float) -> str:
    # Capitalize name and call the grade function
    grade = calculate_grade(score)
    return f"{name.title()} has scored {score} and received grade {grade}"

# Test data
print(generate_student_report("aman", 80))
```

### Details
Breaking down complex tasks into smaller, specialized functions (like separating grading from reporting) is a fundamental practice in clean coding. It makes your code easier to test and maintain.

</details>

---

*Source file: 38.5 - Execise 19.py*
