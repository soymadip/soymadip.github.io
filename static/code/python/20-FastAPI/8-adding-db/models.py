from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=120)


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    image_file: str | None = None
    image_path: str


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    # author: str = Field(min_length=1, max_length=100)


class PostCreate(PostBase):
    user_id: int  # Temporary


class PostResponse(PostCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user: int
    date_posted: str
    author: UserResponse
