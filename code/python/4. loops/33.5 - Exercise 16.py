"""Student Scores Report

You’re building a simple student report generator that combines names and scores.

Tasks:

    Define a function generate_score_report that takes two lists — one with student names and one with their scores.

    Use the zip() function to pair each student with their score.

    Return a list of strings in the format "Name scored X marks"
"""


# This function will be tested automatically.
# Do not change the function name or parameters.
def generate_score_report(names: list[str], scores: list[int]) -> list[str]:
    report: list[str] = []
    for name, score in zip(names, scores):
        report.append(f"{name} scored {score} marks")

    return report
