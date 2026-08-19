from pathlib import Path

#
# ---------- Exception Chaining ------------
#
# Exception chaining preserves the original exception when raising
# a new exception from inside an except block.
#
# Use `from exc` to explicitly specify the original exception as
# the cause of the new exception.


def read_config(path: Path) -> str:
    try:
        return path.read_text()
    except FileNotFoundError as exc:
        raise ValueError("config file is missing") from exc


# If path.read_text() raises FileNotFoundError:
#
#     FileNotFoundError
#            ↓
#       ValueError
#
# `from exc` sets the original exception as `__cause__`.
#
# The original exception can be accessed with:
#
#     exception.__cause__


# --------- Implicit Exception Chaining ------------

try:
    ss: int = int("abc")
except ValueError:
    raise RuntimeError("conversion failed")

# Python automatically keeps the original exception as `__context__`.
#
#     ValueError
#          ↓
#     RuntimeError
#
# `__context__` is used when an exception occurs while another
# exception is being handled.


# --------- Explicit Exception Chaining ------------

try:
    int("abc")
except ValueError as exc:
    raise RuntimeError("conversion failed") from exc

# `from exc` explicitly sets:
#
#     RuntimeError.__cause__ = exc
#
# This tells Python that the first exception was the direct cause
# of the second exception.


# --------- Suppress Exception Chaining ------------

try:
    int("abc")
except ValueError:
    raise ValueError("value must be an integer") from None

# `from None` suppresses the display of the original exception
# in the traceback.
#
# Useful when the original exception is only an implementation
# detail and should not be exposed to the caller.


# --------- Summary ------------

# raise NewError(...)              -> implicit __context__
# raise NewError(...) from exc     -> explicit __cause__
# raise NewError(...) from None    -> suppress chained traceback
#
# Prefer `from exc` when translating a low-level exception into
# a more meaningful application-level exception.
