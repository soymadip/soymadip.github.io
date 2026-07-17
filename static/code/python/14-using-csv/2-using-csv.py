#
# We use csv module to work with csv
import csv
from typing import Literal

# A csv:
#
# Name,Phone,Email
# Soumadip Das,9830197456,soumadip@example.com
# chodon, 9830123475,chodon@example.com
# googel is shit, 9830123593,googel@example.com
#

# ------------ Read a csv file --------------

with open("ss.csv", "r", encoding="utf-8") as file:
    rows = csv.reader(file)  # returns a 'Reader' iterator object

    next(rows)  # skip first row, usually heading

    for row in rows:
        print(row)
        print(rows.line_num)  # gives current line number

# Output
#
# ['Soumadip Das', '9830197456', 'soumadip@example.com']
# ['chodon', ' 9830123475', 'chodon@example.com']
# ['googel is shit', ' 9830123593', 'googel@example.com']
#
print()


# reading as dictionary

with open("ss.csv", "r", encoding="utf-8") as file:
    rows = csv.DictReader(file)  # returns a 'Reader' iterator object

    for row in rows:
        print(row)

# Output
#
# {'Name': 'Soumadip Das', 'Phone': '9830197456', 'Email': 'soumadip@example.com'}
# {'Name': 'chodon', 'Phone': ' 9830123475', 'Email': 'chodon@example.com'}
# {'Name': 'googel is shit', 'Phone': ' 9830123593', 'Email': 'googel@example.com'}
#


#
#
# ------------- Writing csv ----------------
#
with open("new.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write single row
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["soymadip", "17", "Naihati"])

    # Write Many Rows
    writer.writerows(
        [
            ["soymadip", "17", "Naihati"],
            ["guddu", "21", "Naihati"],
            ["sonali", "15", "Kankinara"],
            ["old man", "87", "DumDum"],
        ]
    )


# Appending instead of replacing whole contnet
# Open file in read mode
with open("new.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write single row
    writer.writerow(["rupali", "66", "reading-shelf"])


# Writing a dictionary
#
rows_csv: list[dict[str, str | int | float]] = [
    {
        "Name": "Alice",
        "Age": 20,
        "City": "London",
    },
    {
        "Name": "Bob",
        "Age": 25,
        "City": "Paris",
    },
]

with open("new.csv", "w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])

    # Write single row
    writer.writerow({"Name": "rupali", "Age": "66", "City": "reading-shelf"})

    # Write Multiple Rows
    writer.writerows(rows_csv)
