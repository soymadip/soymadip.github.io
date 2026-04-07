---
id: 37-dictionary-dispatching
title: Dictionary Dispatching
sidebar_label: Dictionary Dispatching
sidebar_position: 37
description: "How to use dictionaries as a clean, efficient alternative to nested conditionals."
source_filename: "37.py"
---

# Dictionary Dispatching

## What to remember

- **Dispatching** is the process of deciding which code to run or value to use based on a key.
- Using a dictionary is often cleaner and more efficient than long `if/elif` or `match/case` blocks.
- It is particularly useful for configuration-driven logic where rules are mapped to specific identifiers.

## Comparison: Match-Case vs. Dictionary

When you have multiple cases that result in simple value lookups, a dictionary keeps the code dry and easy to update.

### Repetitive Match-Case

Using `match-case` for simple key-to-value mapping requires a new block for every case, which can become verbose.

```python
# Multiple cases for every discount code
match user["cupon"]:
    case "p20":
        percent, flat = (0.2, 0)
    case "p60":
        percent, flat = (0.6, 0)
    case "p50":
        percent, flat = (0, 10)
    case _:
        percent, flat = (0, 0)
```

### Clean Dictionary Dispatch

A dictionary collapses those branches into a single line using a lookup table.

```python
discounts = {"p20": (0.2, 0), "p60": (0.6, 0), "p50": (0, 10)}

# Collapses the entire match-case into one clean line
percent, flat = discounts.get(user["cupon"], (0, 0))
```

## Dispatching in Loops

You can map complex values (like tuples or dictionaries) and retrieve them inside a loop for bulk processing.

```python
# Map identifiers to rules (percent, flat_discount)
discounts = {
    "p20": (0.2, 0),
    "p60": (0.6, 0),
    "p50": (0, 10),
}

users = [
    {"id": 1, "total": 100, "cupon": "p20"},
    {"id": 2, "total": 100, "cupon": "p60"},
    {"id": 3, "total": 100, "cupon": "p50"},
]

for user in users:
    # Use .get() to provide a safe default (no discount)
    percent, flat = discounts.get(user["cupon"], (0, 0))
    
    # Calculate final price
    discount_val = user["total"] * percent + flat
    print(
        f"User {user['id']} paid {user['total'] - discount_val} (Discount: {discount_val})"
    )
```

```text
User 1 paid 80.0 (Discount: 20.0)
User 2 paid 40.0 (Discount: 60.0)
User 3 paid 90 (Discount: 10)
```

:::tip Code Maintainability
Adding a new rule is as simple as adding a key-value pair to the dictionary. The processing loop remains untouched.
:::

:::note
This pattern is often referred to as a **Lookup Table** or **Dispatch Table**.
:::
