"""
Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

from helpers import ask, clear, header


def main() -> None:
    clear()
    header("Student Marks Analyzer")

    students: dict = {}
    i = 1

    while True:
        name = ask(
            f"Enter Student {i} Name {"OR 'Done' to finish entering" if i > 2 else ''}",
            validator=lambda name: (
                "Student already Inputed".title()
                if any(name.lower() == student.strip().lower() for student in students)
                else True
            ),
            response_type=str,
        ).strip()

        if name == "done":
            break

        marks = ask("\nEnter Marks Obtained", response_type=float)

        students[name] = marks
        i += 1

        print("\n")

    clear()
    header("Analysis Calculated")

    max_num: float = max(students[student] for student in students)
    min_num: float = min(students[student] for student in students)

    max_students: str = ",".join(
        student for student in students if students[student] == max_num
    )
    min_students: str = ",".join(
        student for student in students if students[student] == min_num
    )

    print("Total Number of Students:", len(students))
    print(
        "\nAverage Marks:",
        round(float(sum(students[student] for student in students)) / len(students), 2),
    )
    print("Highest Score is", max_num, "by", max_students)
    print("Lowest Score is", min_num, "by", min_students, "\n")


if __name__ == "__main__":
    main()
