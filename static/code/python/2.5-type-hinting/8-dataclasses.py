"""
If we are working with existing dictionaries, TypedDict is ok.

But for new code, dataclasses are better.

They provide a more structured way to define data.

"""

from dataclasses import dataclass
from typing import NewType

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])


@dataclass
class User:
    name: str
    age: int

    mail: str | None = None  # optional
    fav_color: RGB | HSL | None = None  # optional


# we create a user by creating an instance of the User class
usr1 = User(
    name="soymadip",
    age=20,
    fav_color=RGB((255, 0, 0)),
)

# we can access the user's attributes
print(usr1.name, usr1.mail, usr1.fav_color)


# In func
def create_user(name: str, age: int) -> User:
    return User(name=name, age=age)


usr2 = create_user("soymadip", 30)
print(usr2.name, usr2.age)
