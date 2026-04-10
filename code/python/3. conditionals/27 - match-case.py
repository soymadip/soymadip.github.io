seat_type: str = (
    input("what kind of seats do you choose? (sleeper/ac/general/luxary): ")
    .lower()
    .strip()
)


match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - slslj")
    case "general":
        print("General - You cheap!")
    case "luxary":
        print("Damn!")
    case _:
        print("Unknown")
