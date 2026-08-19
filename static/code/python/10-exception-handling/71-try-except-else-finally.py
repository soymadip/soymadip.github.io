"""
error handling
"""

# handling error instead of crashing

menu: dict[str, int] = {"msala": 30, "ginger": 40}


try:
    print(menu["googll"])
except KeyError:
    print("Couldn't find")

print("reached here")


# lets go deeper baby!
def serve_chai(chai_name: str) -> None:
    print("Serving Chai...")

    try:  # try to do this risky process
        if chai_name == "unknown":
            raise ValueError(
                "unknkown chai is not found"
            )  # use raise to throw and error or ValueError

    except ValueError as e:  # Except block executes if try block has risen errors
        print(f"Error: {e}")

    else:  # this executes if try block doesn't get any error
        print("chai is served master!")

    finally:  # this always executes error or successful run. (like we wanna close db connection in any case)
        print("Closing shop master!")


serve_chai("google")
serve_chai("unknown")


# We can raise the same exception again
try:
    print(menu["googll"])
except KeyError:
    print("Couldn't find")
    raise
