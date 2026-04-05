---
id: 32-enumerate
title: "Enumerate and Zip"
sidebar_label: "Enumerate and Zip"
sidebar_position: 32
description: "Use `enumerate()` for indexes and `zip()` for parallel sequence iteration."
source_filename: ["32 - enumerate.py", "33 - zip.py"]
---

# Enumerate and Zip

## What to remember

- `enumerate()` adds a loop index to sequence items, returning `(index, value)`.
- `zip()` combines multiple sequences into one iterator of tuples.
- Both helpers support unpacking directly in the loop head.
- `zip()` stops at the shortest input iterable.
- Use `start=1` in `enumerate()` for human-friendly numbering.

## Enumerate: Add Indexing to a Loop

`enumerate(menu)` produces an iterable of tuples, which you can unpack into index and value.

```python
menu: list[str] = ["Green", "Blue", "Lemon"]
for idx, name in enumerate(menu, start=1):
    print(f"{idx}: {name}")
```

```text
1: Green
2: Blue
3: Lemon
```

## Zip: Parallel Sequence Iteration

Use `zip()` when you need to loop through two or more related collections at once without using manual index lookups.

```python
names: list[str] = ["hitesh", "sonaii", "ali"]
bills: list[int] = [50, 70, 100]

for name, amount in zip(names, bills):
    print(f"{name} paid: {amount}")
```

```text
hitesh paid: 50
sonaii paid: 70
ali paid: 100
```

## Comparing Enumerate and Zip

| Pattern       | Use Case                                          | Returns               |
| :------------ | :------------------------------------------------ | :-------------------- |
| **Enumerate** | When you need the item's **position** (index).    | `(index, item)`       |
| **Zip**       | When you have **related data** in separate lists. | `(item1, item2, ...)` |

:::warning Shortest Wins
If iterables have different lengths, `zip()` stops as soon as the shortest one is exhausted. Remaining items in the longer lists are ignored.
:::
