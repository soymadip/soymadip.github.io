# --- all() ---
# returns True if all elements in a given iterable (like a list, tuple, or set) are truthy.
# If even one element is falsy, it returns False

print(all([True, True]))  # True
print(all([True, False]))  # False

numbers: list = [2, 4, 6, 8, 10]

# Check if all numbers are even
print(all(num % 2 == 0 for num in numbers))  # Output: True
