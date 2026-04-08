---
id: functions-arguments
title: Function Arguments
sidebar_position: "5.3"
description: "Mastering flexible argument patterns and avoiding common pitfalls with mutable defaults."
source_filename:
    - "42 - arguments.py"
---
# Function Arguments

Python offers powerful ways to handle functions that take a varying number of inputs. Understanding how to collect and pass arguments efficiently is a key intermediate skill.

## What to Remember

- **Flexible Arguments:** `*args` collects extra positional arguments into a **tuple**, while `**kwargs` collects keyword arguments into a **dictionary**.
- **Mutable Default Trap:** Never use mutable objects (like `[]`) as default arguments. Use `None` instead.
- **Order Matters:** The standard order is: `positional`, `*args`, `keyword`, `**kwargs`.

## Flexible Arguments (\*args and \*\*kwargs)

These allow your functions to be extremely flexible by accepting any number of inputs.

```python
def build_profile(name, *skills, **details):
    print(f"Name: {name}")
    print(f"Skills (tuple): {skills}")
    print(f"Details (dict): {details}")

build_profile("Aman", "Python", "C", location="India", role="Dev")
```

**Output:**

```text
Name: Aman
Skills (tuple): ('Python', 'C')
Details (dict): {'location': 'India', 'role': 'Dev'}
```

## The Mutable Default Trap

A common mistake is using a list or dictionary as a default argument. In Python, these are created **once** when the function is defined, not every time it's called.

```python
# Anti-pattern: The same list is shared across all calls!
def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("Apple"))
print(add_item("Banana")) # Oops! Shared list
```

```text
['Apple']
['Apple', 'Banana']
```

### The Pythonic Fix

Use `None` as a placeholder and initialize the list inside the function.

```python
def add_item_safe(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item_safe("Apple"))
print(add_item_safe("Banana")) # New list each time
```

```text
['Apple']
['Banana']
```

---

_Source file: 42 - arguments.py_
