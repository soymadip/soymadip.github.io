---
id: 1-functions-basics
title: Functions Basics
sidebar_label: Basics
sidebar_position: 1
description: "Understanding how to define, call, and return values from Python functions."
source_filename: 38 - Functions.py
---

# Functions Basics

Functions are the building blocks of reusable code. They allow you to group logic together and call it whenever needed, preventing code duplication.

## What to Remember

- Use the `def` keyword to define a function.
- A function only runs when it is **called**.
- Use `return` to send data back to the caller. If no return is specified, it returns `None`.
- Parameters are variables in the definition; arguments are the values you pass in.

## Defining and Calling

In Python, you define a function with a colon and indentation.

```python
def greet_user(name):
    """Simple greeting function."""
    print(f"Hello, {name}!")

# Calling the function
greet_user("Alice")
```

```text
Hello, Alice!
```

## Return Values

A function can perform a task (like printing) or calculate a value and send it back using `return`.

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print(result)
```

```text
15
```

---

_Source file: 38 - Functions.py_
