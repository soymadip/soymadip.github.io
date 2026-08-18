import os
from pathlib import Path

#
# ---------- Check if the path (file/dir) exists ------------

a_dir = Path("docs")

print(a_dir.exists())  # True if a_dir exists


# --------- Create symlink  & hard link ------------
#
pth = Path("google")

pth.symlink_to("docs")  # creates a symlink named 'google' pointing to 'docs'
pth.hardlink_to("docs")  # creates a hard link named 'google' pointing to 'docs'

print(pth.is_symlink())  # True


# Note: os module has a symlink method too.
os.symlink("target", "link_name")


# ---------- Check if the Path is file/dir/symlink or absolute path------------

a_file = Path("~/.cache/zsh/history").expanduser()


if a_dir.is_dir():
    print("is a dir")  # check if directory, (even if it's a symlink)

if a_file.is_file():
    print("is a file")  # check if a file (even if it's a symlink)

if a_file.is_absolute():
    print("is a absolute path")  # check if the path absolute path

if a_file.is_symlink():
    print("is a symlink")  # check if a symlink (dir/file)


#
# ---------- Resolve a path  ------------

a_relative_path = Path("../qukrun").resolve()
a_symlink = Path(".cache/file.txt").resolve()  # symlink to .git/config

print(a_relative_path)  # /home/soymadip/Projects/quikrun

print(a_symlink)  # also resolve symlinks (/home/soymadip/Projects/.git/config)


#
#
# ----------  Check if samefile (if same filesystem object) ------------

a = Path(".git/config")
b = Path(".cache/file.txt")

print(a.samefile(b))  # True
