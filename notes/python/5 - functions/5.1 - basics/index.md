---
id: "functions-basics"
title: "Functions Basics"
description: "Understanding how to define, call, and return values from Python functions."
source_filename: "38 - Functions.py"
---

# Functions Basics

Functions are the building blocks of reusable code. They group logic together so we can call it whenever needed, preventing code duplication. A function only runs when it is **called**.

## Defining and Calling

Use the `def` keyword to define a function. Indentation is critical in Python to define the function body. Variables in the definition are called **parameters**, while the values we pass in are called **arguments**.

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

_Source file: [38 - Functions.py](/code/python/5-functions/38-functions.py)_
