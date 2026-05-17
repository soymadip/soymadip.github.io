"""
In Python, every if statement needs to evaluate to either True or False.
But Python doesn't require you to pass an actual boolean — it will convert whatever you give it to a boolean internally.
That conversion is called truthiness.

Ex:
    if 1:
        print("yes")  # prints — Python converted 1 → True internally

You can see what any value converts to using bool()

So when we write:
    if some_value:
        ...

Python is doing:
    if bool(some_value) == True:
        ...

**Falsy values in Python (everything else is truthy):**

    False
    None
    0          # zero int
    0.0        # zero float
    ""         # empty string
    []         # empty list
    {}         # empty dict
    set()      # empty set
    ()         # empty tuple


------------- Note --------------

`==` is completely separate — it checks if two things are equal, no conversion happens:

    1 == True     # True  — because bool(1) is True and Python considers them equal
    2 == True     # False — 2 is truthy but it doesn't equal True
    "hi" == True  # False — "hi" is truthy but doesn't equal True



=========== So the mental model is: ===========

if x: → asks "is x truthy?" → almost everything passes except 0, None, "", [] etc.
if x == True: → asks "does x literally equal True?" → only True and 1 pass


=================== all() ====================
all() takes an iterable and returns True if every element is truthy, False if any one is falsy.

all([True, True, True])   # True
all([True, False, True])  # False — one False kills it

With a generator expression:
all(num % i != 0 for i in range(2, num))

This generates True/False for each i, and all() returns True only if every single check passed — meaning no i divided num evenly.
For num=7:
    7 % 2 != 0  → True
    7 % 3 != 0  → True
    7 % 4 != 0  → True
    7 % 5 != 0  → True
    7 % 6 != 0  → True
    all(...)    → True  ✓ prime

"""
