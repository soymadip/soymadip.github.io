"""
Python filesystem APIs
│
├── pathlib
│   └── Paths + filesystem objects
│
├── shutil
│   └── High-level file operations
│
├── tempfile
│   └── Temporary resources
│
└── os
    └── Operating-system interface

os exposes many operating-system related functions and constants.
"""

import os
import sys

# --------- os.environ - Environment variables -----------
# this is a dictionary containing the environment variables (Actually a mapping obj behaves)

print(
    os.environ.get("HOME")
)  #           why shouldn't use []?  [] raises error if the var is not set.
#                                     get() returns None (optionally a default value) if the var is not set

print(os.environ["HOME"])  # gives keyError if not set. Use for required vars.


#
# --------- os.getenv - Get environment variable ------------
#
# same as os.environ.get()
# clearer api

print(os.getenv("HOME"))  # returns None if the var is not set
print(os.getenv("HOME", "~"))  # returns "~" if the var is not set


# We can also modify the environment of current python process.
# Note THIS DOESN'T CHANGE THE SHELL ENVIRONMENT

os.environ["HOME"] = "/root"  # changes only for current process


# --------- os.chdir - Change current directory ------------
#
# Change current working dir of the process
# BE CAREFUL, this changes for entire curent process

os.chdir("/tmp")

print(os.getcwd())  # prints /tmp

# ------------- os.name - Operating system name ------------
#
# Returns the name of the operating system
print(os.name)  # prints 'posix' on Linux, 'nt' on Windows

# For detailed platform info, use sys.platform
print(sys.platform)  # prints 'linux' on Linux, 'win32' on Windows


# --------- os.sep - os's path separator ------------#
#
print(os.sep)  # prints '/' on Linux, '\' on Windows

# This is why in first place we use pathlib. it handles separators automatically.


# -------- os.linesep - os's line separator ------------#
#
print(os.linesep)  # prints '\n' on Linux, '\r\n' on Windows


# -------- os.symlink - Create a symbolic link ------------#
#
os.symlink("target", "link_name")

# -------- os.link - create hard link ------------#

"""
# What is diff between symlink and hard link?

- Symlink acts like a shortcut to the path of the original file
- Hard link points to the inode (file's data) of the original file in the filesystem


If a hard link's original file is deleted, the data still persists unlike symlink.

| *Feature*            | *Hard Link*           | *Soft Link*          |
| Reference            | Direct to inode/data  | Path/name of file    |
| Inode Number         | Same as original      | Different            |
| Cross-Filesystem     | No                    | Yes                  |
| Link to Directory    | No                    | Yes                  |
| Original Deleted     | Data remains          | Link breaks          |
| sh Command           | `ln file link`        | `ln -s file link`    |

"""

# creates a hard link named "link_name" pointing to "target"
os.link("target", "link_name")


# -------- os.scandir - Scans a directory for entries ---------

# we have Path.iterdir.
# This one is low-level dir scanning api.
#
# Diff between os.scandir and Path.iterdir:
# - Path.iterdir returns a generator of Path objects
# - os.scandir returns a generator of DirEntry objects. This is more efficient if scanning large directories.

with os.scandir("large_dir") as entries:
    for entry in entries:
        print(
            entry.name,  # Name of the entry
            entry.path,  # Full path of the entry
            entry.is_dir(),  # True if entry is a directory
            entry.is_file(),  # True if entry is a file
            entry.is_symlink(),  # True if entry is a symbolic link
            entry.stat().st_atime,  # Last access time of the entry
        )

        if entry.is_dir():
            continue


# ------------- os.getpid - Get process ID of current process -------------

print(os.getpid())


# ------------- os.getppid - Get process ID of parent process -------------

print(os.getppid())


# ------------- os.getuid & os.getgid - Get user ID and group ID of current process -------------
# These are unix only

print(os.getuid())
print(os.getgid())
