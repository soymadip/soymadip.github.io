"""
Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.json` file along with a timestamp.

Your program should:

1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.json`
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.


Bonus:

- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.


Example:

📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5

"""

from datetime import datetime

from helpers import ask, clear, header, jsonReader


def main() -> None:
    config = jsonReader("learning_journal.json")

    journals = config.load()

    menu = {
        1: "Show Previous Journals",
        2: "Add New Journal",
        3: "Delete a Journal",
    }

    # ---------------- Print Menu ---------------

    while True:
        clear()
        header("Your Daily Journal", bar_symbol="=", bar_len=45)

        menu[4] = "Exit"

        response = ask(
            "What do you want to do today?",
            response_type=int,
            options=[option for option in menu.values()],
        )

        clear()
        match response:
            case 1:
                header("Previous Journals")

                for date, entries_dict in journals.items():
                    for time, details_dict in entries_dict.items():
                        print(f"------- 📅 {date} - {time} -------\n")
                        print(f"{details_dict['content']}")
                        if details_dict["rating"] is not None:
                            print(f"Productivity Rating: {details_dict['rating']}/5")
                        print()

                header(bar_symbol="-")

                if input("Press any key to go Back to Main Menu"):
                    continue

            case 2:
                while True:
                    clear()
                    header("Add Journal")

                    contnt = ask("What do you want to write?")
                    print()
                    rating = ask(
                        "Leave a Productivity rating [1-5]",
                        response_type=int,
                        validator=lambda rating: (
                            "Rating must be under 5"
                            if (rating < 0 or rating > 5)
                            else True
                        ),
                    )

                    cr_dt = datetime.now()
                    current_date = cr_dt.strftime("%d-%m-%Y")
                    current_time = cr_dt.strftime("%H:%M:%S")

                    if current_date not in journals:
                        journals[current_date] = {}

                    journals[current_date][current_time] = {
                        "content": contnt,
                        "rating": rating,
                    }

                    if not ask("Do You Want to add More?", response_type=bool):
                        break

                config.write(journals)
                continue

            case 3:
                while True:
                    clear()
                    header("Delete Journals")

                    entries = {
                        f"{content_dict['content']}": f"{date}_{time}"
                        for date, entry_dict in journals.items()
                        for time, content_dict in entry_dict.items()
                    }

                    entries["Save & Back to Main Menu"] = "main_menu"

                    to_delete = ask(
                        "Which one you wanna delete?",
                        options=[entry for entry in entries],
                    )

                    if to_delete == "Save & Back to Main Menu":
                        config.write(journals)
                        break

                    date, time = entries[to_delete].split("_")

                    if not journals[date].pop(time, False):
                        print(f"Not Found: {to_delete}")

                    if not journals[date]:
                        journals.pop(date)

                continue

            case 4:
                clear()
                print("Ok then, see you again next time!")
                break


#
#
# Execute Script
if __name__ == "__main__":
    main()
