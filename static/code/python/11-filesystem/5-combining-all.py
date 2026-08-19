"""
In a python program, we use all combined. not just of of the modules
"""

import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

# -------------- A Simple Directory Inspector ------------------


def simple_inspect(dir: Path) -> None:
    for item in dir.iterdir():
        if item.is_file():
            print("File:", item)
        elif item.is_dir():
            print("Dir:", item)


# ----------------- Directory Size Calculator ------------------


def calculate_dir_size(dir: Path) -> str:
    total_size_bytes: float = 0.0

    dir.mkdir(exist_ok=True)

    for item in dir.rglob("*"):
        if item.is_file():
            total_size_bytes += item.stat().st_size

    return f"Total Size: {round(total_size_bytes / (1024**2), 3)} MB"


# ----------------- Find the largest file in a directory ------------------


def find_largest_file(dir: Path) -> Path:

    largest_file: tuple[Path | None, float] = (None, 0.0)

    for item in dir.rglob("*"):
        if not item.is_file():
            continue

        size = item.stat(follow_symlinks=False).st_size

        if size > largest_file[1]:
            largest_file = (item, size)

    if largest_file[0] is None:
        raise ValueError("Directory doesn't contain any file")

    return largest_file[0]


# ------------- Find all python files in a directory ------------------


def find_all_python_files(dir: Path) -> list[Path]:
    return [item for item in dir.rglob("*.py") if item.is_file()]


# -------------- Cleanup Utility -----------------------------


def cleanup(dir_path: Path | None = None, pattern: str = "__pycache__") -> None:

    if dir_path is None:
        dir_path = Path(".")

    for cache in dir_path.rglob(pattern):
        if cache.is_dir():
            shutil.rmtree(cache)


# ----------------- File Organizer ------------------------------


def organize_files(target: Path) -> None:

    item_map: dict[str, list[str]] = {
        "Images": ["jpg", "jpeg", "png", "webp"],
        "Documents": ["pdf", "txt", "md", "mdx", "docx", "xlsx"],
        "Music": ["mp3", "wav", "flac"],
        "Videos": ["mp4", "mkv", "m3u"],
    }

    for item in target.iterdir():
        if item.is_file():
            for catagory, exts in item_map.items():
                if item in exts:
                    ctdir = target / catagory

                    ctdir.mkdir(exist_ok=True, parents=True)

                    shutil.move(item, ctdir)  # pyright: ignore[reportUnusedCallResult]
                    break


# --------------------- Creating backup -------------------------


def backup(
    source_path: Path | str = ".",
    bkp_dir: Path | str = "backup",
    ignore_patterns: list[str] | None = None,
):
    """
    creates backup copy in specified bkp_dir.
    If bkp_dir is backup. the backup will be created at backup/source_path.name
    """

    source_path = Path(source_path)
    bkp_dir = Path(bkp_dir)
    bkp_path: Path = Path(bkp_dir / source_path.name)
    ignore_patterns = ignore_patterns or []

    if not source_path.exists():
        raise ValueError("Source path doesn't exist")

    if source_path.is_dir():
        shutil.copytree(
            source_path,
            bkp_path,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns(*ignore_patterns),
        )  # pyright: ignore[reportUnusedCallResult]
    else:
        bkp_path.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, bkp_path)  # pyright: ignore[reportUnusedCallResult]


# ------------------- List archive content --------------------


def list_archive(archive_path: Path):

    if not archive_path.exists():
        raise ValueError("Archive Doesn't exist")

    with TemporaryDirectory() as tmp_dir:
        shutil.unpack_archive(archive_path, tmp_dir)

        for item in Path(tmp_dir).rglob("*"):
            if item.is_file():
                print(item)


# ------------------ Find executable path ------------------


def which(cmd: str) -> str | None:
    return shutil.which(cmd)


# ---------------- Dir Tree Generation ----------------------


def print_dir_tree(
    root: Path | str = ".",
) -> None:

    root = Path(root)

    for current, _, files in root.walk():
        level: int = len(current.relative_to(root).parts)
        indent: str = "    " * level

        print(f"{indent}{current.name}/")

        for file in files:
            print(f"{indent}   {file}")


# print_dir_tree("notes/3 - machile-learning")


# --------------------- Find symlinks in a directory -------------------


def find_symlinks(directory: Path | str = ".") -> dict[Path, Path]:

    directory = Path(directory)
    symlinks: dict[Path, Path] = {}

    if not (directory.exists() or directory.is_dir()):
        raise ValueError("directory must be a valid directory path")

    for item in directory.rglob("*"):
        if item.is_symlink():
            symlinks[item] = item.readlink()

    return symlinks


# -------------- Broken symlink finder-------------------


def find_broken_symlinks(directory: str | Path = ".") -> list[Path]:
    brokens: list[Path] = []
    directory = Path(directory)

    if not (directory.exists() or directory.is_dir()):
        raise ValueError("directory must be a valid directory path")

    for item in directory.rglob("*"):
        if item.is_symlink() and not item.exists():
            brokens.append(item)

    return brokens
