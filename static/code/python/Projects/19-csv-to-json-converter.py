"""
Challenge: CSV-TO-JSON Converter Tool
"""

import csv
import json
import sys
from pathlib import Path

from helpers import ask, header


def main() -> None:
    header("CSV TO JSON Converter")

    csv_path = Path(
        ask(
            "Enter Source CSV file:",
            response_type=str,
            validator=lambda x: (
                "Enter path to a .csv file!"
                if not x.endswith(".csv")
                else "File Doesn't Exists"
                if not Path(x).exists()
                else True
            ),
        )
    )

    output_json_path = csv_path.with_suffix(".json")

    # Make output dir
    output_json_path.parent.mkdir(parents=True, exist_ok=True)

    json_list = None
    try:
        with open(csv_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file, restval=None)
            json_list = [
                {key: value if value != "" else None for key, value in row.items()}
                for row in reader
            ]
    except Exception as e:
        print(f"Error: {e}")

    if not json_list:
        print("CSV file is empty!")
        sys.exit(1)

    try:
        with open(output_json_path, "w", encoding="utf-8") as file:
            if len(json_list) == 1:
                json.dump(json_list[0], file, indent=2)
            else:
                json.dump(json_list, file, indent=2)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
