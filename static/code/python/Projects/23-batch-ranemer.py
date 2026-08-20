"""
Challenge: Batch Rename Files in a Folder

Goal:

- Scan all files in a selected folder

- Rename them with a consistent pattern:
    e.g., "image_1.jpg", "image_2.jpg", ...

- Ask the user for:
    - A base name (e.g., "image")
    - A file extension to filter (e.g., ".jpg")

- Preview before renaming

Teaches: File iteration, string formatting, renaming, user input
"""

import json
import shutil
import sys
from pathlib import Path


def main() -> None:

    while True:
        target_dir: Path = Path(input("Enter Directory path to scan: "))

        if not (target_dir.exists() and target_dir.is_dir()):
            print("Invalid directory path.\n", file=sys.stderr)
            continue
        break

    base_name: str = input("Enter base name: ")
    extension: str = input("Enter file extension (with dot. e.g., .jpg): ")

    bkp_dir: Path = target_dir / "backup"
    bkp_mapping: Path = bkp_dir / "mapping.json"

    bkp_dir.mkdir(exist_ok=True, parents=True)

    renamed: dict[str, str] = {}

    for item in target_dir.glob(f"*{extension}"):
        if not item.is_dir():
            continue

        new_name: str = f"{base_name}_{len(renamed) + 1}{extension}"

        try:
            _ = shutil.move(item, bkp_dir / new_name)

            renamed[item.name] = new_name

            print("Renamed:", item.name, "->", bkp_dir, "/", new_name)

        except OSError as e:
            print(f"Failed to rename {item.name}: {e}", file=sys.stderr)

    try:
        _ = bkp_mapping.write_text(json.dumps(renamed), encoding="utf-8")
    except OSError as e:
        print(f"Failed to save backup mapping: {e}", file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user! (Ctrl+C).", file=sys.stderr)
        sys.exit(130)
