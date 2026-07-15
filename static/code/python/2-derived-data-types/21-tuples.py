"""A tuple is an ordered, immutable collection of objects.

- Ordered
- Can store different data types
- Allows duplicates
- Cannot be modified after creation (immutable)

"""

empty_tuple: tuple = ()

this_is_not_tuple = 4  # this is int

# we use () for creating tuple. also notice the types. we need to exactly define what is where
person: tuple[str, int, str] = ("Alice", 20, "India")

# unless we use ...
person_2: tuple[str | list | int, ...] = ("Alice", 20, "India", ["gol"])

# we dont even need parenthesis for creating tuple
another: tuple = 10, 12, "soymadip"

# Accessing tuple elements, just like list
print(person[1])  # 20

# Negative Index works too
print(person[-1])  # India

# Slicing works too
print(person[1:])  # (20, "India")


# But we can't modify tuple
# person[0] = 100  # TypeError: 'tuple' object does not support item assignment

# Practical use of immutability
birthday: tuple[int, ...] = (
    15,
    7,
    2005,
)  # This shouldn't change throughout the program


## Unpacking

name, age, country = person

# or store rest in last var AS LIST
name, *rest_of_person = person  # name = "Alice", rest = [20, "India"]

print(rest_of_person)


## Tuples comprehension

# similar to list comprehension
squares: tuple[int, ...] = tuple(
    x**2 for x in range(5)
)  # why not directly ()? () gives generator

print(squares)  # (0, 1, 4, 9, 16)


## Returning multiple values
def get_person() -> tuple[str, int, str]:
    print("doing something...")
    print("doing something more..")

    return "Alice", 20, "India"  # same as ("Alice", 20, "India")


name, age, country = get_person()

print(f"name: {name}, age: {age}, country: {country}")


## Membership works too
print("Alice" in person)  # True


# --------- Tuple Methods ---------
#
# Tuple only has two methods: count() and index()

tple: tuple[int, ...] = (1, 2, 3, 4, 5, 1, 2, 3)


# count('element') returns number of occurrences of 'element'
print(tple.count(1))  # 2

# index('element') returns index of first occurrence of 'element'
print(tple.index(3))  # 2


# -------- Comparison --------------

# Tuples are compared lexicographically (comparing elements one by one)

print((1, 5, 90) < (1, 3, 4))  # False, because 5 > 3 (second element comparison)


# ------ getting unique values in tuple -----------------

# If we dont need to preserve order
unique_values: tuple[int, ...] = tuple(set(tple))

print(unique_values)  # (1, 2, 3, 4, 5)

# If we need to preserve order, use comprehension
unique_values_preserving_order: tuple[int, ...] = tuple(dict.fromkeys(tple))

print(unique_values_preserving_order)


# -------------- conversion from dict -----------------

dictionary = {"name": "soymadip", "age": 32, "city": "New York"}

# values are dropped
print(tuple(dictionary))  # ('name', 'age', 'city')
