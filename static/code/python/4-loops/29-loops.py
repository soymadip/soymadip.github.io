for token in range(10):  # 0 - 9 (so 10 numbers)
    print(f"Serving chai to Token #{token}")

for token in range(1, 11):  # 1 - 10 (limit -1) (so 10 numbers)
    print(f"Serving chai to Token #{token}")


# we can directly iterate over keys of a dict:

dct = {"key": 1, "key2": 2}

for key in dct:
    print(key)
