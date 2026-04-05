---
id: 28-while-loops
title: "While loops"
sidebar_label: "While loops"
sidebar_position: 28
description: "Repeat code until a condition changes and validate input with while loops."
source_filename: "28 - into-to-loops.py"
---

# While loops

What to remember

- `while` repeats until its condition becomes false.
- `while True` with `break` is a common retry loop pattern.
- Update loop variables inside the loop to avoid infinite repetition.
- Use `continue` to skip the rest of one iteration.

## Basic `while` repetition

`while` runs the same block until the condition is false.

```python
count: int = 1
while count <= 3:
    print(f"Check {count}")
    count += 1
```

```text
Check 1
Check 2
Check 3
```

## Keep asking until input is valid

A validation loop repeats until the user provides an allowed value.

```python
available_items: set[str] = {"samosa", "burger", "cookies"}
while True:
    snack: str = input("Enter snack: ").strip().lower()
    if snack in available_items:
        print("Good choice, we will be serving you that.")
        break
    print(f"Sorry, we don't have that. Available: {available_items}")
```

## When to use `break`

Use `break` when the loop should stop early after a successful validation.

:::tip
`while` is better than `for` when the number of repetitions depends on user input or a changing condition.
:::
