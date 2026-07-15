# -- reduce() --
# Applies a function to a sequence and returns a single value.
# It is a part of the `functools` module in Python
# Returns only single value

from functools import reduce

gg = [1, 2, 3, 4, 5, 6]
sum = reduce(lambda x, y: x + y, gg)


print(f"sum is: {sum}")
