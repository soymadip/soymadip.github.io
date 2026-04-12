"""
Function Types

You're building a Function Behavior Analyzer to showcase different types of Python functions in action. Implement the following:

    Pure Function
        Write a function pure_add(a, b) that takes two integers and returns their sum.
        It should not rely on or modify any external state.

    Impure Function
        Define a global variable counter.
        Implement impure_increment() that increases the counter and returns its value.

    Recursive Function
        Implement factorial_recursive(n) that returns the factorial of a given number using recursion.
        Handle base case correctly (e.g., factorial_recursive(0) = 1).

    Lambda Function with map()

    Write a function square_list(nums) that uses a lambda inside map() to return a new list with the squares of the numbers in the input list.
"""


def pure_add(a, b):
    return a + b


counter: int = 0


def impure_increment(a, b):
    global counter
    counter += 1
    return counter


def factorial_recursive(n):
    if n == 0:
        return 1

    return n * factorial_recursive(n - 1)


def square_list(nums: list[int]) -> list[int]:
    return list(map(lambda num: num**2, nums))


def outer() -> int:
    count = 0

    def inner() -> int:
        nonlocal count
        count += 1
        return count

    return inner()


print(outer())
