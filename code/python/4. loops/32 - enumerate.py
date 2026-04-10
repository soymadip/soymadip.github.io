menu: list[str] = ["Green", "Blue", "Lemon", "spiced", "Mint"]

# returns list of tuple, 2 set of values
print(list(enumerate(menu)))

# if one var is given, it stores the tuple in it. (e.g, (0, 'Green'))
for name in enumerate(menu):
    print(f"{name}")


# idx is index number, and name is the list item.
for idx, name in enumerate(menu):
    print(f"{idx}: {name}")

# we can also start number (index starts with 1 instead of 0)
for idx, name in enumerate(menu, start=1):
    print(f"{idx}: {name}")
