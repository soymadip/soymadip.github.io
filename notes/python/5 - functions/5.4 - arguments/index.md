---
id: "functions-arguments"
title: "Function Arguments"
description: "Mastering flexible argument patterns and avoiding common pitfalls with mutable defaults."
source_filename:
  - "42 - arguments.py"
---

# Function Arguments

In Python, lists and dictionaries are passed by **object reference**, meaning changes made to them inside a function affect the original object.

## Flexible Arguments (\*args and \*\*kwargs)

These allow our functions to accept any number of inputs.

- `*args` collects extra positional arguments into a **tuple**, while
- `**kwargs` collects keyword arguments into a **dictionary**.

```python
def build_profile(name, *skills, **details):
    print(f"Name: {name}")
    print(f"Skills (tuple): {skills}")
    print(f"Details (dict): {details}")
    for key, value in details.items():
        print(f"Extra Detail: {key}: {value}")

build_profile("Aman", "Python", "C", location="India", role="Dev")
```

**Output:**

```text
Name: Aman
Skills (tuple): ('Python', 'C')
Details (dict): {'location': 'India', 'role': 'Dev'}
Extra Detail: location: India
Extra Detail: role: Dev
```

:::note Order Matters
The standard order for arguments is: `positional`, `*args`, `keyword`, and then `**kwargs`.
:::

## The Mutable Default Trap

**Never use mutable objects like lists or dictionaries as default arguments.**  
In Python, these are created **once** when the function is defined, not every time it is called, meaning the same object is shared across all calls.

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

Use `None` as a placeholder and initialize the list inside the function logic.

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

_Source file: [42 - arguments.py](/code/python/5-functions/42-arguments.py)_
