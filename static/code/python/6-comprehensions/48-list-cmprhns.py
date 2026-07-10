menu: list[str] = [
    "pizza",
    "hamburger",
    "sushi",
    "pasta",
    "iced tea",
    "Iced flavoured tea",
]

# var = [expression for item in iterable if condition
iced_tea: list = [item for item in menu if "tea" in item]

# we can do this too. Nice note, any str * 2 will concatenate the same str
double_tea: list[str] = [tea_name * 2 for tea_name in menu if len(tea_name) > 5]

print(iced_tea)
print(double_tea)


# examples:

lsit: list[int | str] = ["lsjfslj", 10]

# Generate all (x, y) pairs where x ∈ [1,5], y ∈ [1,5], and x != y.
ex05: list[tuple[int, int]] = [
    (x, y) for x in range(1, 6) for y in range(1, 6) if x != y
]


#  From a list of numbers, build a set of only the prime ones.
# A prime number is a number greater than 1 that Has exactly two factors — 1 and itself".
#  means nothing between 2 and num-1 can divide it, because if anything in that range divided it, it would be a third factor.
numbers_ex09: list[int] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ex09: set[int] = {
    num for num in numbers_ex09 if num > 1 and all(num % i != 0 for i in range(2, num))
}
