r"""
## Pathlib

Before Python 3.4, path manipulation was commonly done using the `os.path` module.

Although `os.path` is still fully supported, `pathlib` is now the recommended approach because it provides a cleaner, object-oriented API.

Compared to `os.path`, `pathlib` offers several advantages:

- Paths are represented by `Path` objects with intuitive methods instead of many standalone functions.
- Handles platform-specific path syntax (such as `/` on Unix-like systems and `\` on Windows) automatically.
- Joining paths, changing file extensions, or getting parent directories are easier to read and write.
- Besides manipulating paths, `Path` objects can also create, rename, delete, copy (with `shutil`), and inspect files and directories.
- Most new Python code and official documentation use `pathlib`.

chat:
    https://chatgpt.com/c/6a620a08-9074-83e8-80cf-b4b0bb7bf763

"""

# In ancient times, we used to use os.path for path manipulation
# This has some problems like it's not object oriented, or cumbersome.
import os
from shutil import rmtree

path: str = os.path.join("home", "soymadip", "file.txt")


# -------------- pathlib introduced Path class ------------------
#
# Instead of manipulating strings, we now use objects


from pathlib import Path

# ------ Creating a path -------
#
# This doesn't create the dir/file. It's just a representation of the fs path
#
dir_path = Path(
    "~/.cache"
).expanduser()  # Absolute Path  (expanduser() expands ~ with /home/user)
another_path = Path("docs/dir")  # Relative Path


print(dir_path)  # /home/soymadip/.cache


# Paths are immutable
new_path = dir_path.with_suffix(".google")  # this creates new path..


#
# -------- converting to string ------

str(Path("notes.txt"))

# most modern libraries accept Path object directly


#
# -------- Joining Paths ---------

# just use division operator. Windows is handled automatically
mount_dir = Path("/mnt") / "hdd" / "1"
print(mount_dir)  #  /mnt/hdd/1

# we can joing 2 paths too.
print(mount_dir / dir_path)


# ----------- Comparing paths -----------

print(dir_path == new_path)  # False


#
# ------------- getting path parts ------------
#
# getting path parts
# useful for processing path components
#
print(dir_path.parts)  # prints a tuple

# delete all python cache dirs except those in .venv
for cache in Path(".").rglob("__pycache__"):
    if ".venv" in cache.parts:
        continue

    print("Deleting", cache)
    rmtree(cache)
