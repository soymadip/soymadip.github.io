def infinite_chai():
    count = 1

    while True:
        yield count
        count += 1


refill = infinite_chai()

for _ in range(10):
    print(next(refill))
