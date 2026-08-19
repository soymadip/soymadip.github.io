from pathlib import Path

"""
A file is not the file content itself. it's actually a name pointing to filesystem object.

filename
   │
   ▼
directory entry
   │
   ▼
inode
   │
   ├── file contents
   ├── permissions
   ├── owner
   ├── timestamps
   └── other metadata

"""


file: Path = Path("ss.txt")

_ = file.write_text("google is shit\n")  # writing to inode


"""
What is an Inode?

on unix systems, inodes store metadata about the filesystem object
The file name is stored in a dir structure that points to inode.
"""

path: Path = Path("ss/ss.txt")

info = path.stat()

print(info.st_ino)
print(info.st_nlink)  # number of hardlinks (directory entry) of that file's inode


"""
A directory is itself a filesystem object with an inode.

The directory entry (its name in its parent directory) points to the directory's inode.

The inode stores metadata about the directory.
"""

# ----------- Creating a Hardlink ----------------

original = Path("ss/ss.txt")

link = original.with_name("ss.c")  # now ss/ss.c

link.hardlink_to(original)  # creates a hardlink from ss/ss.c to ss/ss.txt


if original.stat().st_ino == link.stat().st_ino:
    print(f"Same Inode: {original.stat().st_ino}, {link.stat().st_ino}")


"""
How is symlinks differ from hardlinks?

- Symlinks have their own filesystem object/inode. Each inode stores metadata about the symlink itself and the file it points to.

- Hardlinks share the same inode as the original file. They are just different directory entries pointing to the same inode.

"""


# Python gives a method to check if underlying inode is same:

print(original.samefile(link))

"""
What happens if we delte the original file?

The hardlink still points to the same inode, so the file is still accessible.


This is why 'deleting a file/dir' is misleading. Linux doesnt destroy the data immediately, it just removes directory entry.
"""
