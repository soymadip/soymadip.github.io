---
id: 19-sets
title: Sets
sidebar_label: Sets
sidebar_position: 19
description: "Concise revision notes for the built-in `set` type."
source_filename: "19 - sets.py"
---

# Sets

Sets are unordered collections of unique, hashable values. They are best for membership checks, deduplication, and simple set algebra.

:::tip
Use sets when order does not matter and duplicates must be removed automatically.
:::

## What to Remember

- Unordered collection of _unique_, _hashable_ items.
- Create an empty set with `set()` (not `{}` — that makes a dict).
- Membership (`x in s`) is average O(1).
- Elements must be hashable (e.g., `int`, `str`, `tuple`, `frozenset`).

## Operators & Short Examples

### Union

Combine all unique elements from two sets. Example: `A | B` or `A.union(B)`.

```python
primary_ingredients: set[str] = {"cardamom", "ginger"}
optional_ingredients: set[str] = {"ginger", "cloves"}
all_ingredients = primary_ingredients | optional_ingredients
print(all_ingredients)
```

### Intersection

Return elements common to both sets. Example: `A & B` or `A.intersection(B)`.

```python
primary_ingredients: set[str] = {"cardamom", "ginger"}
optional_ingredients: set[str] = {"ginger", "cloves"}
common_ingredients = primary_ingredients & optional_ingredients
print(common_ingredients)
```

```text
{'ginger'}
```

### Difference

Elements in A but not in B. Example: `A - B` or `A.difference(B)`.

```python
essential_spices: set[str] = {"cardamom", "ginger", "cinemon"}
optional_spices: set[str] = {"ginger"}
essential_only = essential_spices - optional_spices
print(essential_only)
```

### Symmetric Difference

Elements in either set but not both. Example: `A ^ B` or `A.symmetric_difference(B)`.

```python
a: set[str] = {"cardamom", "ginger"}
b: set[str] = {"ginger", "cloves"}
unique_to_each = a ^ b
print(unique_to_each)
```

### Add / Update

Mutate a set by adding elements.

- `s.add(x)` — add single item.
- `s.update(iterable)` — add multiple.

```python
spices: set[str] = {"pepper"}
spices.add("salt")
spices.update(["cumin", "turmeric"])
print(spices)
```

### Remove / Discard

- `s.remove(x)` raises `KeyError` if `x` missing.
- `s.discard(x)` does nothing if `x` missing — prefer when absence is normal.

```python
optional_spices: set[str] = {"cloves", "black_pepper"}
optional_spices.discard("nutmeg")
print(optional_spices)
```

### Pop / Clear

- `pop()` removes and returns an arbitrary element (raises if empty).
- `clear()` empties the set.

Real-world example: processing pending background tasks stored in a set. `pop()` can be used to take one arbitrary task to process (order doesn't matter); `clear()` can be used to reset the pending set.

```python
pending_tasks: set[str] = {"fix-bug-123", "write-unit-tests", "generate-report"}
claimed_task = pending_tasks.pop()
print(f"Working on: {claimed_task}")
pending_tasks.clear()
```

### Set Comprehension

Create sets concisely from iterables.

```python
spice_list: list[str] = ["cardamom", "ginger", "cloves"]
unique_lengths = {len(s) for s in spice_list}
print(unique_lengths)
```

### Immutable sets (`frozenset`)

Use `frozenset` when you need a hashable, immutable set-like object (e.g., dict key).

```python
important_spices = frozenset(["cardamom", "cinnamon", "cloves"])
```

### Practical Usage

- Use sets for deduplication, membership tests, and fast caching of seen values.
- Use `frozenset` when you need a set as a key in another dictionary or a member of another set.

:::tip

- Use `discard()` when missing elements are normal to avoid exceptions.
- Use `sorted(s)` for reproducible order when displaying or testing.
- Use set comprehensions for concise transforms.
- Use `frozenset` when you need immutability/hashability.
  :::
