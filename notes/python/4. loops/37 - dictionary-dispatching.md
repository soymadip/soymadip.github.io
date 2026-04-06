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

## Why Use Dictionaries for Logic?

When you have multiple cases that result in simple value lookups, a dictionary keeps the code dry and easy to update.

Instead of this:
```python
if cupon == "p20":
    percent = 0.2
elif cupon == "p60":
    percent = 0.6
else:
    percent = 0
```

Use this:
```python
discounts = {"p20": 0.2, "p60": 0.6}
percent = discounts.get(cupon, 0)
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
]

for user in users:
    # Use .get() to provide a safe default (no discount)
    percent, flat = discounts.get(user["cupon"], (0, 0))
    
    # Calculate final price
    discount_val = user["total"] * percent + flat
    print(f"User {user['id']} paid {user['total'] - discount_val} (Discount: {discount_val})")
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
