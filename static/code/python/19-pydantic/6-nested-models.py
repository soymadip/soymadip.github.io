"""
For complex data structures, we can use nested models.
"""

from datetime import UTC, datetime
from functools import partial
from typing import Literal

from pydantic import BaseModel, EmailStr, Field, SecretStr


class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likes: int = 0


class Author(BaseModel):
    username: str
    email: EmailStr
    age: int
    password: SecretStr


class BlogPost(BaseModel):
    title: str
    content: str
    view_count: int = 0
    is_published: bool = False
    comments: list[Comment] = Field(default_factory=list)
    author: Author

    # default_factory takes a function that is called when creating objects
    tags: list[str] = Field(default_factory=list)  # create new list

    # we need to pass a callable instead of executing now.
    # so we use lambds.
    # functools.partial works too
    created_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))

    # We use Literal type to restrict to a set of values
    status: Literal["draft", "published", "on_hold"]


post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "status": "published",
    "tags": ["pydantic", "models", "nested"],
    "author": {
        "username": "soymadips",
        "email": "sd@gg.com",
        "age": 999,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}


post = BlogPost(**post_data)

# Instead of using dict unpacking,
# Wwe SHOULD use model_validate (or model_validate_json for json data)
post = BlogPost.model_validate(post_data)

print(post.model_dump_json(indent=2))
