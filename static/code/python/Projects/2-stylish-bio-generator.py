"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer
  💡 Making things beautiful
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""

while True:
    name: str = input("Enter your name: ").strip().capitalize()
    profession: str = input("Enter your Profession: ").strip()
    passion: str = input("Enter your Passion (in one line): ").strip()
    favourite_emoji: str = input("Enter your favourite emoji (Optional): ").strip()
    website: str = input("Enter your website (optional): ").strip()

    for item, value in [
        ("name", name),
        ("profession", profession),
        ("passion", passion),
    ]:
        if not value:
            print(f"\n{item} must be given!\n")
            break
    else:
        break


print("\nChoose Your preffered Style:")
print(" 1. CyberPunk\n 2. Minimal\n")

while True:
    try:
        chosen = int(input("Enter Your Preffered Style (1/2): ").strip())
        if chosen < 1 and chosen < 2:
            raise ValueError("Choose between 1 and 2")
    except TypeError:
        print("Please input a number!")
        continue
    except ValueError as e:
        print(e)
        continue
    else:
        break


bio: str = ""

match chosen:
    case 1:
        bio = (
            f"Loading profile: {favourite_emoji if favourite_emoji else ''}{name}...\n"
            f">> 💻 PROFESSION: {profession}\n"
            f">> 🔥 PASSION: {passion}\n"
            f"{f'>>   WEBSITE: {website}\n' if website else ''}"
        )
    case 2:
        bio = (
            f"Name: {name}"
            f"Professoin: {profession}\n"
            f"Passion: {passion}\n"
            f"{f'{website}\n' if website else ''}"
        )


border = "*" * 40

bio = f"\n{border}\n\n{bio}\n{border}\n"

print(bio)


while True:
    print("Do You wanna save this to a file? [Y/N]")
    response = input(">> ").strip().lower()

    if response not in ["y", "n"]:
        print("Please choose between Y/N!")
        continue

    break


if response == "y":
    file_name = name.replace(" ", "_") + "_bio.txt"

    try:
        with open(file_name, "x") as file:
            file.write(bio)
    except Exception as e:
        print(f"Error: {e}")
