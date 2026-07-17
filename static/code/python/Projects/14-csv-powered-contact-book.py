"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv
import os
import sys
from time import sleep

from helpers import ask, clear, header


class CsvManager:
    def __init__(self, file) -> None:
        self.config_file = file
        self.__header_row = ["Name", "Phone", "Email"]

        # Create the containing directory if it doesn't exist
        dir_name = os.path.dirname(self.config_file)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)

        # Create file if it does not exist
        if not os.path.exists(self.config_file):
            try:
                with open(self.config_file, "w", encoding="utf-8", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(self.__header_row)
            except Exception as e:
                print(f"Initialization Error: {e}")
                sys.exit(1)

    def list(self, raw=False) -> list:
        try:
            with open(self.config_file, "r", encoding="utf-8") as file:
                rows = csv.reader(file)

                if raw:
                    try:
                        next(rows)  # Skip the header row
                    except StopIteration:
                        pass
                    return list(rows)
                else:
                    has_printed = False
                    for row in rows:
                        has_printed = True
                        col3 = f"{row[2]} |" if len(row) > 2 and row[2] else "N/A |"
                        print(f"{row[0]} | {row[1]} | {col3}")

                    if not has_printed:
                        print("No contacts found.")
                    return []

        except Exception as e:
            print(f"Error reading file: {e}")
            return []

    def add(self, name, phone, email) -> bool:
        contacts = self.list(raw=True)

        try:
            if contacts:
                for contact in contacts:
                    if name.lower() in contact[0].lower():
                        raise ValueError("Contact Name is already in Contacts")

            with open(self.config_file, "a", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, phone, email])
        except Exception as e:
            print(f"Error adding contact: {e}")
            return False

        return True

    def search(self, query: int | str, raw=False) -> list | None:
        contacts = self.list(raw=True)

        if not contacts:
            print("No contacts available to search.")
            return None

        search_result: list = []

        for i, row in enumerate(contacts, start=1):
            search_field: str = row[0] if isinstance(query, str) else str(row[1])

            if str(query).lower() in search_field.lower():
                if raw:
                    search_result.append(row)
                else:
                    print(f"{i}. {row[0]}: {row[1]}")

        if not raw or not search_result:
            return None

        return search_result

    def remove(self, query) -> bool:
        try:
            contacts = self.list(raw=True)

            if not contacts:
                print("Contact list is empty.")
                return False

            target_contact = None
            for contact in contacts:
                search_field: str = (
                    contact[0] if isinstance(query, str) else str(contact[1])
                )

                if str(query).lower() == search_field.lower():
                    target_contact = contact
                    break

            if target_contact is not None:
                contacts.remove(target_contact)
            else:
                raise ValueError("Contact Not Found!")

            # Re-write the updated data completely safely
            with open(self.config_file, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(self.__header_row)
                writer.writerows(contacts)

        except Exception as e:
            print(f"Error removing contact: {e}")
            return False

        return True


def main() -> None:
    CONTACT_DB_FILE = ".cache/contacts.csv"
    contacts = CsvManager(CONTACT_DB_FILE)

    while True:
        clear()
        header("Contact Book")

        action = ask(
            question="Please Choose an option: ",
            options=[
                ("view-all", "View All Contacts"),
                ("add-new", "Add New Contact"),
                ("search", "Search For a Contact"),
                ("delete", "Delete a Contact"),
                ("exit", "Exit App"),
            ],
        )

        clear()
        match action:
            case "view-all":
                header("View Contacts")
                contacts.list()
                ask("\nPress Any Key to Return to Main Menu...", press_any_key=True)

            case "add-new":
                header("Add New Contact")
                name = ask("Enter Contact Name")
                phone = ask("\nEnter contact Phone No.", response_type=int)
                email = ask("\nEnter contact Email (optional)", allow_empty=True)

                if contacts.add(name, phone, email):
                    print("\nContact Added Successfully!")
                sleep(1)

            case "search":
                header("Search Contact")
                response = ask(
                    "Search Contact by:",
                    options=["Number", "Name"],
                )

                query = ask(
                    f"\nEnter Contact {response}",
                    response_type=int if response == "Number" else str,
                )

                clear()
                header(f"Results for: {query}", bar_len=60)
                contacts.search(query)
                ask("\nPress Any Key to Return to Main Menu...", press_any_key=True)

            case "delete":
                header("Delete a Contact")
                response = ask(
                    "Delete Contact by:",
                    options=["Name", "Number"],
                )

                query = ask(
                    f"\nEnter Contact {response}",
                    response_type=int if response == "Number" else str,
                )

                if not ask("\nAre you sure?", response_type=bool):
                    print("\nOperation Canceled!")
                    sleep(1)
                    continue

                if contacts.remove(query):
                    print("\nSuccessfully deleted!")
                else:
                    print("\nFailed to Delete contact! Try again...")
                sleep(1)

            case "exit":
                clear()
                print("Ok, See you again next time...")
                break


if __name__ == "__main__":
    main()
