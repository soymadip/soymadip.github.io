"""
Up untill now, we were just receiving request, looking up db and returning with GET method.

Now, we are adding a POST method to create new posts.
"""

from datetime import UTC, datetime
from functools import partial

from fastapi import FastAPI, Request, status
from posts import posts
from pydantic import BaseModel, Field, computed_field

app = FastAPI()


class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True
    author: str


class Post(PostCreate):
    id: int
    date_posted: datetime = Field(default_factory=partial(datetime.now, tz=UTC))


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=Post)
def create_post(request: Request, post: PostCreate):
    posts.append(
        {
            "id": max(post["id"] for post in posts) + 1,
            "date_posted": datetime.now(tz=UTC),
            "title": post.title,
            "content": post.content,
            "published": post.published,
            "author": post.author,
        }
    )

    return posts[-1]


@app.get("/posts")
def read_posts():
    return posts
