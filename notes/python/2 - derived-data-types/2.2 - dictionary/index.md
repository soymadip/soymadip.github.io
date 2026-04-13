---
id: "dictionaries"
title: "Dictionaries"
description: "Hash maps optimized for fast lookups, now with insertion order."
source_filename: "20 - dictionary.py"
---

# Dictionaries

Dictionaries are used to store data as key-value pairs. They are like a real-world dictionary where we look up a word (the key) to find its definition (the value). Keys must be **immutable** (strings, integers, tuples), while values can be anything.

## Creating and Accessing Dictionaries

Dictionaries are **O(1) fast** for lookups and insertions. Since Python 3.7, they **keep the order** in which we add items.

```python
# Type hinting: specify Key and Value types inside dict[]
# See: [Modern Python Types](../../1 - basics/1.9 - modern-python-types.md) for details
car: dict[str, str | int] = {"brand": "Tesla", "model": "S", "year": 2022}

# Grabbing a value by its key
print(car["brand"])
```

**Output:**

```text
Tesla
```

### The .get() Trick

If we try to access a key that doesn't exist (like `car["color"]`), Python will crash with a `KeyError`. Using `.get()` is safer because it returns `None` (or a default fallback) instead of crashing.

```python
# Safe way to look up a key
print(car.get("color"))

# We can even provide a default fallback
print(car.get("color", "Not Available"))
```

```text
None
Not Available
```

## Modifying Dictionaries

Dictionaries are **mutable**, so we can add, change, or remove items on the fly.

```python
# Adding or changing items
car["color"] = "Red"
car.update({"year": 2024}) # Updates existing or adds if not found

# Removing items
# pop() removes and returns the value
popped_year = car.pop("year")

print(car)
print(popped_year)
```

```text
{'brand': 'Tesla', 'model': 'S', 'color': 'Red'}
2024
```

## Merging Dictionaries (Python 3.9+)

Instead of using `update()`, which changes the original dictionary, we can use the `|` (merge) operator to create a brand-new one. The right-side value wins if there's a collision (the second dictionary's value overrides the first).

```python
A = {"x": 1, "y": 2}
B = {"y": 3, "z": 4}

print(A | B)
```

```text
{'x': 1, 'y': 3, 'z': 4}
```

:::note Bitwise AND
Unlike sets, dictionaries do not support the bitwise AND (`&`) operator directly. To find common keys, we would need to intersect the sets of their keys: `a.keys() & b.keys()`.
:::

## Worth Mentioning: Initialization and Bulk Creation

- `setdefault()`: Returns the value of a key if it exists; if not, inserts the key with a specified value. Great for initializing nested structures.
- `fromkeys()`: Creates a new dictionary with keys from a collection and a single value for all.
- `clear()`: Removes all items from the dictionary.

```python
# setdefault: helpful for counters
counts = {"apples": 10}
counts.setdefault("oranges", 0) # Adds oranges with 0
counts.setdefault("apples", 0)  # Does nothing (apples exists)

# fromkeys: bulk creation
users = dict.fromkeys(["alice", "bob", "charlie"], "standard")

print(counts)
print(users)

# Worth noting: .items() returns a view object (dict_items)
# which is an iterable of (key, value) tuples.
print(users.items())
```

**Output:**

```text
{'apples': 10, 'oranges': 0}
{'alice': 'standard', 'bob': 'standard', 'charlie': 'standard'}
dict_items([('alice', 'standard'), ('bob', 'standard'), ('charlie', 'standard')])
```

<SourcePreview path="/code/python/2-derived-data-types/20-dictionary.py" label="20 - dictionary.py" />
