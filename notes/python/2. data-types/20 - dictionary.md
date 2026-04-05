---
id: 20-dictionary
title: Dictionary
sidebar_label: Dictionary
sidebar_position: 20
description: "Compact reference for dictionaries: creation, access, update, and useful methods."
source_filename: "20 - dictionary.py"
---

# Dictionaries

Dictionaries map keys to values. They are ideal when you need fast lookup by a unique key and when order does not matter.

## What to Remember

- Keys must be hashable.
- Use `{}` or `dict()` to create dictionaries.
- Access with `d[key]` for required values.
- Use `.get(key, default)` to avoid `KeyError`.
- `update()` changes a dict in place; `|` creates a new merged dict.

## Create and Access Dictionaries

```python
recipe: dict[str, int | str] = {"type": "chai", "size": "medium", "price": 10}
print(recipe["type"])
print(recipe.get("flavor", "unknown"))
```

```text
chai
unknown
```

## Add and Update Entries

```python
recipe["milk"] = "whole"
recipe.update({"price": 15, "sugar": "yes"})
print(recipe)
```

## Update, Merge, and Intersection

- `update()` changes a dictionary in place and overwrites existing keys.
- The `|` operator creates a new merged dictionary without changing the originals.
- If the same key appears in both dictionaries, the right-hand dictionary wins.
- The `&` operator is not supported for dict intersection in all Python versions; use set operations on keys or dictionary comprehensions instead.

## Remove Entries Safely

```python
age = {"name": "John", "age": 32}
print(age.pop("age", None))
print(age)
```

## Iterate Dictionaries

```python
for key, value in recipe.items():
    print(key, value)
```

## Common Patterns

- Use `.get()` for safe lookup.
- Use `setdefault()` to ensure a key exists.
- Use dict comprehensions for transforms.

```python
counts: dict[str, int] = {}
for tag in ["bug", "feature", "bug"]:
    counts[tag] = counts.get(tag, 0) + 1
print(counts)
```

## Output

```text
{'bug': 2, 'feature': 1}
```

## When to Use Dictionaries

Use dictionaries for configuration, records, lookup tables, and any mapping where keys are unique.

:::tip
Use `sorted(d.items())` when you need deterministic output for tests or display.
:::
