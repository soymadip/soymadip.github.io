from pathlib import Path

#
# --------------- Get File/Dir Name & stem --------------------

file1 = Path(".cache/file.txt")
dir1 = Path(".cahche/a_dir")

print(file1.name, dir1.name)  # -> file.txt   a_dir

print(file1.stem, dir1.stem)  # -> file   a_dir

print(file1.suffix, dir1.suffix)  # -> .txt   (returns empty for dirs)


# If the file has multiple suffixes
tar_file = Path(".cache/compressed.tar.gz")

print(tar_file.suffix)  # -> .gz (gives last suffix)
print(tar_file.suffixes)  # -> [ '.tar', '.gz' ] (returns LIST of suffixes)

#
# --------------- Getting parent dir --------------------

file3 = Path(".cache/grand_grand_parent/grand_parent/parent/file.txt")

print(file3.parent)  # .cache/parent/sub_parent/child

# getting parent's parent
# (btw, this returns another Path object)

print(file3.parent.parent)  # .cache/parent/sub_parent

# We can also use .parents[n] to get
#
print(file3.parents[0])  # .cache/grand_grand_parent/grand_parent/parent
print(file3.parents[1])  # .cache/grand_grand_parent/grand_parent
print(file3.parents[2])  # .cache/grand_grand_parent


#
# --------------- Create new path with... --------------------

a_file = Path(".cache/file.txt")
a_dir = a_file.parent

## New path WITH SUFFIX CHANGED
# If a dir, adds after the last dir
#
print(a_file.with_suffix(".gogle"))  # .cache/file.google
print(a_dir.with_suffix(".google"))  # .cache.google

print(a_dir.with_suffix(".google").is_dir())  # True

## New path with FILENAME/DIRNAME CHANGED
#
print(a_file.with_name("gogle.json"))  # .cache/google.json
print(a_dir.with_name("another_dir"))  # another_dir


## New path with STEM CHANGED
print(a_file.with_stem("changed_file"))  # .cache/changed_file.txt
print(a_dir.with_stem("changed_stem"))  # changed_stem


#
# --------------- Create new path with... --------------------
# 
# Raises ValueError if path is not SubPath of path with being compared

niri_path = Path("/home/soymadip/.config/niri/config.kdl")

print(niri_path.relative_to(Path.home()))  # .config/niri/config.kdl
