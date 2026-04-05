"""
You’re creating a menu price lookup system for a digital food ordering app using the match-case statement.
Tasks:
    Define a function get_item_price that takes a string input item.
    Use match-case to return the following based on the item name:

        "pizza" → "Price: 30 bucks"
        "burger" → "Price: 15 bucks"
        "pasta" → "Price: 20 bucks"
        "salad" → "Price: 10 bucks"
        Any other item → "Item not available"

    Make sure the item check is case-insensitive (e.g., “BURGER” or “burger” should both match).
"""


# This function will be tested automatically.
# Do not change the function name or parameter type.
def get_item_price(item: str) -> str:

    match item.lower().strip():
        case "pizza":
            return "Price: 30 bucks"
        case "burger":
            return "Price: 15 bucks"
        case "pasta":
            return "Price: 20 bucks"
        case "salad":
            return "Price: 10 bucks"
        case _:
            return "Item not available"
