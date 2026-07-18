"""
Challenge: JSON-to-csv Converter Tool

Create a Python utility that reads structured data (like you'd get from an API) from a `.json` file and converts it to a CSV file.

Your program should:
1. Read from a file named `api_data.json` in the same folder.
2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
3. Automatically extract field names as CSV headers.
4. Handle nested structures by flattening or skipping them.

Bonus:
- Provide feedback on how many records were converted
- Allow user to define which fields to extract
- Handle missing fields gracefully
"""

import csv
import json
import sys
from pathlib import Path

from helpers import ask, flatten_json, header


def main() -> None:
    header("JSON to CSV Converter")
    source_json = Path(
        ask(
            "Enter Source JSON file:",
            response_type=str,
            validator=lambda x: (
                "Enter path to a .json file!"
                if not x.endswith(".json")
                else "File Doesn't Exists"
                if not Path(x).exists()
                else True
            ),
        )
    )

    output_csv = source_json.with_suffix(".csv")

    print()

    json_data = None
    try:
        with open(source_json, "r", encoding="utf-8") as file:
            json_data = json.load(file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    if not json_data:
        print("Source Json File is Empty!")
        sys.exit(2)

    if isinstance(json_data, list):
        flattened_json = [flatten_json(dict) for dict in json_data]
    elif isinstance(json_data, dict):
        flattened_json = flatten_json(json_data)
    else:
        print("Error: Failed to Flatten Json!")
        sys.exit(3)

    # Create Parent Directory if doesn't exist
    output_csv.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(output_csv, "w", encoding="utf-8", newline="") as file:
            headers = []

            if isinstance(flattened_json, list):
                headers = list({key: None for dtdct in flattened_json for key in dtdct})
            else:
                headers = list(flattened_json)

            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

            writer.writerows(
                flattened_json if isinstance(flattened_json, list) else [flattened_json]
            )
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(4)

    print(json.dumps(flattened_json, indent=2))
    


if __name__ == "__main__":
    main()
