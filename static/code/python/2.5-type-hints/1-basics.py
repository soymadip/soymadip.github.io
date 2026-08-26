"""
Type hinting is a way to specify the expected type of a variable

Types are not enforced by the interpreter but are used by static type checkers like Ruff, mypy etc.

"""

# ----------------- primitives ------------------

name: str = "soymadip"
age: int = 12
weight: float = 70.5
is_active: bool = True


#
# ------------------ collections ------------------

array: list[int | str | float] = [12, "soymadip", 80.5]

# '|' is union operator. used to specify multiple types for a variable

# dict[key_type, value_type]
map: dict[str | int, int | str] = {"soymadip": 12, 0: "google", "age": 12}


# tuple[type1, type2], only two types are allowed
tpl: tuple[int, str] = (12, "soymadip")

# to allow unlimited lengths, use tuple[type1, ...]
tpl2: tuple[int | str | float, ...] = (12, "soymadip", 80.5)


#
# ------------------ Functions ------------------

# def func_name(param1: type1, param2: type2) -> return_type:


def create_user(name: str, age: int | None = None) -> dict[str, int | str | None]:
    return {"name": name, "age": age}


# Above function cleary describes:
#  - name is a string
#  - age is an integer
#  - the return value is a dictionary with string keys and values of type int, str, or None
#      '|' is used to specify OR
