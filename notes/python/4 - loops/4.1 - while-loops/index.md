---
id: "while-loops"
title: "While Loops"
description: "Repeating code until a condition changes and using validation loops."
source_filename:
  ["28 - into-to-loops.py", "34 - while loops.py", "23 - conditionals-input.py"]
---

# While Loops

A `while` loop repeats as long as a specific condition is **True**, making it ideal for situations where we don't know the iteration count in advance. Always ensure the loop condition eventually becomes **False** to avoid an infinite loop.

## Basic Repetition

`while` loops in Python work exactly as we'd expect. We can use `continue` to skip the rest of the current iteration and jump back to the condition check.

```python
count = 1
while count <= 3:
    print(f"Loop iteration: {count}")
    count += 1
```

**Output:**

```text
Loop iteration: 1
Loop iteration: 2
Loop iteration: 3
```

## Validation Loops: "Ask Until Valid"

A common **Pythonic** pattern is to use `while True` combined with `break` to loop forever until the user provides correct data.

```python
allowed_options = {"yes", "no", "maybe"}

while True:
    choice = input("Enter yes/no: ").strip().lower()

    if choice in allowed_options:
        print(f"We chose: {choice}")
        break  # Exit the loop entirely

    print(f"Invalid choice. Please choose from: {allowed_options}")
```

**Output:**

```text
Enter yes/no: okay
Invalid choice. Please choose from: {'maybe', 'no', 'yes'}
Enter yes/no: yes
We chose: yes
```

### Why Use `while True`?

Using `while True` with an internal `break` is often cleaner than initializing a dummy variable just to satisfy a condition. It keeps the "ask" logic and the "exit" logic clearly separated.

---

_Source files: [28 - into-to-loops.py](/code/python/4-loops/28-into-to-loops.py), [34 - while loops.py](/code/python/4-loops/34-while-loops.py), [23 - conditionals-input.py](/code/python/3-conditionals/23-conditionals-input.py)_
