"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

from helpers import ask, clear, header


def main() -> None:
    clear()
    header("Friendshit Compatibility Calculator".title(), bar_len=60)

    frnd1: str = ask("Enter Your Name:")
    frnd2: str = ask("\nEnter Your Friend's Name:")

    common_chars = set(frnd1) & set(frnd2)

    common_chars_marks = len(common_chars) * 5
    common_vowels_mark = len(set("aeiou") & common_chars) * 10

    total_marks = min(common_chars_marks + common_vowels_mark, 100)

    clear()
    header("Friendship score".title(), bar_len=60)

    print("Your friendship score is:", total_marks)

    if total_marks > 50:
        print("Wow! You two are pretty good!")
    else:
        print("Maybe You two are not meant for each others buddy :)")

    print()


if __name__ == "__main__":
    main()
