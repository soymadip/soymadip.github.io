def chai_customers():
    print("Welcome! What chai would you like?")
    order = yield
    while True:
        print(f"Preparing {order}")
        order = yield


stall = chai_customers()

next(stall)  # start the generator. Equivalent to stall.send(None)

stall.send("Masala Chai")
stall.send("Lemon chai")
