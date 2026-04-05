order_ammount: int = int(input("Enter order ammount: "))  # default input is str
print(type(order_ammount))  # str

# Ternary operator
delivery_fees: int = 0 if order_ammount > 300 else 30

# unary operator
# binary operator
