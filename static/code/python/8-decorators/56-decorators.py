"""
A decorator is a higher-order function that wraps another function.

It takes a function as input, executes code before and/or after calling that
function, and returns the wrapped function.
"""


def my_decorator(function):
    def wrapper():
        print("Before function print")
        function()
        print("After function print")

    return wrapper


@my_decorator  # This is same as my_decorator(greet)
def greet():
    print("greetings master!")


greet()


## but one problem.

print(greet.__name__)  ## gives wrapper instead of the greet.

# To fix this we use a stdlib method

from functools import wraps  # noqa: E402


def my_deco(func):
    @wraps(func)
    def wrapper():
        print("Before function print")
        func()
        print("After function print")

    return wrapper


print(greet.__name__)  ## gives  greet.
