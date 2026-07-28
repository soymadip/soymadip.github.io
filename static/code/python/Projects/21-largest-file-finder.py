"""
Find the largest file in a user Given directory
and show path, size in KB/MB/GB
"""

import sys
from pathlib import Path
from time import sleep

from helpers import clear, format_size


def main() -> None:

    while True:
        clear()
        dir = input("\nEnter a Directory to check: ")
        print()

        try:
            target_dir = Path(dir).resolve()

            if not target_dir.exists():
                raise FileNotFoundError("Given directory doesn't exist")

            if not target_dir.is_dir:
                raise NotADirectoryError("Given Path is not a directory!")

            break
        except NotADirectoryError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except TypeError:
            print("Please enter a valid dir path")

        sleep(2)

    largest = (None, 0)

    for item in target_dir.rglob("*"):
        if item.is_dir():
            continue

        size = item.stat().st_size

        if size > largest[1]:
            largest = (item, size)

    if not largest[0]:
        print("Directory doesn't contain any file")
        sys.exit(1)

    size, unit = format_size(largest[1])
    print(f"Biggest file is {largest[0].relative_to(Path.cwd())} [{size}{unit}]")


if __name__ == "__main__":
    main()
