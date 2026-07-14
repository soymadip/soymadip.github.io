"""
Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

# TODO: use json in below format:
# [
#   {"task": "the task entry", "done": true},
#   {"task": "anotner task entry", "done": false}
# ]

import os


class ConfReader:
    def __init__(self, config_file) -> None:
        self.config_file = config_file

        if not os.path.exists(config_file):
            try:
                with open(config_file, "w", encoding="utf-8") as file:
                    file.write("")
            except Exception as e:
                print(f"Error: {e}")

    def load_tasks(self) -> list[dict]:
        tasks = []

        try:
            with open(self.config_file, "r", encoding="utf-8") as file:
                for line in file:
                    cleaned_line = line.strip()  # Clean trailing whitespaces/newlines

                    # Skip blank lines
                    if not cleaned_line:
                        continue

                    # Skip line if | is not in line
                    if "|" not in cleaned_line:
                        continue

                    task, status = cleaned_line.rsplit("|", 1)

                    tasks.append(
                        {
                            "task": task.strip(),
                            "done": status.strip() == "done",
                        }
                    )
        except Exception as e:
            print(f"Error loading tasks: {e}")

        return tasks


def main() -> None:
    config = ConfReader("tasks.txt")

    tasks = config.load_tasks()

    # tasks.append({"name": })

    print(tasks)


if __name__ == "__main__":
    main()
