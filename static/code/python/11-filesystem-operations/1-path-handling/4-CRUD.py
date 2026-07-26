# In this, we will see how to actually create/update/delete/rename files/dirs

from pathlib import Path

#
# ------------ Make directory -------------

docs_dir = Path("wiki/")


docs_dir.mkdir()

# Skip creation if dir exists
#
docs_dir.mkdir(exist_ok=True)

#
# If the dir has parents dir that needs to be created
#
a_dir = Path("parent/child/")

a_dir.mkdir(parents=True, exist_ok=True)


# --------------- Making Files ---------------

a_file = Path("path/to/file")

# first create parent dirs
a_file.parent.mkdir(exist_ok=True, parents=True)

# Now create the file
# exists_ok=True tells to skip if it's there. without this, updates timestamp of the file
#
a_file.touch(exist_ok=True)


# If you wanna write any text in the file instead of creating empty file
a_file.write_text("google is shit")


# or binary data
# a_file.write_bytes(binary_data)


# ---------------------- Renaming a file -----------------------------

# We use replace() method for renaming a file
# We can use .rename() method too but it has inconsistent behavior across OSs

file3 = Path(".cache/file2.txt")
target = file3.with_name("google.json")

if target.exists():
    file3.replace(target)
    file3 = target


# ------------------ Delete a file/dir ------------------------------

file4 = Path(".cache/file2.txt")
dir4 = Path('.cache/config')

# delete a file
file4.unlink()

# delete a EMPTY directory
# if dir is not empty, it will raise OSError
dir4.rmdir()