"""
we can handle multiple errors with multiple except block
"""


def process_order(item: str, quantity: int):
    try:
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be int")
        if not isinstance(item, str):
            raise TypeError("Item must be a stking")

        price = {"masala": 20}[item]
        cost = price * quantity

        print(f"total const is: {cost}")

    except KeyError:
        print("KeyError: Sorry chai is not on menu")

    except TypeError:
        print("Error: Quantity must be a number")


process_order("ginger", 2)      # raises KeyError
process_order("masala", "two")  # raises TypeError
