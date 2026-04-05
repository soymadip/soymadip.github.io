---
id: 29-for-loops
title: For loops
sidebar_label: For loops
sidebar_position: 29
description: "Iterating over sequences like range() and lists in Python."
source_filename: ["29 - loops.py", "31 - iterating-lists.py"]
---

# For loops

## What to remember

- `for` iterates over any sequence, including `range` and `list`.
- `range(stop)` produces values from `0` to `stop - 1`.
- Python lists can hold mixed types; type hints are not enforced at runtime.
- `for` loops are ideal for repetitive, sequential tasks.

## Repeat Work With `range()`

`range()` produces a simple numeric sequence without creating a full list in memory.

```python
for token in range(1, 4):
    print(f"Serving chai to Token #{token}")
```

```text
Serving chai to Token #1
Serving chai to Token #2
Serving chai to Token #3
```

## Iterate Over Lists

A list iteration reads each element in the order it was defined.

```python
items: list[str | int] = ["aman", "google", 11, 11.5]
for item in items:
    print(item)
```

## Mixed Types and Runtime Behavior

Python is dynamically typed. Even if you use a type hint like `list[str]`, the interpreter will not stop you from adding or printing other types during execution.

```python
# The hint list[str | int] helps static analysis, but Python allows any type
mixed_data = ["data", 100, 3.14, True]
for val in mixed_data:
    print(f"Value: {val} | Type: {type(val).__name__}")
```

:::tip Performance Note
`range` values are generated lazily, making it memory-efficient even for very large sequences.
:::
