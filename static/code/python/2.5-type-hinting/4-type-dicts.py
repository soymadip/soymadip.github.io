from typing import NewType

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])


# Types aliases have no individual type checking.
type Usr = dict[str, int | str | RGB | None]


def crt_usr(
    name: str,
    age: int,
    fav_color: RGB | None = None,
) -> Usr:

    return {
        "email": f"{name}@example.com",
        "name": name,
        "age": str(age),  # although we are returning age as int, type checker is fine
        "fav_color": fav_color,
    }


#
# To fix this, we use TypeDict

from typing import TypedDict


class User(TypedDict):
    name: str
    email: str
    age: int
    fav_color: RGB | HSL


def create_user(
    name: str,
    age: int,
    fav_color: RGB | None = None,
) -> User:

    return {
        "email": f"{name}@example.com",
        "name": name,
        "age": str(age),  # Now Type checker gives error.
        "fav_color": fav_color,
    }


#
#
# Frankly, instead of TypedDict, dataclass is better.
