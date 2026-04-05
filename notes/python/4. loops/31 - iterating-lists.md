---
id: 31-iterating-lists
title: "Iterating lists"
sidebar_label: "Iterating lists"
sidebar_position: 31
description: "Loop over list elements and understand runtime behavior for mixed-type lists."
source_filename: "31 - iterating-lists.py"
---

# Iterating lists

What to remember

- `for item in list` reads each element in order.
- A Python list can hold mixed types at runtime.
- Type hints are optional and not enforced when the code runs.
- Use list iteration for sequential processing of values.

## Loop over a list

```python
items: list[str | int] = ["aman", "google", 11, 11.5, "slfjslj"]
for item in items:
    print(item)
```

```text
aman
google
11
11.5
slfjslj
```

## Why Python doesn’t enforce list element types at runtime

The source code asks whether Python forces types at runtime. It does not: the `list[str | int]` hint is only for static tools, not the interpreter.

```python
items: list[str | int] = ["aman", "google", 11, 11.5, "slfjslj"]
```

At runtime, Python stores each item as a value and prints it one by one. That makes lists flexible, but a consistent element type is easier to reason about.
