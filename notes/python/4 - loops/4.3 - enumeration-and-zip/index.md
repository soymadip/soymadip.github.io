---
id: "enumerate-and-zip"
title: "Enumerate and Zip"
description: "Parallel and indexed iteration using Python's built-in helpers."
source_filename: ["32 - enumerate.py", "33 - zip.py"]
---

# Enumerate and Zip

If you are coming from C, you might be tempted to use a counter variable or `range(len(list))` to access indices. In Python, we use `enumerate()` and `zip()` to handle these common iteration patterns more cleanly.

## What to Remember

- `enumerate()` adds a counter to an iterable, returning `(index, item)`.
- `zip()` pairs up elements from multiple iterables, returning tuples.
- Both functions return **iterators**, meaning they are memory efficient.
- `zip()` stops at the shortest input iterable.

## Enumerate: Iterating with an Index

Use `enumerate()` when you need the value _and_ its position in the list.

```python
tech_stack = ["Python", "C", "Bash"]

# start=1 makes the index start at 1 instead of 0
for idx, name in enumerate(tech_stack, start=1):
    print(f"{idx}. {name}")
```

**Output:**

```text
1. Python
2. C
3. Bash
```

### Why Not Use `range(len())`?

Writing `for i in range(len(list)): print(list[i])` is considered an anti-pattern in Python. It's slower, more verbose, and prone to errors. `enumerate()` is the "Pythonic" way to get indices.

## Zip: Parallel Iteration

Use `zip()` when you have related data stored in two or more separate lists.

```python
users = ["Alice", "Bob", "Charlie"]
roles = ["Admin", "Editor", "Guest"]

for name, role in zip(users, roles):
    print(f"{name} is an {role}")
```

**Output:**

```text
Alice is an Admin
Bob is an Editor
Charlie is an Guest
```

### The "shortest Wins" Rule

If your lists are different lengths, `zip()` will silently stop as soon as the shortest list is exhausted.

```python
list_a = [1, 2, 3]
list_b = ["A", "B"]

# This only loops twice
for num, char in zip(list_a, list_b):
    print(num, char)
```

**Output:**

```text
1 A
2 B
```

---

_Source files: [32 - enumerate.py](/code/python/4.%20loops/32%20-%20enumerate.py), [33 - zip.py](/code/python/4.%20loops/33%20-%20zip.py)_
