names: list[str] = ["hitesh", "sonaii", "ali"]
bills: list[int] = [50, 70, 100]

# Use zip to iterate over several iterables in parallel
# Each iteration returns a tuple of elements
for item in zip(names, bills):
    print(item)

# Unpack the tuple into separate variables for cleaner access
for name, amount in zip(names, bills):
    print(f"{name} paid: {amount}")

# Note: enumerate() adds an index to ONE iterable, 
# while zip() pairs elements from MULTIPLE iterables.
