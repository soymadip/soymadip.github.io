# --- any() ---
# returns True if any element in a given iterable (like a list, tuple, or set) is truthy.
# If all elements are falsy, it returns False

print(any([True, True]))  # True
print(any([True, False]))  # True
print(any([False, False]))  # False

numbers: list = [2, 4, 6, 8, 10]

# Check if any number is even
print(any(num % 2 == 0 for num in numbers))  # Output: True