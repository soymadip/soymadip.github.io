"""
generators are functions that behave like iterators
They:
    pause a function, returns a value, then resumes.
    Iterate without loading everything into memory (ex. reading large files)
    return = Pouring bucket
    yield = drip faucet
"""


# # without yield, normal function
# def count_num(num: int) -> list[int]:

#     lst: list[int] = []  # This will create new list everytime?

#     for i in range(1, num + 1):
#         lst.append(i)

#     return lst


# # if we give 100000000, we get MemoreExcided error
# print(count_num(int(input("entre a number:"))))


# -------------------------------------------

from typing import Generator


# Now we will make generator,
# Generator will transmit the values live when needed.
def count_num_fast(num: int) -> Generator[int]:
    for i in range(1, num + 1):
        yield i


# # if we give 100000000, dont get error
# for i in count_num_fast(int(input("Enter a number: "))):
#     print(i)


# next keyword
# The next keyword prints the value one by one each call

counts = count_num_fast(4)

print(next(counts))  # 1
print(next(counts))  # 2
print(next(counts))  # 3
print(next(counts))  # 4
print(next(counts))  # will give error
