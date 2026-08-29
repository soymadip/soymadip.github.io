"""
Pydantic is Python’s most popular data validation and parsing library.

Instead of writing manual checks to make sure incoming data (like JSON from an API, environment variables, or user input) is formatted correctly,
Pydantic handles it automatically using standard Python type hints.

It also does settings management


NOTE: we are using pydantic v2, v1 has different methods that are deprecated now
"""

# ------------ Without Pydantic --------

# Let's say we need to create a user, and we want to make sure the data is valid.

from typing import Any


def create_user(id: int, name: str, is_active: bool) -> dict[str, str | int | bool]:

    if not isinstance(id, int):
        raise TypeError("id must be an int")

    if not isinstance(name, str):
        raise TypeError("name must be a str")

    if not isinstance(is_active, bool):
        raise TypeError("is_active must be a bool")

    return {
        "id": id,
        "name": name,
        "is_active": is_active,
    }


user = create_user(
    id=101,
    name="soyma",
    is_active=True,
)

print(user)


# --------------------- With Pydantic -----------------------
#
# This becomes easier with Pydantic's BaseModel

# we import BaseModel from pydantic
from pydantic import BaseModel, Field


# Then We inherit from BaseModel
# Each class is called a "model"
class User(BaseModel):
    uid: int
    name: str
    is_active: bool


# now we create a object of user by unpacking dict
user = User(
    uid=1,
    name="soyma",
    is_active=True,
)

# gives ValidationError in for example is_active is anytype other than bool
#

# Pydantic tries to type convert the values to the correct types by default
user2 = User(
    uid="1",  # auto converts to int
    name="soyma",
    is_active=False,
)

print(user)


# -------------------------  Default Values --------------- -------

# We can set default values for fields
# If an optional field is not provided, the default value will be used


class Product(BaseModel):
    uid: int
    name: str
    code: str | None = None
    desc: str = ""
    price: float
    in_stock: bool = True


product1 = Product(uid=1, name="fuck charger", price=1000)
product2 = Product(uid=2, name="sonaii", price=99.9, in_stock=False)

# This gives Error
# product2 = Product(name="sonaii")

# We acccess values with dot notation.
print(
    f"\nProduct 1's info:\n   Name: {product1.name}\n   desc: {product1.desc if product1.desc else 'N/A'}\n   In Stock: {product1.in_stock}"
)


#
# We can also get the values as dict / json

# dict
print(product2.model_dump())

# json

print(product2.model_dump_json(indent=2))
