# Dictionary

chai_recipe: dict = {"type": "Chay", "size": "Medium", "price": "10"}

# print(chai_recipe.keys())
# print(chai_recipe.values())
# print(chai_recipe["type"])

# popped_item = chai_recipe.pop("type")
# last_item = chai_recipe.popitem()

# chai_recipe.update(
#     {"price": "lsjflsj", "gos": "slfj"}
# )  # Updates and adds if not found?


# print(chai_recipe.get("goog", "not there"))  # if not available, print default.
# print(chai_recipe["goog"])  # crashes


# Set operations work too.
scnd_dict: dict = {"size": "gogl", "num": "ums"}

# # Union
# print(chai_recipe | scnd_dict)  # updated the value of size from second?

# # intersection
# print(chai_recipe & scnd_dict)  # doesn't work?


# ------------------------- Exercise ---------------------------
# Step 1: Create a customer dictionary with name, age, and city
customer: dict[str, str | int] = {"name": "John Doe", "age": 32, "city": "New York"}

# Step 2: Add email and phone
customer.update({"email": "john@johndoe.me", "phone": 9836997456})
print(customer)

# Step 3: Print customer's name and city
print(customer["name"])
print(customer["city"])

# Step 4: Check if "email" exists
print("email" in customer)

# Step 5: Delete the "age" field
customer.pop("age")
print(customer)

# Step 6: Print all keys, values, and items
print(customer.keys)
print(customer.values)
print(customer.items)

# Step 7: Remove and print the last inserted item
print(customer.popitem)

# Step 8: Use .get() to access "membership"
print(customer.get("membership", "no membership"))

# Step 9: Update dictionary with "address"
customer.update({"address": "221B Baker Street"})
print(customer)

# Step 10: Print final dictionary
print(customer)
