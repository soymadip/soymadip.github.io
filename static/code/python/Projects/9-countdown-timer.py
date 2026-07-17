"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time

from helpers import ask, clear, header


def main() -> None:
    while True:
        clear()
        header("Count Down Timer")

        total_seconds: int = ask(
            "Please Enter time in seconds",
            response_type=int,
            validator=lambda tm: (
                "Please Enter valid time in seconds!" if tm <= 0 else True
            ),
        )

        clear()
        header("Count Down Timer")
        print("Started!\n")
        for remaining_seconds in range(total_seconds, 0, -1):
            minute, second = divmod(remaining_seconds, 60)

            print(f"\rRemaining Time: {minute}:{second}      ", end="")
            time.sleep(1)
        else:
            print("\rRemaining Time: 00:00")
            print("\nTime Up!!!!!\n")
            print("\a")

        ask("Press any key to reset Timer...", press_any_key=True)
        continue


if __name__ == "__main__":
    main()
