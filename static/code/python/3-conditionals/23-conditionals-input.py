available_itms: list[str] = ["samosa", "burger", "cookies"]




while True:
    user_snack: str = input("Please enter your perffered snack: ").lower().strip()
    print()

    if user_snack in available_itms:
        print("Good choice, we will be serving you that.")
        break
    else:
        print("Sorry we dont have that.")
        print(f"Available items: {available_itms}\n")
        continue
