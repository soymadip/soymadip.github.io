---
id: "break-continue-and-else"
title: "Break, Continue, and Else"
description: "Control loop flow and use loop-else for search fallback logic."
source_filename: "35 - break, continue, skip.py"
---

# Break, Continue, and Else

In Python, we can precisely control loop behavior using `break` to exit immediately and `continue` to skip the rest of the current iteration. Python also features a unique `else` clause for loops.

## Using `break` and `continue`

Use these to manage how our program handles specific items during iteration.

```python
stock = {"Ginger": "out", "Lemon": "in-stock", "Mint": "discontinued"}

while True:
    choice = input("Enter flavor: ").strip().capitalize()
    status = stock.get(choice, "not-available")

    if status == "in-stock":
        print(f"Adding {choice} to our order.")
        break  # We found what we need, stop asking

    if status == "out":
        print("Sorry, we're out of that. Pick another.")
        continue  # Skip to the next iteration immediately

    print("Flavor not recognized.")
```

**Output:**

```text
Enter flavor: Ginger
Sorry, we're out of that. Pick another.
Enter flavor: Apple
Flavor not recognized.
Enter flavor: Lemon
Adding Lemon to our order.
```

## Nested Loop Control

If we're using nested loops, `break` and `continue` only apply to the **innermost** loop they are in.

### Breaking the Inner Loop

```python
# Type hint: a list containing lists of integers
matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5

for row in matrix:
    found = False

    for item in row:
        if item == target:
            print(f"Found {target}!")
            found = True
            break  # This only breaks the INNER loop (item in row)

    if found:
        print("Stopping the search.")
        break  # This breaks the OUTER loop (row in matrix)
```

**Output:**

```text
Found 5!
Stopping the search.
```

## The Loop `else` Clause

The `else` block runs **only if the loop finished naturally** (without hitting a `break`). It is ideal for "search and find" logic to handle fallback cases when no match was found.

```python
candidates = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in candidates:
    if age >= 18:
        print(f"{name} is eligible.")
        break
else:
    # This runs ONLY if the 'break' above was never triggered
    print("No eligible candidates found in the entire list.")
```

**Output:**

```text
No eligible candidates found in the entire list.
```

### Why Use Loop `else`?

It is cleaner and more idiomatic than managing a manual boolean flag. It tells the reader: "If the loop finishes its work without finding what it's looking for, do this fallback action."

<SrcPv href="/code/python/4-loops/35-break,-continue,-skip.py" label="35 - break, continue, skip.py" />
