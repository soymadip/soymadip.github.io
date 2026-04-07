---
id: 38-functions-basics-and-scope
title: "Functions: Basics, Scope, and Arguments"
sidebar_label: "Functions: Basics & Scope"
sidebar_position: 38
description: "A comprehensive guide to Python functions, including LEGB scope, *args/**kwargs, and mutable defaults."
source_filename:
  [
    "38 - Functions.py",
    "40 - Scope & named spaces.py",
    "41 - non global and global scope.py",
    "42 - arguments.py",
  ]
---

# Functions: Basics, Scope, and Arguments

## What to remember

- **Basics**: Use `def` to encapsulate reusable logic. Parameters are placeholders; arguments are actual values.
- **Scope (LEGB)**: Python resolves names in order: **Local** → **Enclosing** → **Global** → **Built-in**.
- **Modification Keywords**: Use `global` for top-level variables and `nonlocal` for variables in the parent function.
- **Flexible Arguments**: `*args` collects positional arguments into a **tuple**; `**kwargs` collects keyword arguments into a **dictionary**.
- **Mutable Default Trap**: Never use mutable objects (like `[]`) as default arguments; use `None` instead.

---

## 1. Defining and Calling Functions

Functions allow you to process different inputs with the same logic, facilitating the DRY (Don't Repeat Yourself) principle.

```python
def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai!")

print_order("Aman", "masala")
```

### Return Values vs. Printing

Using `return` allows a function to output a value that can be stored in a variable, whereas `print()` only displays it.

```python
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(2, 10)
```

---

## 2. Function Scope and the LEGB Rule

Python searches for variables starting from the innermost scope and moves outward.

```python
chai_order = "tulsi"  # Global

def chai_counter():
    chai_order = "lemon"  # Enclosing

    def print_order():
        chai_order = "ginger" # Local
        print(f"Inner: {chai_order}") # ginger

    print_order()
    print(f"Outer: {chai_order}") # lemon

chai_counter()
```

### Using `global` and `nonlocal`

Use these keywords when you need to _modify_ a variable outside the current local scope.

```python
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type # Targets parent function
        chai_type = "kesar"
    kitchen()

# Global modification
chai_type = "plain"
def front_desk():
    global chai_type # Targets top-level variable
    chai_type = "Irani"
```

---

## 3. Advanced Arguments: \*args and \*\*kwargs

Keyword arguments allow you to pass values without worrying about order, while `*args` and `**kwargs` provide maximum flexibility.

```python
def special_chai(*ingredients, **extras):
    # ingredients is a tuple: ('ginger', 'mint')
    # extras is a dict: {'sweetener': 'honey'}
    print(ingredients, extras)

special_chai("ginger", "mint", sweetener="honey")
```

### The Mutable Default Trap

Default arguments are evaluated only **once** at definition. If you use a list, that same list instance is reused across every call.

```python
# WRONG: List persists across calls
def add_to_order(item, order=[]):
    order.append(item)
    return order

# RIGHT: Initialize inside the function
def add_to_order_safe(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order
```

:::warning Safety First
Avoid overusing `global` as it creates hidden dependencies. Always prefer returning values from functions over modifying global state.
:::
