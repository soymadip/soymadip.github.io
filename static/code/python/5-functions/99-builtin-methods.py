# ========================================================
# Built-in Functions & Methods (Iterables & Higher-Order)
# ========================================================

# --- all() ---
# returns True if all elements in a given iterable (like a list, tuple, or set) are truthy.
# If even one element is falsy, it returns False

print(all([True, True]))  # True
print(all([True, False]))  # False

numbers: list = [2, 4, 6, 8, 10]

# Check if all numbers are even
print(all(num % 2 == 0 for num in numbers))  # Output: True


# --- any() ---
# returns True if any element in a given iterable (like a list, tuple, or set) is truthy.
# If all elements are falsy, it returns False

print(any([True, True]))  # True
print(any([True, False]))  # True
print(any([False, False]))  # False

numbers_any: list = [2, 4, 6, 8, 10]

# Check if any number is even
print(any(num % 2 == 0 for num in numbers_any))  # Output: True


# -- filter() --
# Constructs an iterator of the items from given iterable which given function returns True for.
# syntax: filter(func | lambda, iterable)
# It returns a filter object, an iterator (of type filter).
#    So we need to convert to list/tuple/set... to see all values when printing.

lst = [10, 12, 9, 35, 90]

evens = list(filter(lambda x: x % 2 == 0, lst))
# evens = [x for x in lst if x % 2 == 0] this is pythonic way, list comprehension

print(evens)


# -- map() --
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


# -- reduce() --
# Applies a function to a sequence and returns a single value.
# It is a part of the `functools` module in Python
# Returns only single value

from functools import reduce

gg = [1, 2, 3, 4, 5, 6]
sum_val = reduce(lambda x, y: x + y, gg)


print(f"sum is: {sum_val}")


# ----- list.sort() --------
#
# sort() is a list method and sorts list IN-PLACE

import json

lst_sort: list = [5, 68, 3, 56, 100, 34, 1, 0]

lst_sort.sort()  # By default sorts from lowest value to highest value

print(lst_sort)  # Original list changes: [0, 1, 3, 5, 34, 56, 68, 100]

lst_sort.sort(reverse=True)  # We can pass reverse param to sort in reverse (higher to lower)

print(lst_sort)  # [100, 68, 56, 34, 5, 3, 1, 0]


# Use the key parameter to tell Python what value to compare when sorting.
# key must be a callable (usually a function) that accepts one argument.
# Python calls key(element) for every element and sorts using the returned value.

words = ["apple", "kiwi", "Banana", "fig"]

words.sort(key=len)  # sort by each word's length

print(words)  # ['fig', 'kiwi', 'apple', 'Banana']


# compare strings ignoring uppercase
words.sort(key=lambda word: word.lower())  # lower the elements before comparing

print(words)  # ['apple', 'Banana', 'fig', 'kiwi']


# Sorting Dictionaries
#
students = [
    {"name": "Alice", "marks": 90},
    {"name": "Bob", "marks": 75},
    {"name": "Charlie", "marks": 85},
]

# sort with student with more marks at first
students.sort(key=lambda student: student["marks"], reverse=True)


print("\n" + json.dumps(students, indent=2))  # just pretty printing

# using join to print student name: marks in each line
print(
    "\n" + "\n".join(f"{student['name']}: {student['marks']}" for student in students)
)



# We can give multiple key too, so if first key comparision gives tie, .sort() uses 2nd one

students_tie = [
    {"name": "Charlie", "marks": 90},
    {"name": "Alice",   "marks": 90},
    {"name": "David",   "marks": 75},
    {"name": "Bob",     "marks": 75},
]

# sort by marks first if same comes then use name
students_tie.sort(
    key=lambda s: (s["marks"], s["name"])
)

# Charlie -> (90, "Charlie")
# Alice   -> (90, "Alice")
# David   -> (75, "David")
# Bob     -> (75, "Bob")
 
# Result: 
# [
#     {"name": "Bob",     "marks": 75},
#     {"name": "David",   "marks": 75},
#     {"name": "Alice",   "marks": 90},
#     {"name": "Charlie", "marks": 90},
# ]


print()

#
# ------- sorted() ----------
#
# sorted() is a builtin method that works in ANY ITERABLE
# it creates a new sorted LIST instead of changing the original

numbers_sorted = [5, 2, 8, 1, 4]
new_numbers = sorted(numbers_sorted)

print(new_numbers)  # [1, 2, 4, 5, 8]
print(numbers_sorted)  # [5, 2, 8, 1, 4]

# using tuple
nums: tuple = (4, 1, 7, 2)
result = sorted(nums)

print(result)  #  [1, 2, 4, 7]


# We can even use string
string = "python"

print(sorted(string))  # ['h', 'n', 'o', 'p', 't', 'y']

# Use ''.join() for joining the letters again
print(
    "".join(sorted(string, reverse=True))  # 'hnopty'
)


# sorted() takes similar props to .sort() and returns list


#
# ------- min() and max() ----------
#
# min() returns the smallest item in an iterable or the smallest of two or more arguments.
# max() returns the largest item in an iterable or the largest of two or more arguments.
# Both functions can take a `key` argument, similar to `sort()` and `sorted()`.

numbers_min_max = [10, 20, 5, 40, 30]

print(min(numbers_min_max))  # 5
print(max(numbers_min_max))  # 40

# Using key function
words_min_max = ["apple", "banana", "cherry", "date"]

# Shortest word
print(min(words_min_max, key=len))  # 'date'

# Longest word
print(max(words_min_max, key=len))  # 'banana'

# With dictionaries
students_min_max = [
    {"name": "Alice", "marks": 90},
    {"name": "Bob", "marks": 75},
    {"name": "Charlie", "marks": 85},
]

# Student with highest marks
best_student = max(students_min_max, key=lambda s: s["marks"])
print(f"Best student: {best_student['name']} with {best_student['marks']} marks")

# Student with lowest marks
worst_student = min(students_min_max, key=lambda s: s["marks"])
print(f"Worst student: {worst_student['name']} with {worst_student['marks']} marks")
