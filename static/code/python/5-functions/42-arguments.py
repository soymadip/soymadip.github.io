"""
FUNCTION ARGUMENTS & PARAMETERS

Parameter:
    A variable written in the function definition.

Argument:
    A value supplied when calling the function.

Example:

    def prepare_chai(order):
                         ^^^^^
                         parameter


    prepare_chai("ginger chai")
                   ^^^^^^^^^^^
                   argument
"""


# ============================================================
# 1. BASIC PARAMETERS & ARGUMENTS
# ============================================================


def prepare_chai(order):
    print(f"Preparing: {order}")

prepare_chai("ginger chai")


# Parameters can receive arguments positionally or by keyword
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


# Positional arguments:
make_chai("Darjeeling", "milk", "low")

# Keyword arguments:
# Order doesn't matter when using parameter names.
make_chai(
    tea="green",
    sugar="medium",
    milk="no",
)


# We can also mix positional and keyword arguments.
# Positional arguments must come BEFORE keyword arguments.

make_chai("Darjeeling", milk="yes", sugar="low")

# ❌ Invalid:
make_chai(tea="Darjeeling", "milk", "low")


# ============================================================
# ARGUMENTS ARE OBJECT REFERENCES
# ============================================================

chai = [1, 2, 3]


def edit_chai(cup):
    cup[1] = 42


edit_chai(chai)

print(chai)
# [1, 42, 3]


# CHANGED:
# Python does NOT simply "pass a copy".
#
# The argument is passed as an object reference.
#
# `cup` and `chai` refer to the SAME list object:
#
#       chai ─────┐
#                 ▼
#              [1, 2, 3]
#                 ▲
#       cup ──────┘
#
# Therefore, mutating the object through `cup`
# is visible through `chai`.


# Reassigning the parameter is different:

def replace_chai(cup):
    cup = ["new", "chai"]


chai = [1, 2, 3]

replace_chai(chai)

print(chai)
# [1, 2, 3]

# `cup` was merely made to refer to a different object.
# The caller's variable `chai` was not changed.



# ============================================================
# POSITIONAL-ONLY, NORMAL, AND KEYWORD-ONLY PARAMETERS
# ============================================================

"""
Python allows us to control HOW parameters may be supplied.

    def func(a, b, /, c, d, *, e, f):
              ─────  ────  ─────
                │      │      │
                │      │      └── keyword-only
                │      │
                │      └── positional OR keyword
                │
                └── positional-only
"""


def example(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


# `a` and `b` are positional-only.
example(1, 2, 3, 4, e=5, f=6)

# ❌ Invalid:
# example(a=1, b=2, c=3, d=4, e=5, f=6)


# `c` and `d` can be positional OR keyword.
example(1, 2, c=3, d=4, e=5, f=6)


# `e` and `f` are keyword-only.
# They MUST be passed by name.

# ❌ Invalid:
# example(1, 2, 3, 4, 5, 6)

# ✅ Correct:
example(1, 2, 3, 4, e=5, f=6)


# ============================================================
# 4. KEYWORD-ONLY PARAMETERS WITH *
# ============================================================

# A bare `*` means:
#
#     everything after this must be passed by keyword.


def greet(name: str, *, loud: bool = False):
    if loud:
        print(f"HELLO {name.upper()}!")
    else:
        print(f"Hello {name}!")


greet("Alice", loud=True)
greet("Alice")

# ❌ Invalid:
# greet("Alice", True)


# This is useful when a function has optional configuration
# parameters because the call becomes self-documenting.


def backup(
    source,
    destination,
    *,
    overwrite=False,
    preserve_metadata=True,
): ...


backup(
    "project",
    "backup",
    overwrite=True,
    preserve_metadata=True,
)


# ============================================================
# 5. DEFAULT PARAMETERS
# ============================================================


def chai(type="lemon"):
    print(type)


chai()
# lemon

chai("ginger")
# ginger


# A default value is used when the caller doesn't provide
# that argument.


# Required parameter + default parameter:


def order_chai(tea, milk="yes", sugar="low"):
    print(tea, milk, sugar)


order_chai("Darjeeling")
# Darjeeling yes low

order_chai(
    "Green",
    sugar="medium",
)
# Green yes medium


# ============================================================
# 6. IMPORTANT: DEFAULT VALUES ARE CREATED ONCE
# ============================================================

# DON'T DO THIS for mutable defaults:


def chai_order(order=[]):

    order.append("Masala")
    return order


print(chai_order())
# ["Masala"]

print(chai_order())
# ["Masala", "Masala"]


# Why?
#
# The list [] is created ONCE when the function is defined:
#
#       function definition
#              │
#              ▼
#            []  ← one list
#              │
#       ┌──────┴──────┐
#       ▼             ▼
#    call 1         call 2
#       │             │
#       └──────┬──────┘
#              ▼
#        same list object


# ============================================================
# 7. CORRECT WAY TO HANDLE MUTABLE DEFAULTS
# ============================================================


def chai_order(order=None):
    if order is None:
        order = []

    order.append("Masala")
    return order


print(chai_order())
# ["Masala"]

print(chai_order())
# ["Masala"]


# Each call gets a NEW list.


# ============================================================
# 8. *args — VARIABLE NUMBER OF POSITIONAL ARGUMENTS
# ============================================================


def special_chai(*ingredients):
    print(ingredients)


special_chai(
    "cardamom",
    "ginger",
    "cinnamon",
)


# Output:
#
# ("cardamom", "ginger", "cinnamon")


# CHANGED:
# `*ingredients` receives the extra positional arguments
# as a TUPLE, NOT a list.


# Conceptually:
#
# special_chai("cardamom", "ginger", "cinnamon")
#
#                │
#                ▼
#
# ingredients = (
#     "cardamom",
#     "ginger",
#     "cinnamon",
# )


# ============================================================
# 9. **kwargs — VARIABLE NUMBER OF KEYWORD ARGUMENTS
# ============================================================


def special_chai(**extras):
    print(extras)


special_chai(
    sweetener="honey",
    foam="yes",
    temperature="hot",
)


# Output:
#
# {
#     "sweetener": "honey",
#     "foam": "yes",
#     "temperature": "hot",
# }


# `**extras` collects extra keyword arguments into a DICTIONARY.


# ============================================================
# 10. *args AND **kwargs TOGETHER
# ============================================================


def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

    for key, value in extras.items():
        print(f"Extra: {key}: {value}")


special_chai(
    "cardamom",
    "ginger",
    sweetener="honey",
    foam="yes",
)


# Output roughly:
#
# Ingredients: ("cardamom", "ginger")
# Extras: {"sweetener": "honey", "foam": "yes"}
#
# Extra: sweetener: honey
# Extra: foam: yes


# ============================================================
# 11. *args AND **kwargs — WHAT THEY ACTUALLY MEAN
# ============================================================

"""
*args
    Collects extra positional arguments.

    Type:
        tuple


**kwargs
    Collects extra keyword arguments.

    Type:
        dict


Example:

    func(1, 2, 3, name="Guddu", debug=True)

becomes conceptually:

    args = (1, 2, 3)

    kwargs = {
        "name": "Guddu",
        "debug": True,
    }
"""


# ============================================================
# 12. UNPACKING WITH *
# ============================================================


def add(a, b, c):
    return a + b + c


numbers = [10, 20, 30]

# Without unpacking:
add(10, 20, 30)

# With *:
add(*numbers)


# `*numbers` means:
#
#     take the iterable and unpack its elements
#     into positional arguments.
#
# Equivalent to:
#
#     add(
#         numbers[0],
#         numbers[1],
#         numbers[2],
#     )


# It works with ANY iterable:

numbers = (10, 20, 30)
add(*numbers)


numbers = (x for x in range(3))
add(*numbers)


# ============================================================
# 13. UNPACKING WITH **
# ============================================================


def connect(host, port, timeout):
    print(host, port, timeout)


config = {
    "host": "localhost",
    "port": 5432,
    "timeout": 10,
}


connect(**config)


# Equivalent to:
#
# connect(
#     host="localhost",
#     port=5432,
#     timeout=10,
# )


"""
*  → unpack an iterable into positional arguments

** → unpack a mapping into keyword arguments
"""


# ============================================================
# 14. *args / **kwargs CAN ALSO FORWARD ARGUMENTS
# ============================================================


def wrapper(*args, **kwargs):
    return some_function(
        *args,
        **kwargs,
    )


# This allows `wrapper()` to accept and forward
# arbitrary positional and keyword arguments.


# ============================================================
# 15. FUNCTIONS ARE OBJECTS
# ============================================================


def greet():
    print("Hello")


# Store the function object:
func = greet

func()
# Hello


# IMPORTANT:
#
# greet
#     → function object
#
# greet()
#     → CALL the function


# ============================================================
# 16. FUNCTIONS CAN BE PASSED AS ARGUMENTS
# ============================================================


def square(x):
    return x * x


def apply(func, value):
    return func(value)


result = apply(square, 5)

print(result)
# 25


# A function that accepts another function is called
# a HIGHER-ORDER FUNCTION.


# ============================================================
# 17. FUNCTIONS CAN RETURN FUNCTIONS
# ============================================================


def multiplier(factor):

    def multiply(value):
        return value * factor

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(10))
# 20

print(triple(10))
# 30


# `multiply()` remembers `factor`.
#
# This is called a CLOSURE.


# ============================================================
# 18. LAMBDA
# ============================================================

square = lambda x: x * x

print(square(5))
# 25


# Equivalent to:


def square(x):
    return x * x



# ============================================================
# 21. QUICK REFERENCE
# ============================================================

"""
FUNCTION DEFINITION
-------------------

def func(a, b, /, c=10, *args, d=20, **kwargs):
    ...


/       → everything before it is positional-only

*       → everything after it is keyword-only
          EXCEPT *args, when a name follows the *


*args   → extra positional arguments
          stored as tuple

**kwargs → extra keyword arguments
           stored as dict


FUNCTION CALL
-------------

func(1, 2)
    ↑  ↑
    positional arguments


func(a=1, b=2)
         ↑
         keyword arguments


func(*values)
    ↑
    unpack iterable into positional arguments


func(**config)
    ↑
    unpack mapping into keyword arguments
"""


# ============================================================
# 22. COMPLETE ARGUMENT MODEL
# ============================================================

"""
                    FUNCTION
                       │
                       ▼
                  PARAMETERS
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
    positional      normal      keyword-only
      only        parameters
          │            │            │
          ▼            ▼            ▼
         /          normal          *
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                  FUNCTION CALL
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
     positional     keyword      unpacking
      arguments     arguments
          │            │
          ▼            ▼
       *args        **kwargs
          │            │
          ▼            ▼
        tuple          dict
"""


# ============================================================
# 23. THE RULES TO REMEMBER
# ============================================================

"""
1. Parameters are in the function definition.
   Arguments are supplied when calling the function.

2. Python passes object references.
   It does NOT simply make a copy of every argument.

3. Mutating a passed mutable object affects the same object
   seen by the caller.

4. Reassigning a parameter does NOT reassign the caller's variable.

5. Positional arguments come before keyword arguments.

6. `/` makes parameters before it positional-only.

7. `*` makes parameters after it keyword-only.

8. `*args` collects extra positional arguments into a tuple.

9. `**kwargs` collects extra keyword arguments into a dictionary.

10. `*iterable` unpacks positional arguments.

11. `**mapping` unpacks keyword arguments.

12. Avoid mutable default arguments such as `[]` or `{}`.
    Use `None` and create the object inside the function.

13. Functions are objects.
    They can be stored, passed around, and returned.

14. A function accepting or returning another function is
    a higher-order function.

15. Closures allow an inner function to remember values from
    its enclosing scope.
"""
