---
id: 29-for-loops
title: For loops
sidebar_label: For loops
sidebar_position: 29
description: "Using `for` with `range()` to repeat work in Python."
source_filename: "29 - loops.py"
---

# For loops

## What to remember

- `for` iterates over any sequence, including `range`.
- `range(stop)` produces values from `0` to `stop - 1`.
- `range(start, stop)` begins at `start` and ends before `stop`.
- `for` loops are ideal for repetitive, sequential tasks.

## Repeat Work With `range()`

`range()` produces a simple numeric sequence without creating a full list first.

```python
for token in range(1, 4):
    print(f"Serving chai to Token #{token}")
```

## Example Output

```text
Serving chai to Token #1
Serving chai to Token #2
Serving chai to Token #3
```

## Sequence Variants

`range()` can also include a step.

```python
for token in range(0, 6, 2):
    token: int
    print(token)
```

```text
0
2
4
```

:::tip Performance Note
`range` values are generated lazily, so large sequences are memory-efficient.
:::

## Why `range` Is Useful

- `range` generates values lazily for efficient loops.
- `for` loops keep repeated actions concise.
- The sequence can be adapted with start, stop, and step values.
