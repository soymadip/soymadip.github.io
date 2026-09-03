"""
Path Parameters

path params are a variable that are part of the URL path

Example:
    /api/posts/{post_id}
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from posts import posts  # pyright: ignore[reportImplicitRelativeImport]

app = FastAPI(redoc_url=None)
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static-files")


@app.get("/api")
@app.get("/")
def home(request: Request):
    if request.url.path == "/":
        return {"message": "Welcome to Example"}
    return {"message": "Welcome to the API"}


# This sends all posts
@app.get("/api/posts/")
def get_posts():
    return posts


# We use path params to get a specific post by id
# We declare path params in decorator path with {param} & same param in function signature with type.
# FastAPI will automatically verify, convert the path param to the type specified in the function signature
# if post_id is not an integer, FastAPI will raise a 422 Unprocessable Entity response
@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post

    return {"error": "post not found"}
    # This is not the right way. it sends a 200 OK response
    # We will learn about HTTP status codes later


@app.get("/posts")
def show_posts(request: Request):
    return templates.TemplateResponse(
        request, name="home.html", context={"posts": posts}
    )


@app.get("/posts/{post_id}")
def post_page(request: Request, post_id: int):

    for post in posts:
        if post["id"] == post_id:
            title: str = post["title"][:50]  # Truncate title to 50 characters

            return templates.TemplateResponse(
                request,
                name="post.html",
                context={"title": title, "post": post},
            )

    return templates.TemplateResponse(
        request,
        name="error.html",
        context={"status_code": "404", "message": "Post Not Found"},
    )
