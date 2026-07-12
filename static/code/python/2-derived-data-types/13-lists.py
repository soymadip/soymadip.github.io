# Lists are ordered collection.
# Index starts from 0


lst: list = ["me", "my_bou", "my_gf"]

lst2: list[int] = [1, 2, 3, 4, 5]


# appending items
lst2.append(5)


# concatenating
lst += lst2

print(lst)  # ['me', 'my_bou', 'my_gf', 1, 2, 3, 4, 5, 5]
