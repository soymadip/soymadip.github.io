---
id: "for-loops"
title: "For Loops"
description: "Iterating over sequences with range and lists in Python."
source_filename: ["29 - loops.py", "31 - iterating-lists.py"]
---

# For Loops

In Python, a `for` loop is used to iterate over a sequence (like a list, string, or range). Python lists can store mixed data types at runtime, making iteration very flexible.

## Using `range()` for Repeats

When we need to repeat an action a specific number of times, use `range()`. It creates an immutable sequence of numbers on the fly. It is memory efficient because it generates each number only when the loop asks for it.

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

Unlike a list, `range()` does not store all its numbers in memory at once. Generating `range(1_000_000)` uses the same tiny amount of memory as `range(10)`.

## Iterating Over Lists

We can loop through a list directly without needing to manage an index variable. This is more readable and less prone to errors than index-based counters.

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

Python is dynamically typed and doesn't enforce list element types at runtime. Even if we use a type hint like `list[str]`, we can still store integers or floats in that list without the interpreter stopping we.

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

<SourcePreview sources={[
  { path: "/code/python/4-loops/29-loops.py", label: "29 - loops.py" },
  { path: "/code/python/4-loops/31-iterating-lists.py", label: "31 - iterating-lists.py" }
]} />
