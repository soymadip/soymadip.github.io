---
id: 36-expressions-statements-walrus
title: "Expressions, Statements, and Walrus"
sidebar_label: "Expressions, Statements, and Walrus"
sidebar_position: 36
description: "Understand the difference between statements and expressions, and use the walrus operator (:=)."
source_filename: "36 - walrs.py"
---

# Expressions, Statements, and Walrus

## What to remember

- A **Statement** performs an action but does not return a value (e.g., `x = 5`).
- An **Expression** evaluates to a value (e.g., `3 + 3`).
- The **Walrus Operator (`:=`)** allows you to assign a value to a variable **inside** an expression.
- Use the walrus operator to reduce redundant function calls or variable assignments in loops and conditionals.

## Statements vs. Expressions

Most code in Python consists of either statements or expressions.

```python
# Statement: Assigns 5 to x, but the line itself has no value.
x = 5 

# Expression: Evaluates to 6.
result = 3 + 3 
```

## The Walrus Operator (`:=`)

The walrus operator (officially known as the Assignment Expression) lets you assign and return a value in one step.

### Reducing Redundant Checks

Instead of assigning a variable and then checking it, you can do both at once.

```python
# With walrus:
if (n := len(input("Enter something: "))) > 0:
    print(f"You typed {n} characters.")

# In complex conditionals
import os
if username := os.environ.get("USER_NAME"):
    print(f"Found username: {username}")
```

### Efficient While Loops

Use the walrus operator to update a condition variable directly in the `while` header.

```python
# Loop until the user provides an empty string
while user_input := input("Next flavour (blank to stop): ").strip().lower():
    print(f"Adding {user_input} to the list...")
```

:::warning Readability
While the walrus operator can make code more compact, overusing it can make logic harder to follow. Use it when it clarifies the intent by reducing repetition.
:::

:::note Compatibility
The walrus operator was introduced in **Python 3.8**. Ensure your environment supports it before using it in production code.
:::
