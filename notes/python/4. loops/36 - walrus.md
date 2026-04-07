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
3 + 3 
```

## The Walrus Operator (`:=`)

The walrus operator (officially known as the Assignment Expression) lets you assign and return a value in one step.

### Reducing Redundant Checks

Instead of assigning a variable and then checking it, you can do both at once.

```python
# without walrus operator
remainder = 13 % 5
if remainder:
    print("not devisible by 5")

# with walrus
if remainder := 13 % 5:
    print("not divisible by 5")
```

```text
not devisible by 5
not divisible by 5
```

### Simplifying Logic

It is highly effective when you need to fetch a configuration value or environment variable and immediately check if it exists before using it.

```python
import os

class config:
    server_username = ""

    def write_output(self, name: str) -> type[str]:
        return str

dsd_config = config()
plugin_utils = config()

# without walrus
def set_server_username():
    username = os.environ.get("DO_DJANGO_USER")
    if username:
        # Use this custom username.
        dsd_config.server_username = username
        plugin_utils.write_output(f"  username: {username}")
        return

# with walrus operator
def set_server_username2():
    if username := os.environ.get("DO_DJANGO_USER"):
        # Use this custom username.
        dsd_config.server_username = username
        plugin_utils.write_output(f"  username: {username}")
        return
```

### Efficient While Loops

Use the walrus operator to update a condition variable directly in the `while` header.

```python
flavours: list[str] = ["mint", "lemon", "mirch"]

# Loop until the user provides an empty string
while user_flav := input("choose your flavour: ").strip().lower():
    print(f"sorry we dont have {user_flav}")

print(f"you choose: {user_flav}")
```

```text
choose your flavour: mango
sorry we dont have mango
choose your flavour: 
you choose: 
```

:::warning Readability
While the walrus operator can make code more compact, overusing it can make logic harder to follow. Use it when it clarifies the intent by reducing repetition.
:::

:::note Compatibility
The walrus operator was introduced in **Python 3.8**. Ensure your environment supports it before using it in production code.
:::
