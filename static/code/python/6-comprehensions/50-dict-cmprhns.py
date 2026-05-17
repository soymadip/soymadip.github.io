# Dict and set comprehensions both use curly braces.
# The only diff is how we are storing.
# - If we are just storing a value, it's set
# - If we are sotring Key:value pair, it's dict


tea_price_inr = {"Masalla Chai": 10, "Green Chai": 50}

tea_dollar = {key: val / 80 for key, val in tea_price_inr.items()}


# In print this returns entire dict structure.
# In loop only name gives keys
print(tea_dollar)

# example:


# Build a dict where keys are numbers 1–10 and values are
#     their **factor lists**  →  {1: [1], 2: [1,2], 3: [1,3], 6: [1,2,3,6], ...}
ex16: dict[int, list[int]] = {
    num: [i for i in range(1, num + 1) if num % i == 0] for num in range(1, 11)
}
