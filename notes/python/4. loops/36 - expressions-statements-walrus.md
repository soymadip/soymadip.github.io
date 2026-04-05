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

```python
# Without walrus:
data = input("Enter something: ")
if len(data) > 0:
    print(f"You typed {len(data)} characters.")

# With walrus:
if (n := len(input("Enter something: "))) > 0:
    print(f"You typed {n} characters.")
```

:::warning Readability
While the walrus operator can make code more compact, overusing it can make logic harder to follow. Use it when it clarifies the intent by reducing repetition.
:::

:::note Compatibility
The walrus operator was introduced in **Python 3.8**. Ensure your environment supports it before using it in production code.
:::
