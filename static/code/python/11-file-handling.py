"""
For file handling, we should use dedicated libraries.

But let's understand python's builtin one
"""

# we can use open method:
file = open(
    "file.txt", "w", encoding="utf-8" # open in write mode. this loads into memory
)


""" ------------- Note --------------

We should almost always pass encoding="utf-8" to open mehtod for compatibility b/w windows and unix.


Only exception is binary files.

with open("image.png", "rb") as f:
    content = f.read()

"""


file.write(  # this completely replaces file's content with given. Creates file if not exists
    "google is shit"
)

file.close()  # close the file.


#  BUT THERE IS MORE EFFICIENT WAY
with open("file.txt", "w", encoding="utf-8") as file:   # file is now an iterator object
    file.write(
        "Google is an absolute shit\n"  # we need the newline as it's not added by default
    )
# The file is closed here.

# we need the newline as it's not added by default
# We should use exception handling when working with files
# Like below, if file.txt doesnt exist, it will raise FileNotFoundError
try:
    with open("file.txt", "r", encoding="utf-8") as file:
        print(file.read())   # file.read() returns lines
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
        file.write("Google is absolute garbage.")
except FileExistsError:
    print("Error: File already exists")



# Iterating over lines of a file
try:
    with open("file.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line)
except Exception as e:
    print(f'Error: {e}')


# =======================================================
"""
what about things like file exists or not etc things?

They are in Pathlib stdlib. will learn later

"""
