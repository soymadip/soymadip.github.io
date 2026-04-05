"""
Generate Multiplication Table
You are developing a feature in an educational app that displays multiplication tables.

Tasks:

    Write a function named multiplication_table that takes a single integer argument number.

    Using a for loop and range(), generate the multiplication table for number from 1 to 10.

    Return a list of strings in the following format:

    "number x i = result"

    (Example: "3 x 4 = 12")
"""


# This function will be tested automatically.
# Do not change the function name or parameter type.
def multiplication_table(number: int) -> list[str]:
    num_list: list[str] = []
    for i in range(1, 11):
        num_list.append(f"{number} x {i} = {number * i}")

    return list(num_list)


print(multiplication_table(6))
