"""
shutils provide high level operation functionalities

shutils name comes from shell utils

this is equivalent of posix commands like
    - cp, \
    - mv,
    - rm -r,
    - du,
    - which,
    - zip
etc.

Unlike pathlib shutil focuses on utilities

pathlib
│
├── Represents paths
├── Reads metadata
├── Creates files/directories
├── Renames
└── Deletes single objects

shutil
│
├── Copy
├── Move
├── Copy entire folders
├── Delete directory trees
├── Archives
└── Miscellaneous filesystem utilities


If something envolves copying data, there shutil should be used
"""

from pathlib import Path
from shutil import copy, copy2, copyfile, copytree, disk_usage, move, rmtree

# -------------- copy() - simplest copy -----------

# this is simplest copy method.
# File content is copied but SOME/NO metadata are copied.
# Overwrites if the target already exists
#
# Returns Path/str according to what is given


src_file: Path = Path(".cache/file.txt")
dest_file: Path = src_file.with_name("file_copied.txt")

result = copy(src_file, dest_file)

print(result, type(result))  # .cache/file_copied.txt      <class posixpath>


#
# -------------- copy2() - copy with metadata -----------

# This copy method is recommended for most of the cases
# It copies:
#  - file contents
#  - modification time
#  - access time
#  - permissions (where supported)
#  - other metadata where the operating system allows

pic = Path(".cache/ss.jpeg")

dest = Path(".code/fucker.jpeg")

# copies file content and metadata like creation date, modified date etc..
copy2(pic, dest)


dest_dir = dest.parent

# copies file with the same name to the destination directory
copy2(pic, dest_dir)  # .code/ss.jpeg


#
# ---------- copyfile() - strictly no metadata -----------
#
# copy() can copy some metadata.
# If we strictly don't want any metadata, we can use copyfile()

pic = Path(".cache/ss.jpeg")
dest = Path(".code/fucker.jpeg")

# copies file content only
copyfile(pic, dest)


#
# ---------- copytree() - copy directory -----------
#
# Copies a directory recursively
#
# Returns the destination directory path

src_dir = Path(".cache")
dest_dir = src_dir.parent / ".new_cache"

copytree(src_dir, dest_dir)
# If srcdir already exists, copytree() will raise an FileExistsError


# We can use the `dirs_exist_ok` param to overwrite it
copytree(src_dir, dest_dir, dirs_exist_ok=True)


rmtree(dest_dir)

#
# ------------ move() - move file or directory -----------

# we can use path.replace() to move a file.
# But it has filesystem limitation
#
# It's recommended to use shutil.move() instead of path.replace()
# If possible it renames, else it copies and deletes the source

src_file = Path(".cache/ss.txt")
dst_dir = src_dir.parent / ".new_cache"

src_file.write_text("google is shit\n" * 1000)
dst_dir.mkdir(exist_ok=True)

move(src_file, dst_dir)  # moves to .new_cache/ss.txt


#
# --------------- rmtree() - remove nonempty directory -------------

# this is one of the most dangerous methods in stdlib
#
# This removes a directory and all of it's contents

for cache_dir in Path(".").rglob("__pycache__"):
    if ".venv" in cache_dir.parts:
        continue

    print("Deleting", cache_dir)
    rmtree(cache_dir)

#
# BE CAREFUL, THIS FUNCTION CAN DELETE WITHOUT WARNING

rmtree("/")  # This will delete the entire filesystem
rmtree("")  # This will delete the current directory

#
# ------------------- disk_usage() - get disk usage -----------

usage = disk_usage("/")  # gives a namedtuple with total, used, and free space

format = lambda bytes: round(bytes / (1024**3), 2) + 'GB'

print(usage)

print(
    f"Total: {format(usage.total)}, Used: {format(usage.used)}, Free: {format(usage.free)}"
)
