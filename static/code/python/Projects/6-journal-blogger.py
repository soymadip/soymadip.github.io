"""
Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:

1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.json`
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.


Bonus:

- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.


Example:

📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5

"""

import json

data = {"google": None, "zsh": True, "arch": True, "fedora": False, "id": 101}

# Production log format (Sorted keys, indented by 2 or 4 spaces)
pretty_json = json.dumps(data, indent=2, sort_keys=True)

print(pretty_json)
