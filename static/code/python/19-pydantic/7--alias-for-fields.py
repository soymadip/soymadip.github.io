from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, EmailStr, Field, SecretStr


class User(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,  # tell pydantic to accept both field names and aliases
        strict=True,  # disable field cohorsion ()
        from_attributes=True,  # allow pydantic to read data from objects too
    )

    uid: UUID = Field(alias="id", default_factory=uuid4)
    username: str
    email: EmailStr
    age: int
    password: SecretStr


user_data = {
    # We can use id or uid as the field name
    "id": "3bc4bf25-1b73-44da-9078-f2bb310c7374",
    #
    # rest goes like usual
    "username": "Corey_Schafer",
    "email": "CoreyMSchafer@gmail.com",
    "age": "39",
    "password": "secret123",
}

user = User.model_validate(user_data)


# internally, uid is the field name
print(user.uid)

# When dumping, use by_alias=True to use the alias name
print(user.model_dump(by_alias=True))
print(user.model_dump_json(by_alias=True, indent=2))


# Excluding fields
print(user.model_dump(by_alias=True, exclude={"password"}))

# Include specific fields
print(user.model_dump(by_alias=True, include={"uid", "username", "email"}))
