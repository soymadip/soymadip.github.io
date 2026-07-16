# https://www.youtube.com/watch?v=xZtTIm3fpfA
# A Higher-Order Function in Python is a function that either
#  - Takes another function as an argument or
#  - Returns a function as a result.

# This is possible because, in Python, functions are first-class objects.
# Meaning they can be passed around just like integers, strings, or lists.
# This is a diff programming paradigm than oop called Functional programming

# Key characteristics and examples include:

#     Taking functions as arguments: Functions like map(), filter(), and sort(), sorted() apply a given function to elements of an iterable without explicit loops.
#                                    For instance, map(lambda x: x ** 2, [1, 2, 3]) squares each number in the list.


#     Returning functions: A higher-order function can define and return an inner function, often used to create closures or decorators that modify behavior dynamically.

#     Applications: They are fundamental to functional programming, enabling modular, reusable code through closures, decorators, and callbacks.

# So actually decorators?
# decorators(will study later), are syntactic sugar for higher-order functions.


# ------------ 1. Accepts a function  --------------------

# Func for upper a text
from typing import Callable


def shout(text) -> str:
    return text.upper()


# Func for lower a text
def quiet(text) -> str:
    return text.lower()


# Higher order function, accepts a function
def hello(
    func: Callable[[str], str],
) -> str:  # callable that takes a str and returns a str
    text: str = func("hello")  # so in runtime if passed 'quiet' it runs: quiet('hello')
    return text


print(hello(shout))  # HELLO
print(hello(quiet))  # hello


# ---------- 2. Returns a function ----------------------

# dividend / divisor =  quotient
# 10       /    2    =  5


def to_the_power(power: int) -> Callable[[int], int]:
    def result(num: int) -> int:
        return num**power

    return result


square: Callable[[int], int] = to_the_power(3)
quad: Callable[[int], int] = to_the_power(4)

print(f"square of 3 is: {square(3)}")  # 3^3 = 27
print(f"Quad of 3 is: {quad(3)}")  # 3^4 = 81


# Commonly used in-built higher order functions are discused in builtin-methods file
