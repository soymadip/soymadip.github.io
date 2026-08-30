from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, EmailStr, Field, SecretStr


class User(BaseModel):
    model_config = ConfigDict(
        strict=True,  # disable field cohorsion ('10' -> 10)
        extra="allow",  # allow extra fields that are not defined, set to 'forbid' to raise an error
        validate_assignment=True,  # Revalidate on making changes
        frozen=True,  # Make the model immutable (raises an error if fields are modified)
    )

    uid: UUID = Field(alias="id", default_factory=uuid4)
    username: str
    email: EmailStr
    age: int
    password: SecretStr


# ---------------- Strict Mode ----------------

user_data = {
    "age": "39",  # Fails in strict mode
    "username": "Corey_Schafer",
    "email": "CoreyMSchafer@gmail.com",
    "password": "secret123",
}

print(User.model_validate(user_data))


#
# --------------- Extra Fields ----------------

user_data = {
    "age": 39,
    "username": "Corey_Schafer",
    "email": "CoreyMSchafer@gmail.com",
    "password": "secret123",
    "extra_field": "extra value",  # Extra field allowed
}

print(User.model_validate(user_data))


#
# ----------------- Revalidate on assignment ----------------

user = User.model_validate(user_data)

user.email = "notAnEmail"  # rechecked here. raises a validation error


#
# -------------------- Frozen model ----------------


# After frozen=True, this raises 'instance is frozen' validation error
user.email = "shit"
