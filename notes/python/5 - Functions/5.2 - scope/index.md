---
id: "functions-scope"
title: "Functions Scope"
description: "Mastering the LEGB scope rule and modifying variables across different levels."
source_filename:
  - 40 - Scope & named spaces.py
  - 41 - non global and global scope.py
---
# Functions Scope

In Python, understanding how variables are resolved (Scope) is key to writing clean, maintainable logic. The interpreter searches four levels to find a variable name, following the **LEGB** rule.

## What to Remember

- **Scope (LEGB):** Python looks for variables in order: **Local** → **Enclosing** → **Global** → **Built-in**.
- **Global vs Nonlocal:** Use `global` to modify top-level variables and `nonlocal` to modify variables in a parent (enclosing) function.
- By default, you can **read** outside variables, but you cannot **modify** them without keywords.

## The LEGB Scope Rule

Python's scope rules might feel broader if you are coming from C.

```python
x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(f"Inner: {x}") # Prints "Local"

    inner()
    print(f"Outer: {x}") # Prints "Enclosing"

outer()
print(f"Global: {x}") # Prints "Global"
```

**Output:**

```text
Inner: Local
Outer: Enclosing
Global: Global
```

## Modifying Outside Variables

To change a variable defined outside the current function's local scope, you must explicitly declare your intent.

### Global Keyword

Use `global` to modify a variable defined at the top level of the file.

```python
count = 0

def increment():
    global count  # Tells Python to use the top-level 'count'
    count += 1

increment()
print(f"Global count: {count}")
```

```text
Global count: 1
```

### Nonlocal Keyword

Use `nonlocal` to modify a variable in the parent (enclosing) function's scope.

```python
def parent():
    name = "Alice"
    def child():
        nonlocal name  # Targets the variable in 'parent' scope
        name = "Bob"
    child()
    print(f"Parent name: {name}")

parent()
```

```text
Parent name: Bob
```

---

_Source files: [40 - Scope & named spaces.py](../../../../src/code/python/5.%20Functions/40%20-%20Scope%20&%20named%20spaces.py), [41 - non global and global scope.py](../../../../src/code/python/5.%20Functions/41%20-%20non%20global%20and%20global%20scope.py)_
