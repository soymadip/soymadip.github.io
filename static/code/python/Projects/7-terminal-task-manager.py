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

1. Buy groceries||not_done
2. Finish Python project||done
3. Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

# Instead of using json in below format:
# [
#   {"content": "the task entry", "done": true},
#   {"content": "anotner task entry", "done": false}
# ]
#
# We will be manually parsing a txt file for this project
# Internally, we still use above format

import copy
import os
from time import sleep

import helpers as hl


class TaskManager:
    def __init__(self, config_file) -> None:
        self.config_file = config_file
        self.__tasks: list[dict] = []
        self.__stock_tasks = []

        # make the file if not exists
        if not os.path.exists(config_file):
            try:
                with open(config_file, "w", encoding="utf-8") as file:
                    file.write("")
            except Exception as e:
                print(f"Error: {e}")

        # Make the tasks dict
        try:
            with open(config_file, "r", encoding="utf-8") as file:
                for line in file:
                    cleaned_line = line.strip()  # Clean trailing whitespaces/newlines

                    # Skip blank lines
                    if not cleaned_line:
                        continue

                    if cleaned_line.startswith("done|"):
                        task_content = cleaned_line.removeprefix("done|")
                        task_done = True
                    else:
                        task_content = cleaned_line
                        task_done = False

                    if task_content.strip() not in (
                        task_dict["content"] for task_dict in self.__tasks
                    ):
                        self.__tasks.append(
                            {
                                "content": task_content.strip(),
                                "done": task_done,
                            }
                        )

                    # sort tasks, keep pendings before
                    self.__tasks.sort(key=lambda x: x["done"])

        except Exception as e:
            print(f"Error: {e}")

        self.save()
        self.__stock_tasks = copy.deepcopy(self.__tasks)

    @property
    def tasks(self) -> list[dict]:
        copy_tasks = copy.deepcopy(self.__tasks)
        return copy_tasks

    @tasks.setter
    def tasks(self, new_tasks: list[dict]):
        if not isinstance(new_tasks, list):
            raise TypeError("tasks must be a list!")

        if not all(isinstance(task, dict) for task in new_tasks):
            raise ValueError("All items inside the tasks list must be dictionaries!")

        self.__tasks = copy.deepcopy(new_tasks)

    def save(self) -> bool:
        """Write the tasks to config File"""

        # Dont write if notihing is changed
        if self.__stock_tasks == self.__tasks:
            print("no changes")
            return True

        lines: str = ""

        # pythonic way
        lines = "\n".join(
            f"{'done|' if task_dict['done'] else ''}{task_dict['content']}"
            for task_dict in self.__tasks
        )

        try:
            with open(self.config_file, "w", encoding="utf-8") as file:
                file.write(lines + "\n")
        except Exception as e:
            print(f"Error: {e}")
            return False
        else:
            self.__stock_tasks = copy.deepcopy(self.__tasks)

        return True

    def count(self) -> int:
        return len(self.__tasks)

    def exists(self, task: str) -> bool:
        cleaned_content = task.strip()

        for task_dict in self.__tasks:
            if cleaned_content in task_dict["content"]:
                return True
        else:
            return False

    def add(self, content: str, done: bool = False) -> bool:
        """Add an entry to the tasks"""

        cleanded_content = content.strip()

        if not isinstance(content, str):
            raise TypeError("'content' must be a string!")

        if not isinstance(done, bool):
            raise TypeError("'done' must be a boolean!")

        if not self.exists(cleanded_content):
            self.__tasks.append(
                {
                    "content": content.strip(),
                    "done": done,
                }
            )
            return self.save()

        return True

    def update_state(self, task: str, done: bool) -> bool:
        """Mark a Task done/undone"""
        cleaned_content = task.strip()

        for i, task_dict in enumerate(self.__tasks):
            if cleaned_content in task_dict["content"]:
                task_dict["done"] = done
                break
            self.__tasks[i] = task_dict
        else:
            raise ValueError("Given Task not found!")

        return self.save()

    def pop(self, task: str) -> bool:
        cleaned_content = task.strip()

        for i, task_dict in enumerate(self.__tasks):
            if cleaned_content in task_dict["content"]:
                self.__tasks.pop(i)
                break
        else:
            raise ValueError("Given Task not found!")

        return self.save()


def main() -> None:
    tasks = TaskManager("tasks.txt")

    while True:
        hl.clear()
        hl.header("Task Manager")

        response = hl.ask(
            "Please Select an option:",
            options={
                "add-task": "Add a Task",
                "view-tasks": "View All Tasks",
                "change-state": "Mark a Task Completed/Pending",
                "delete-task": "Delete a Task",
                "exit": "Exit App",
            },
        )

        hl.clear()
        match response:
            case "add-task":
                hl.clear()
                hl.header("Add Tasks")

                if tasks.add(hl.ask("Enter Your Task:", allow_empty=False)):
                    print("\n[Success] Task Added!")
                    sleep(1)
                else:
                    print("\n[Error] Couldn't add task! Please Try again")
                    sleep(3)

                continue

            case "view-tasks":
                hl.header("All Tasks")

                for task_dict in tasks.tasks:
                    print(
                        f"{'✓' if task_dict['done'] else '✘'}  {task_dict['content']}"
                    )

                hl.ask("\nPress any key to return..", press_any_key=True)

            case "change-state":
                while True:
                    hl.header("Change Status of a Task")

                    current_tasks = tasks.tasks

                    selected_task = hl.ask(
                        "Enter a Task Number to change state:",
                        options=(
                            f"{'✓' if task_dict['done'] else '󰃰'}  {task_dict['content']}"
                            for task_dict in current_tasks
                        ),
                        final_options="Return To Main Menu",
                        return_index=True,
                    )

                    if selected_task == -1:
                        break

                    selected_task -= 1

                    selected_task_content = current_tasks[selected_task]["content"]
                    selected_task_status = current_tasks[selected_task]["done"]

                    if not tasks.update_state(
                        selected_task_content, not selected_task_status
                    ):
                        print("Failed to update, Please Try Again..")
                        sleep(3)

                    hl.clear()

                continue

            case "delete-task":
                while True:
                    hl.header("Delete Tasks")

                    current_tasks = tasks.tasks

                    selected_task = hl.ask(
                        "Enter a Task Number to Delete:",
                        options=(
                            f"{'✓' if task_dict['done'] else '󰃰'}  {task_dict['content']}"
                            for task_dict in current_tasks
                        ),
                        final_options="Return To Main Menu",
                        return_index=True,
                    )

                    if selected_task == -1:
                        break

                    print(selected_task)
                    selected_task -= 1

                    selected_task_content = current_tasks[selected_task]["content"]
                    selected_task_status = current_tasks[selected_task]["done"]

                    if not tasks.pop(selected_task_content):
                        print("Failed to update, Please Try Again..")
                        sleep(3)

                    hl.clear()

            case "exit":
                print("Ok then, See you until next time!")
                break


if __name__ == "__main__":
    main()
