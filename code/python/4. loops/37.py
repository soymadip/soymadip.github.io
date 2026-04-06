# dicts instead of repeated match case


from dis import disco

users = [
    {"id": 1, "total": 100, "cupon": "p20"},
    {"id": 2, "total": 100, "cupon": "p60"},
    {"id": 3, "total": 100, "cupon": "p50"},
]

discounts = {
    # name:  %, flat
    "p20": (0.2, 0),
    "p60": (0.6, 0),
    "p50": (0, 10),
}


for user in users:
    percent, flat = discounts.get(user["cupon"], (0, 0))
    discount_val = user["total"] * percent + flat

    print(
        f"User {user['id']} paid {user['total'] - discount_val} (Discount: {discount_val})"
    )
