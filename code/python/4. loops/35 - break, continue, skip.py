stock: dict[str, str] = {"Ginger": "out", "Lemon": "discontinued", "Tulsi": "in-stock"}


while True:
    req_flvr: str = input("Please specify your requested flavour: ").lower().strip()

    status: str = stock[req_flvr].lower()

    match status:
        case "in-stock":
            print("Great! will serving you soon.")
            break
        case "out":
            print("Sorry, this is out of stock.\nPlease choose another flavour.")
            continue
        case "discontinued":
            print("Sorry, this flavour is discontinued")
            break
        case _:
            print("Sorry, we dont have this flavour.\nPlease choose another flavour.")
            continue


# For/while  - else
staff: list[tuple[str, int]] = [("Amit", 16), ("zara", 17), ("raj", 15)]

# NOTE THAT ELSE IF IN INDENTATION LEVEL OF FOR
# else only prints if loop doesn't break. use it for fallback logic.
# Also works for while loop
for name, age in staff:
    if age >= 18:
        print(f"{name} is eligble to manage the staff.")
        break
else:
    print("No one is eliglbe for managing")


# Nested loop break, continue
