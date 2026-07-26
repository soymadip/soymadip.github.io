from datetime import UTC, datetime
from pathlib import Path

#
#
# ---------------- File metadata  -----------------


# we use path.stat() to get file/dir metadata
# it returns a os.stat_result object containing
# size, creating time, last modified info, owner info etc.
#
# It queries os directly, giving most accurate & lower level info
#
# IF THE FILE IS A SYMLINK, it follows it automatically.
# To see the link's stat, pass folllow_symlink=False


file = Path(".cache/ss.txt")

# Fetch metadata
file_info = file.stat(follow_symlinks=False)


print(f"Last Access Time: {datetime.fromtimestamp(file_info.st_atime, tz=UTC)}")
print(f"Permission: {file_info.st_mode}")
print(f"Size: {file_info.st_size / (1024**2):.3f} MB")
print(f"Last modified: {file_info.st_mtime} [ unix timestamp (epoch) ]")


"""
commonly used info:

| Attribute  | What It Means                                                     | Unit / Format                  |
| ---------- | ----------------------------------------------------------------- | ------------------------------ |
| st_size    | File size                                                         | Bytes                          |
| st_ctime   | Metadata change time (Linux/macOS) **or** creation time (Windows) | Unix Epoch timestamp (seconds) |
| st_mtime   | Last content modification time                                    | Unix Epoch timestamp (seconds) |
| st_atime   | Last access time                                                  | Unix Epoch timestamp (seconds) |
| st_mode    | File type and permission bits                                     | Integer / Bitmask              |
| st_uid     | User ID of the owner (Unix only)                                  | Integer ID                     |
| st_gid     | Group ID of the owner (Unix only)                                 | Integer ID                     |
| st_nlink   |  Number of hardlinks pointing to the same inode                   | Integer                        |

NOTE: st_size for dir DOESN'T GIVE ACTUAL TOTAL SIZE OF THE DIR'S FILES. it just gives dir's metadata's size

"""

# ------------- common use cases ----------------

# convert datetime to human redable format

print(
    f"File Creation Time: {datetime.fromtimestamp(file.stat().st_ctime, tz=UTC):%y-%m-%d}"
)
