# ----- list.sort() --------
#
# sort() is a list method and sorts list IN-PLACE

import json

lst: list = [5, 68, 3, 56, 100, 34, 1, 0]

lst.sort()  # By default sorts from lowest value to highest value

print(lst)  # Original list changes: [0, 1, 3, 5, 34, 56, 68, 100]

lst.sort(reverse=True)  # We can pass reverse param to sort in reverse (higher to lower)

print(lst)  # [100, 68, 56, 34, 5, 3, 1, 0]


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

students = [
    {"name": "Charlie", "marks": 90},
    {"name": "Alice",   "marks": 90},
    {"name": "David",   "marks": 75},
    {"name": "Bob",     "marks": 75},
]

# sort by marks first if same comes then use name
students.sort(
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

numbers = [5, 2, 8, 1, 4]
new_numbers = sorted(numbers)

print(new_numbers)  # [1, 2, 4, 5, 8]
print(numbers)  # [5, 2, 8, 1, 4]

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


# sorting() takes similar props to .sort() and returns list
