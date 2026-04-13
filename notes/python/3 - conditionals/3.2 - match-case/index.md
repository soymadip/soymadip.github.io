---
id: "match-case"
title: "Match-Case"
description: "Pattern matching with Python's match-case statement for cleaner multi-way decisions."
source_filename: "27 - match-case.py"
---

# Match-case

Introduced in Python 3.10, `match-case` is a powerful alternative to long `if/elif/else` chains. It evaluates an expression and compares it against multiple `case` patterns, checking them in order from top to bottom.

## Basic Pattern Matching

Use `match-case` for menu-driven logic where a variable can have several distinct literal values. It is much more readable than `if/elif` when branching based on a **single expression**.

```python
seat_type = "ac"

match seat_type:
    case "sleeper":
        print("Sleeper: No AC, but has beds.")
    case "ac":
        print("AC: Climate controlled.")
    case "general":
        print("General: Budget seating.")
    case _:
        print("Unknown seat type.")
```

```text
AC: Climate controlled.
```

## The Wildcard Pattern

The underscore `_` is a special pattern that matches anything. It acts as the mandatory "wildcard" or fallback if nothing else matches, preventing our logic from falling through silently.


<SourcePreview path="/code/python/3-conditionals/27-match-case.py" label="27 - match-case.py" />
