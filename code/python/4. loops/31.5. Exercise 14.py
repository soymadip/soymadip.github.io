"""
Task Completion Tracker: Understand interating thorugh list in Python

Instructions
You’re building a simple task tracker for a to-do app. Whenever a user completes tasks, your app should mark them as done.

Tasks:

    Define a function mark_completed_tasks that accepts a list of task names.

    Iterate through the list using a for loop, and update the format like "Completed:  {task}".

    Return a new list with the updated task strings.
"""


# This function will be tested automatically.
# Do not change the function name or parameters.
def mark_completed_tasks(tasks: list[str]) -> list[str]:
    completed_tasks: list[str] = []
    for task in tasks:
        completed_tasks.append(f"Completed: {task}")

    return completed_tasks
