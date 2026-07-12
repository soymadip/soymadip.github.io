"""
Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
    1. Ask how many people are in the group.
    2. Ask for each person's name.
    3. Ask for the total bill amount.
    4. Calculate each person's share of the bill.
    5. Display how much each person owes in a clean, readable format.

Example:

Total bill: ₹1200
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400
  Neha owes ₹400
  Ravi owes ₹400

Bonus:
    - Round to 2 decimal places
    - Print a decorative summary box

"""

from helpers import ask, border


class TooFewNumberError(Exception):
    pass


print("================ Total Bill Splitter =================\n")


def should_more_than(num: int = 1):
    def validator(answer):
        return True if answer > num else f"Members should be more than {num}!"

    return validator


total_bill: float = ask(
    "What is the total bill ammount", response_type=float, validator=should_more_than(1)
)

print()

total_members: int = ask(
    "How many people to split bill between",
    response_type=int,
    validator=should_more_than(1),
)

each_person_gets: float = round((total_bill / float(total_members)), 2)

members: list[str] = []

for i in range(1, total_members + 1):
    print()
    members.append(ask(f"Enter Name of Member {i}"))


print(f"\n{border}\n\nTotal Bill: ₹{total_bill}\n")

for i in range(total_members):
    print(f"  {members[i].capitalize()} owes ₹{each_person_gets}")

print(f"\n{border}\n")
