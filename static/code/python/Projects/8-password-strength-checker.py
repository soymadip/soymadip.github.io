"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
  1. Length (at least 8 characters)
  2. At least one uppercase letter
  3. At least one lowercase letter
  4. At least one digit
  5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import getpass
import random
import string

from helpers import clear, header


def main() -> None:
    clear()
    header("Passward Strength checker")

    MIN_PASSWORD_LEN = 8

    issues: list[str] = []

    password = getpass.getpass("Enter your password: ", echo_char="*")

    if len(password) < MIN_PASSWORD_LEN:
        issues.append(f"Password length should be atleast {MIN_PASSWORD_LEN}")

    if any(letter.isupper() for letter in password):
        issues.append("atleast one letter should be uppercase".title())

    if any(letter.islower() for letter in password):
        issues.append("atleast one letter should be lowercase".title())

    if any(letter.isnumeric() for letter in password):
        issues.append("should include atleast one number".title())

    if any(letter in string.punctuation for letter in password):
        issues.append("should include atleast special character".title())

    print()
    if not issues:
        print("All good, this is a strong password!")
    else:
        clear()
        print("This is not a strong password!\n")
        print("Your password should:\n")
        print("\n".join(f"- {reason}" for reason in issues))

    # suggest strong password
    CHARS: str = string.ascii_letters + string.punctuation + string.digits

    print(
        "\nHere is a recommended strong password:",
        "".join(random.choice(CHARS) for _ in range(MIN_PASSWORD_LEN + 4)),
    )


if __name__ == "__main__":
    main()
