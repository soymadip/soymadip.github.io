---
id: for-loops
title: For Loops
sidebar_position: 1
description: "Iterating over sequences like range() and lists in Python."
source_filename: ["29 - loops.py", "31 - iterating-lists.py"]
---
# For Loops

Python does not use C-style `for(i=0; i<10; i++)` loops. Instead, its `for` loop acts as a "for-each" statement that iterates directly over the items of any sequence, such as a list or a `range`.

## What to Remember

- `for` iterates over any **iterable** object (lists, strings, ranges).
- `range(stop)` generates a sequence of numbers from `0` to `stop - 1`.
- Python lists can store mixed data types at runtime.
- Use direct iteration over items whenever possible; avoid using index counters unless necessary.

## Using `range()` for Repeats

When you need to repeat an action a specific number of times, use `range()`. It creates an immutable sequence of numbers on the fly.

```python
for i in range(1, 4):
    print(f"Iteration #{i}")
```

**Output:**

```text
Iteration #1
Iteration #2
Iteration #3
```

### Why `range()` Is Memory Efficient
Unlike a list, `range()` does not store all its numbers in memory at once. It generates each number only when the loop asks for it. This means `range(1_000_000)` uses the same tiny amount of memory as `range(10)`.

## Iterating Over Lists

You can loop through a list directly without needing to manage an index variable.

```python
tech_stack = ["Python", "C", "Bash"]

for language in tech_stack:
    print(f"Learning {language}...")
```

**Output:**

```text
Learning Python...
Learning C...
Learning Bash...
```

## Mixed Types at Runtime

Python is dynamically typed and doesn't enforce list element types at runtime. Even if you use a type hint like `list[str]`, you can still store integers or floats in that list without the interpreter stopping you.

```python
# Type hints are for developers and tools, not for the Python interpreter
mixed_list: list[str] = ["Aman", 101, 3.14]

for item in mixed_list:
    print(f"Item: {item} | Type: {type(item).__name__}")
```

**Output:**

```text
Item: Aman | Type: str
Item: 101 | Type: int
Item: 3.14 | Type: float
```

---

*Source files: 29 - loops.py, 31 - iterating-lists.py*
