---
id: "functions-basics"
title: "Functions Basics"
description: "Understanding how to define, call, and return values from Python functions."
source_filename: "38 - Functions.py"
---

# Functions Basics

Functions are the building blocks of reusable code. They allow you to group logic together and call it whenever needed, preventing code duplication.

## What to Remember

- Use the `def` keyword to define a function.
- A function only runs when it is **called**.
- Parameters are variables in the definition; arguments are the values you pass in.
- Indentation is critical in Python to define the function body.

## Defining and Calling

In Python, you define a function with a colon and indentation.

```python
def greet_user(name):
    """Simple greeting function."""
    print(f"Hello, {name}!")

# Calling the function
greet_user("Alice")
```

**Output:**

```text
Hello, Alice!
```

---

_Source file: [38 - Functions.py](../../../../src/code/python/5-functions/38-functions.py)_
