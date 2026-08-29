"""
Pydantic has built-in types to validate common data types.

In many cases, they are aliases of Annotated .

# For all types head to https://pydantic.dev/docs/validation/latest/api/pydantic/types/

"""

from datetime import UTC, datetime
from functools import partial
from uuid import UUID, uuid4

# We need to install pydantic[email] for these
from pydantic import BaseModel, EmailStr, HttpUrl, SecretStr

# impoat field
from pydantic.fields import Field


class User(BaseModel):
    uid: UUID = Field(default_factory=uuid4)

    username: str

    # By default, the value is hidden.
    # can be acccessed with .get_secret_value()
    password: SecretStr = Field(min_length=8, max_length=128)

    # Auto validates email standard
    email: EmailStr

    # Validates URL standard
    website: HttpUrl | None = None

    created_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))


if __name__ == "__main__":
    usr1 = User(username="soymadio", email="soymadio@em.com", password="google")  # pyright: ignore[reportArgumentType]
    print(usr1)

    # The secret string is hidden by default, but can be accessed.
    print(usr1.model_dump_json(indent=2))
    print(usr1.password.get_secret_value())
