"""
Smart Inventory Filter

You are building a Smart Inventory Filter for a retail store.

Tasks:

    Process a list of product dictionaries, where each product has name, price, and category.

    Use different types of comprehensions to:

        Extract names of products priced below ₹500 using list comprehension.

        Extract all unique categories using set comprehension.

        Create a name-to-price mapping using dictionary comprehension.

        Generate a list of discounted prices using a generator expression and convert it to a list.

    Return all four outputs as a tuple.


"""

# This function will be tested automatically.
# Do not change the function name or parameters.

"""
    items: A list of dictionaries, each representing a product with keys:
        - "name": str
        - "price": int
        - "category": str

    Returns:
        - List of names of affordable products (price < 500)
        - Set of unique categories
        - Dictionary of product name to price mapping
        - Generator expression converted to list of prices after applying 10% discount
"""

items = [
    {"name": "Notebook", "price": 250, "category": "Stationery"},
    {"name": "Pen", "price": 100, "category": "Stationery"},
    {"name": "Bag", "price": 1200, "category": "Accessories"},
    {"name": "Bottle", "price": 400, "category": "Utensils"},
]


def filter_inventory(
    items: list[dict],
) -> tuple[list[str], set[str], dict[str, int], list[int]]:

    prod_names: list[str] = [prod["name"] for prod in items if prod['price'] < 500]
    prod_categories: set[str] = {prod["category"] for prod in items}
    name_price_dict = {prod["name"]: prod["price"] for prod in items}
    discounted_price: list[int] = [int(prod["price"] * 0.9) for prod in items]

    return (prod_names, prod_categories, name_price_dict, discounted_price)
