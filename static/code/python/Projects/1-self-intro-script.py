"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

while True:
    name: str = input("Enter Your Name: ").strip()

    try:
        age: int = int(input("Enter Your Age: ").strip())
    except ValueError:
        print("Error: Age must be a number\n\n")
        continue

    address: str = input("Enter Your Address: ").strip().capitalize()
    profession: str = input("Enter Your Profession: ").strip()
    hobby: str = input("Enter Your Hobby: ").strip()

    break


msg: str = (
    f"Hello! My name is {name.capitalize()}. I'm {age} years old and live in {address}.\n"
    f"I work as a {profession} & I absolutely enjoy {hobby} in my free time.\n"
    "Nice to meet You!"
)


# # We could do this too
# lines = [
#     "--- Profile ---",
#     "Name: Soumadip Das",
#     "Hobby: Coding"
# ]
#
# print("\n".join(lines))


border: str = f"\n{'*' * 40}\n"

print(border + msg + border)
