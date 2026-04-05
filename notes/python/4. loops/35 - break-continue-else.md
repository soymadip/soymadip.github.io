---
id: 35-break-continue-else
title: "Break, Continue, and Else"
sidebar_label: "Break, Continue, and Else"
sidebar_position: 35
description: "Control loop flow with break and continue, and use for-else/while-else for fallback logic."
source_filename: "35 - break, continue, skip.py"
---

# Break, Continue, and Else

## What to remember

- `break` exits the loop entirely.
- `continue` skips the rest of the current iteration.
- `else` in a loop executes **only if the loop finishes without hitting a `break`**.
- This pattern is ideal for "search and find" scenarios where you need a fallback if nothing is found.

## Control Flow with `break` and `continue`

Use these to fine-tune exactly when a loop should stop or skip work.

```python
stock: dict[str, str] = {"Ginger": "out", "Lemon": "discontinued", "Tulsi": "in-stock"}

while True:
    req: str = input("Flavour: ").strip().capitalize()
    status: str = stock.get(req, "missing").lower()

    if status == "in-stock":
        print("Serving soon!")
        break  # Found it, stop the loop
    elif status == "out":
        print("Out of stock. Choose another.")
        continue  # Skip to next iteration
    else:
        print("Not available.")
```

## Loop `else` Clauses

A loop's `else` block runs only when the loop completes its full cycle. If the loop is terminated by a `break`, the `else` is skipped.

```python
staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage.")
        break
else:
    # This runs ONLY if no one in the list was >= 18
    print("No one is eligible for managing.")
```

:::tip Indentation level
The `else` must be at the same indentation level as the `for` or `while` keyword, not the `if` inside the loop.
:::

:::note Why use Loop Else?
Without it, you usually need a flag variable like `found = False`. Using `else` is cleaner and more idiomatic Python.
:::
