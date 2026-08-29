"""
sometimes the builtin validations aren't enough

pydantic allows you to define custom validators
"""

from uuid import UUID, uuid4

from pydantic import (
    BaseModel,
    EmailStr,
    HttpUrl,
    SecretStr,
    field_validator,
    model_validator,
)
from pydantic.fields import Field


class User(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    username: str
    age: int
    email: EmailStr
    password: SecretStr
    password_confirm: SecretStr

    website: HttpUrl | None = None
    bio: str = ""
    is_active: bool = True

    #
    # check if username is valid
    # We use field_validator and give it a classmethod.
    @field_validator("username")
    @classmethod
    def validate_usrnm(cls, value: str) -> str:

        if not value.replace("_", "").isalnum():
            raise ValueError("username must be alphanumeric (underscores are allowed)")

        if not value.replace("_", "").islower():
            raise ValueError("username must be lowercase")

        # We are stripping trailing whitespace from the username and returning it.
        # If we dont want any transformations, we should just return the value as-is.
        return value.strip()

    #
    #
    # by default, field_validator runs after pydantic's field validation
    # but we can run it before by setting mode="before"
    @field_validator("website", mode="before")
    @classmethod
    def val_web(cls, value: str) -> str:

        value = value.strip()

        if value and not value.startswith(("https://", "http://")):
            return f"https://{value}"

        # if the value does start, return as is
        return value

    #
    #
    # We use model_validator to check a model's fields after instantiation
    @model_validator(mode="after")
    def pass_match(self):
        if self.password != self.password_confirm:
            raise ValueError("password and password_confirm must match")

        return self  # model validator should return self


#
#
# create a user
usr1 = User(
    username="9google",
    age=23,
    email="ss@gmail.com",
    password="google is shit",  # pyright: ignore[reportArgumentType]
    password_confirm="google is shit",  # pyright: ignore[reportArgumentType]
    website="google.com",  # pyright: ignore[reportArgumentType]
)

print(usr1, end="\n\n")
