user_input: str = input(" What size of cup do you need?\n=> ").strip().lower()

if user_input == "small":
    print("price: 10")
elif user_input == "medium":
    print("price: 30")
elif user_input == "large":
    print("price: 50")
else:
    print("Unkonw cup size")
