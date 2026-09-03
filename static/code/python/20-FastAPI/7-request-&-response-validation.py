from datetime import UTC, datetime

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from posts import posts
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", app=StaticFiles(directory="static"), name="static-files")


# ------- models shoiuld be in schemas.py -----


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=23)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    model_config = ConfigDict(
        from_attributes=True  # allow pydantic to read data from objects along with dictionaries
    )

    # Adds more on top of the base model
    id: int = Field(ge=1)
    date_posted: str


@app.get("/api/posts", response_model=list[PostResponse])
def get_posts(request: Request):
    if not posts:
        return templates.TemplateResponse(
            request,
            name="error.html",
            status_code=status.HTTP_404_NOT_FOUND,
            context={
                "title": "No posts found",
                "message": "No posts found",
                "status_code": status.HTTP_404_NOT_FOUND,
            },
        )
    return posts


@app.get("/api/post/{id}", response_model=PostResponse)
def get_post(id: int):
    for post in posts:
        if post["id"] == id:
            return post

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.post(
    "/api/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED
)
def create_post(post: PostCreate):
    new_post = {
        "id": max(post["id"] for post in posts) + 1,
        "author": post.author,
        "title": post.title,
        "content": post.content,
        "date_posted": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S"),
    }
    posts.append(new_post)
    return new_post
