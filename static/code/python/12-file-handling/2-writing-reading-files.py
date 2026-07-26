"""
For file handling, we should use dedicated libraries.

But let's understand python's builtin one
"""

# we can use open method:
import sys
from pathlib import Path

file = open(
    "file.txt",
    "w",
    encoding="utf-8",  # open in write mode. this loads into memory
)

file.write("google is shit\n")


""" ------------- Note --------------

We should almost always pass encoding="utf-8" to open mehtod for compatibility b/w windows and unix.

Only exception is binary files.

with open("image.png", "rb") as f:
    content = f.read()

"""

# ---------------------- Writing files ------------------

file.write(  # this completely replaces file's content with given. Creates file if not exists
    "google is shit\n"
)

file.close()  # close the file.


#  BUT THERE IS MORE EFFICIENT WAY
with open("file.txt", "w", encoding="utf-8") as file:  # file is now an iterator object
    file.write(
        "Google is an absolute shit\n"  # we need the newline as it's not added by default
    )
# The file is closed here.

# we need the newline as it's not added by default
# We should use exception handling when working with files
# Like below, if file.txt doesnt exist, it will raise FileNotFoundError
try:
    with open("file.txt", "r", encoding="utf-8") as file:
        print(file.read())  # file.read() returns lines
except FileNotFoundError as e:
    print(e)


# The 'w' or write mode completely replaces file's existing content.
# If we wanna append content, we can use 'a' or append mode:
try:
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write("Google is absolute shit\n")
        file.write("google is indded that\n")
except Exception as e:
    print(f"Errror: {e}")


# If we  wanna write to file only if file doesn't exists
# we can use 'x' or exclusive mode
try:
    with open("file.txt", "x", encoding="utf-8") as file:
        file.write("Google is absolute garbage.\n")
except FileExistsError:
    print("Error: File already exists")


# ---------------------- Reading files ----------------------

# Read entire file (as a single string)
try:
    with open("file.txt", "r", encoding="utf-8") as file:
        data = file.read()  # Reads and stores all file's lines as a single string. NEWLINE CHARACTERS INCLUDED
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)


# Read all lines of file (as list)
try:
    with open("file.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()  # Read and stores  all lines as a list of string, Each element contains the newline character
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

print(lines)  # ['google\n' 'is\n', 'shit\n']

# Read a single line
try:
    with open("file.txt", "r", encoding="utf-8") as file:
        line1 = file.readline()  # reads the first line untill the newline character. each line includes the newline character
        line2 = file.readline()  # reads the 2nd line..
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

print(line1.strip(), line2.strip())


# Iterate over lines of a file
try:
    with open("file.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line)
except Exception as e:
    print(f"Error: {e}")


# ================= Using pathlib to read/write file=====================

# For quickly opening and writing/reading a file.
# we can use pathlib

file_path = Path(".cache/ss.txt")

file_path.write_text("google is shit\n")

# Equivalent of:
try:
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("google is shit\n")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)


# Reading:
print(file_path.read_text(), end="")

# Equivalednt to:
try:
    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read(), end="")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
