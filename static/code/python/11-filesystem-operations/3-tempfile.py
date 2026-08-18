# tempfie is for creating temporary files and dirs safely
#

from pathlib import Path
from tempfile import (
    NamedTemporaryFile,
    TemporaryDirectory,
    TemporaryFile,
    gettempdir,
    mkdtemp,
    mkstemp,
)

# Why not just mkdir?
Path("/tmp/my/tmp_file").mkdir()

"""We don't know:

whether it already exists
whether another process created it
whether someone can interfere with it
whether the name is predictable

tempfile handles secure temporary-name generation.
That's one of the main reasons it exists.

"""


# This can have name collisions & security issues
# instead use tempfile
with TemporaryDirectory() as tmp_dir:
    print(tmp_dir)

# After context manager, python automatically cleans up the dir
#
# The tmp_dir is not path.
with TemporaryDirectory() as tmp_dir:
    tmp_path = Path(tmp_dir)
    print(tmp_path.parent)


# TemporaryFile - create temporary files
with TemporaryFile() as tmp_file:  # by default, opens in binary mode
    tmp_file.write(b"google is shit\n")  # tmp_file is a file-like object


# NamedTemporaryFile - create temporary files with a name
with NamedTemporaryFile() as file:
    print(file.name)


# ------- gettempdir() - get the temporary directory --------
#
print(gettempdir())  # returns path as string


# Low level api:

dir = mkdtemp()  # Make temporary dir. accepts optional prefix (filename)
id, path = mkstemp()  # Make temporary file. returns id and path as strings

print(dir)
print(id, path)
