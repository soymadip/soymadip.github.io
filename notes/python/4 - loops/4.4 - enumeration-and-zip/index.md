---
id: "enumerate-and-zip"
title: "Enumerate and Zip"
description: "Parallel and indexed iteration using Python's built-in helpers."
source_filename: ["32 - enumerate.py", "33 - zip.py"]
---

# Enumerate and Zip

If we are coming from C, we might be tempted to use a counter variable or `range(len(list))` to access indices. In Python, we use `enumerate()` and `zip()` to handle these patterns more cleanly. Both functions return **iterators**, making them memory efficient.

## Enumerate: Iterating with an Index

`enumerate()` adds a counter to an iterable, returning `(index, item)`. Use it when we need the value _and_ its position in the list.

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

`zip()` pairs up elements from multiple iterables, returning tuples. Use it when we have related data stored in separate lists.

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

### The "Shortest Wins" Rule

`zip()` will silently stop as soon as the shortest input iterable is exhausted.

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

<SrcPv sources={[
  { path: "/code/python/4-loops/32-enumerate.py", label: "32 - enumerate.py" },
  { path: "/code/python/4-loops/33-zip.py", label: "33 - zip.py" }
]} />
