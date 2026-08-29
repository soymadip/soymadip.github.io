from pydantic import BaseModel, EmailStr, Field, HttpUrl, SecretStr, computed_field

"""
Sometimes we need to compute a field based on other fields.

To do that, we use the `@computed_field` decorator and a regular property.

This helps when we need to compute a field based on other fields.

"""


class User(BaseModel):
    username: str
    email: EmailStr
    password: SecretStr
    age: int = Field(ge=9)
    website: HttpUrl | None = None

    first_name: str = ""
    last_name: str = ""
    follower_count: int = 0

    # computing display name
    @computed_field
    @property
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"

        return self.username

    @computed_field
    @property
    def is_influencer(self) -> bool:
        return self.follower_count >= 100000


inflncr = User(
    username="inflncr",
    email="ss@ss.com",
    age=30,
    password="google is shit",  # pyright: ignore[reportArgumentType]
    follower_count=100000,
    first_name="influncer",
    last_name="doe",
)

print(inflncr)
