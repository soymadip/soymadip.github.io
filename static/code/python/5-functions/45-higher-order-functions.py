# https://www.youtube.com/watch?v=xZtTIm3fpfA
# A Higher-Order Function in Python is a function that either
#  - Takes another function as an argument or
#  - Returns a function as a result.

# This is possible because, in Python, functions are first-class objects.
# Meaning they can be passed around just like integers, strings, or lists.
# This is a diff programming paradigm than oop called Functional programming

# Key characteristics and examples include:

#     Taking functions as arguments: Functions like map(), filter(), and sorted() apply a given function to elements of an iterable without explicit loops.
#                                    For instance, map(lambda x: x ** 2, [1, 2, 3]) squares each number in the list.


#     Returning functions: A higher-order function can define and return an inner function, often used to create closures or decorators that modify behavior dynamically.

#     Applications: They are fundamental to functional programming, enabling modular, reusable code through closures, decorators, and callbacks.

# So actually decorators?
# decorators(will study later), are syntactic sugar for higher-order functions.


# -------------------------------- 1. Accepts a function

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


# -------------------------------- 2. Returns a function

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


# -------------------- Commonly used higher order functions -------------

# -------------------- map()
# Applies a specific function to every item in an iterable and returns an iterator.
# map() returns a map object, an iterator (of type map). Why? because of efficiency. Iterator calculates next value when asked. ALSO, THIS IS ONE TIME USE
# We need to convert to list to see all values when printing.

lists = [1, 2, 3]
mapobj = map(lambda x: x**3, lists)
mlist = list(mapobj)

print(mlist)

# Remember that an iterator (like your mpobj) is a one-way stream. Once you "consume" it, it's empty.
# What happened in your code:
#     print(list(mpobj)): When you wrapped mpobj in list(), you told Python to pull every single value out of the iterator to build that list.
#     The Exhaustion: By the time that line finished, the mpobj iterator had reached the end of the data. It "remembered" that it had no more items left.
#     The Loop: When the for loop started, it asked mpobj for the next value. mpobj essentially replied, "I'm already finished," so the loop body never executed.


# -------------------- filter()
# Constructs an iterator of the items from given iterable which given function returns True for.
# syntax: filter(func | lambda, iterable)
# It returns a filter object, an iterator (of type filter).
#    So we need to convert to list/tuple/set... to see all values when printing.

lst = [10, 12, 9, 35, 90]

evens = list(filter(lambda x: x % 2 == 0, lst))
# evens = [x for x in lst if x % 2 == 0] this is pythonic way, list comprehension

print(evens)


# ------------------------------- reduce()
# Applies a function to a sequence and returns a single value.
# It is a part of the `functools` module in Python
# Returns only single value

from functools import reduce

gg = [1, 2, 3, 4, 5, 6]
sum = reduce(lambda x, y: x + y, gg)


print(f"sum is: {sum}")
