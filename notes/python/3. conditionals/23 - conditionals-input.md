---
id: 23-conditionals-input
title: Conditionals & input
sidebar_label: Conditionals & input
sidebar_position: 23
description: "Python conditionals with user input, nested branches, and type conversion."
source_filename: ["23 - conditionals-input.py", "24 - chai-price-calc.py", "25 - nested-conditionals.py", "26 - delivery-fees-wager.py"]
---

# Conditionals & input

What to remember

- `input()` always returns a string; convert it before numeric use.
- Normalize text with `.strip().lower()` before comparing user input.
- Use `if` / `elif` / `else` for multi-way decisions.
- Use ternary expressions for simple one-line conditionals.
- Nest conditionals when one check depends on a previous result.

## Normalize Input and Branch by Text

```python
cup_size: str = input("What size of cup do you need?\n=> ").strip().lower()

if cup_size == "small":
    print("price: 10")
elif cup_size == "medium":
    print("price: 30")
elif cup_size == "large":
    print("price: 50")
else:
    print("Unknown cup size")
```

:::tip
Need to keep asking until the user provides a valid choice? Use a [validation loop](../4.%20loops/28-while-loops).
:::

## Nested Conditionals for Dependent Checks

```python
device_status: str = "active"
temperature: int = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline.")
```

## Convert Input to a Number Before Using It Numerically

Use `int()` or `float()` when you need numeric operations.

```python
order_amount: int = int(input("Enter order amount: "))
print(type(order_amount))
```

```text
<class 'int'>
```

## Use a Ternary Expression for Short Decisions

A ternary expression keeps a simple conditional in one line.

```python
order_amount: int = 320
delivery_fees: int = 0 if order_amount > 300 else 30
print(delivery_fees)
```

```text
0
```

## Why This Grouping Makes Sense

- Input normalization and conditional branches are common together.
- Nested checks are a direct extension of basic branching.
- Converting input to a number is the missing step before numeric comparisons.

