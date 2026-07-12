"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""

import time

from helpers import ask


def calculate_age(age_in_year: int | float) -> tuple:
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24.00
    MINUTES_IN_HOUR = 60.00

    age_days = round(float(age_in_year) * DAYS_IN_YEAR, 2)
    age_hours = age_days * HOURS_IN_DAY
    age_minutes = age_hours * MINUTES_IN_HOUR

    return age_days, age_hours, age_minutes


def main() -> None:

    while True:
        age_years: float = ask("What is your age (In Years)", response_type=float)

        age_days, age_hours, age_minutes = calculate_age(age_years)

        print(
            f"\nYou are {age_days:,} days, {age_hours:,} hours, {age_minutes:,} minutes old"
        )

        print()
        time.sleep(2)
        if (
            ask(
                "Do want to try again",
                response_type=bool,
                options=["y", "n"],
                case_sensitive=True,
            )
            == "y"
        ):
            print("\n")
            continue
        else:
            break


if __name__ == "__main__":
    main()
