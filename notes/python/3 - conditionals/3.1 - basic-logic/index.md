---
id: "conditionals-and-input"
title: "Conditionals and Input"
description: "Handling multi-way decisions, nested branches, and input normalization."
source_filename:
  [
    "23 - conditionals-input.py",
    "24 - chai-price-calc.py",
    "25 - nested-conditionals.py",
    "26 - delivery-fees-wager.py",
  ]
---
# Conditionals and Input

Conditionals allow your program to make decisions. In Python, we use `if`, `elif`, and `else` to control the flow of execution based on specific conditions.

## What to Remember

- Use `.strip().lower()` to normalize user input before comparing it.
- `if` / `elif` / `else` handles multiple branches; only the first true branch runs.
- **Ternary Operators** allow for simple one-line `if/else` assignments.
- Nesting `if` statements is useful for checks that depend on a previous result.

## Normalizing Input

When accepting text from a user, always clean it up first. This prevents bugs caused by extra spaces or unexpected capitalization.

```python
# Assuming user enters " Medium "
user_input = input("Choose a size (Small/Medium/Large): ").strip().lower()

if user_input == "small":
    price = 10
elif user_input == "medium":
    price = 30
else:
    price = 50

print(f"Price: {price}")
```

```text
Choose a size (Small/Medium/Large):  Medium
Price: 30
```

:::tip
For repeating a prompt until the user gives a valid answer, see [Validation Loops](../../4 - loops/4.1 - while-loops/index.md).
:::

## Nested Conditionals

Use nested `if` statements when the second check only matters if the first one passed.

```python
device_status = "active"
temp = 38

if device_status == "active":
    if temp > 35:
        print("Warning: High temperature!")
    else:
        print("Temperature is normal")
else:
    print("System is offline.")
```

```text
Warning: High temperature!
```

## The Ternary Operator

For simple assignments, a one-line ternary expression is more Pythonic than a full `if/else` block. It reads almost like an English sentence.

```python
order_total = 320

# format: [value_if_true] if [condition] else [value_if_false]
delivery_fee = 0 if order_total > 300 else 30

print(f"Delivery fee: {delivery_fee}")
```

```text
Delivery fee: 0
```

## Converting Types for Comparisons

Remember that `input()` always returns a string. If you need to compare it against a number, you must cast it first.

```python
# Assuming user enters "20"
age = int(input("Enter your age: "))
if age >= 18:
    print("Access granted.")
```

```text
Enter your age: 20
Access granted.
```

---

_Source files: [23 - conditionals-input.py](../../../../src/code/python/3.%20conditionals/23%20-%20conditionals-input.py), [24 - chai-price-calc.py](../../../../src/code/python/3.%20conditionals/24%20-%20chai-price-calc.py), [25 - nested-conditionals.py](../../../../src/code/python/3.%20conditionals/25%20-%20nested-conditionals.py), [26 - delivery-fees-wager.py](../../../../src/code/python/3.%20conditionals/26%20-%20delivery-fees-wager.py)_
