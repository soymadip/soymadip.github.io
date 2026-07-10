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


# Enumerate with both key, value of dict:
stock = {"masala": 20, "adrak": 30, "ginger": 4}

for i, (key, value) in enumerate(stock.items(), start=1):  # We need to use (key,value) because dict.items() returns tuple. python automatically unpacks it
    print(f"{i}. {key}: {value}")


# Btw we can bypass unpacking too:
for both in stock.items():
    print(both)  # Output: ('masala', 10)