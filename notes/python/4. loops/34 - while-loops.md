---
id: 34-while-loops
title: "While loops"
sidebar_label: "While loops"
sidebar_position: 34
description: "Repeat code until a condition changes and validate input with while loops."
source_filename: ["28 - into-to-loops.py", "34 - while loops.py"]
---

# While loops

## What to remember

- `while` repeats until its condition becomes false.
- `while True` with `break` is a common retry loop pattern.
- Update loop variables inside the loop to avoid infinite repetition.
- Use `continue` to skip the rest of one iteration.

## Basic `while` repetition

`while` runs the same block until the condition is false. Use this for simple counters or when you know the boundary condition.

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

## Validation Loops: Ask Until Valid

A common pattern for interactive programs is to loop until the user provides an allowed value. Use `while True` and `break` once a valid condition is met.

```python
available_items: set[str] = {"samosa", "burger", "cookies"}

while True:
    snack: str = input("Please enter your preferred snack: ").strip().lower()
    
    if snack in available_items:
        print("Good choice, we will be serving you that.")
        break
        
    print(f"Sorry we don't have that. Available: {available_items}\n")
```

## When to use `break` and `continue`

- `break` exits the loop entirely.
- `continue` skips the remaining code in the *current* iteration and jumps back to the condition check.

:::tip
Use `while` loops when you don't know in advance how many times you need to repeat—such as waiting for specific user input or a network response.
:::

