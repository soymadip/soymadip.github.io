def gen():
    x = yield 1  # pauses here, sends 1 out, and waits to receive a value
    print(f"got: {x}")
    yield 2


g = gen()


print(next(g))  # → 1  (runs until first yield, pauses)
print(g.send(42))  # → got: 42 \n 2  (resumes, x=42, runs until next yield)
