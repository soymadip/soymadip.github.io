"""
 Challenge: File Sorter by Type

Goal:
- Scan the current folder (or a user-provided folder)
- Move files into subfolders based on their type:
    - .pdf → PDFs/
    - .jpg, .jpeg, .png → Images/
    - .txt → TextFiles/
    - Others → Others/
- Create folders if they don't exist
- Ignore folders during the move

Teaches: File system operations, automation, file handling with `os` and `shutil`
"""

import shutil
import sys
from pathlib import Path


def organize_files(folder: str | Path = ".") -> None:
    folder = Path(folder)

    if not (folder.exists() and folder.is_dir()):
        raise ValueError("folder must be a valid directory path!")

    EXT_MAP = {
        "PDFs": ["pdf"],
        "Images": ["jpg", "jpeg", "png", "avif"],
        "Videos": ["mp4", "mkv"],
        "TextFiles": ["txt", "md"],
    }

    def mkdir(trgt: Path):
        try:
            trgt.mkdir(exist_ok=True, parents=True)
        except OSError as e:
            print("Failed to create directory:", e, file=sys.stderr)
            sys.exit(1)

    for item in folder.iterdir():
        if item.is_dir():
            continue

        for cdir, exts in EXT_MAP.items():
            if item.suffix.lstrip(".").lower() in exts:
                target_dir: Path = Path(folder) / cdir

                mkdir(target_dir)
                shutil.move(item, target_dir)

                break
        else:
            target_dir = folder / "Others"

            mkdir(target_dir)
            shutil.move(item, target_dir)
