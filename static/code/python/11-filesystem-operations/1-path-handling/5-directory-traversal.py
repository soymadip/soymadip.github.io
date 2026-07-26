# In this chapter will learn how to iterate over each file/dir of a dir.


# Think of dir as a tree:
#
# /home/soymadip/
#   │
#   ├── Documents/
#   │   ├── notes.txt
#   │   ├── image.png
#   │   └── report.pdf
#   │
#   ├── Downloads/
#   │   └── movie.mp4
#   │
#   └── Projects/
#       ├── app.py
#       └── README.md
#
#
# Directory traversal means walking thorough this tree


from pathlib import Path

# ------------- non-recursive traversal - iterdir() -------------

# This is the simplest
#
# Documents/
#   │
#   ├── subdir/
#   ├── notes.txt
#   ├── image.png
#   └── report.pdf

docs = Path(".cache")

# iterdir returns an iterator
for item in docs.iterdir():
    print(item)
print()

# Output:
#   Documents/notes.txt
#   Documents/image.png
#   Documents/subdir
#   Documents/report.pdf
#
# - Each output is a path obj.
# - Also order is not guaranteed
# - Hidden directories/files are also listed
#
# - ONLY TOP LEVEL DIRS/FILES ARE LISTED
#   this is NOT RECURSIVE

# We can convert it to list if we want list
# Each item of the list will be a path object
items = list(docs.iterdir())


# to sort file/dir we have to manually do:
for item in docs.iterdir():
    if item.is_file():
        print(item)


#
# ------------ pattern search - glob*() --------------------

# path.glob() is used to search files & dir with specific pattern within a directory
# It returns a iterator

cache_dir = Path(".cache/")

print()

for item in cache_dir.glob("*.json"):  # return only json files
    print(item)

# make the glob matching case insensitive
for item in cache_dir.glob("code*", case_sensitive=False):
    print(item)  # matches: coder, Coder, code.txt


# common glob patterns:
#
#      *             All files and directories inside folder (top-level only).
#    *.json          Only files ending in .json inside folder.
# file_[0-9].txt     Files matching wildcards/ranges (e.g., file_1.txt, file_2.txt).
#


## Recursive match: rglob()
for item in cache_dir.rglob("code*", case_sensitive=False):
    print(item)  # matches: coder, Coder, code.txt, subdir/CODER_TXT


## LIST ALL FILES AND DIRS Recursively
for item in cache_dir.rglob("*"):
    print(item)


cache_dir = Path(".code")

print("------")
print(Path.cwd())

for root, dirs, files in cache_dir.walk():
    print()
    print(f"Directory: {root}")
    print(f"Subfolders: {dirs}")
    print(f"Files: {files}")


# --------------- Walk() --------------------

