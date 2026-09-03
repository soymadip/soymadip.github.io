"""
In this, we will learn about error handling in FastAPI.
"""

from time import sleep

from fastapi import FastAPI, HTTPException, Request, responses, status
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from posts import posts  # pyright: ignore[reportImplicitRelativeImport]

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static-files")


@app.get("/", include_in_schema=False)
@app.get("/api", include_in_schema=False)
def home(request: Request):
    if request.url.path == "/":
        return "Welcome to the API"
    return "Please go to /posts or /api/posts"


@app.get("/test-delay")
def test_delay():
    sleep(2)  # Every request takes 2 seconds to compute
    return {"status": "done"}


# NOTE: designing routes this way is not recommended. i am using here for convenience of learning
# DO NOT MIX API AND NON-API ROUTES

"""
Let's handle error & responses of previous lesson gracefully
"""


@app.get("/posts", name="posts", include_in_schema=False)
@app.get("/api/posts", name="api_posts")
def get_posts(request: Request):
    """Get all posts"""
    if request.url.path.startswith("/api"):
        return posts

    return templates.TemplateResponse(
        request, "home.html", context={"title": "Posts", "posts": posts}
    )


@app.get("/posts/{post_id}", name="post_page", include_in_schema=False)
@app.get("/api/posts/{post_id}", name="api_post_page")
def post_page(request: Request, post_id: int):
    """Get a single post by ID"""
    for post in posts:
        if post["id"] == post_id:
            if request.url.path.startswith("/api"):
                return post

            return templates.TemplateResponse(
                request, "post.html", context={"title": "Post", "post": post}
            )

    #
    # Now if the id is not there

    ## For api request We will raise HttpException
    if request.url.path.startswith("/api"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} not found",
        )

    ## For User requests,
    ## we will return an error template with status_code
    return templates.TemplateResponse(
        request,
        name="error.html",
        status_code=status.HTTP_404_NOT_FOUND,
        context={
            "title": "Error",
            "status_code": status.HTTP_404_NOT_FOUND,
            "message": f"Post with id {post_id} not found",
        },
    )


#
# -------------------- Global Error Handling -----------------------
#
# What if user goes to /non-existent-page ?
# Till now, a plain 'not found' response was returned
# But we can do better

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


# Handle HTTP exceptions (like wrong paths)
# why starlette?
# Because fastapi is built on top of it
# And starlette provides the HTTPException class
# So it's better to handle automatic errors from starlette
@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):

    # Again not good idea to manually inspect the URL path
    # Same for manual json responses
    if "/api/" in request.url.path:
        return JSONResponse(
            status_code=exception.status_code,
            content={
                "detail": exception.detail,
            },
        )

    return templates.TemplateResponse(
        request,
        name="error.html",
        status_code=exception.status_code,
        context={
            "status_code": exception.status_code,
            "title": exception.status_code,
            "message": exception.detail,
        },
    )


#
# Handle validation errors
# Validation error have list o
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()},
        )

    return templates.TemplateResponse(
        request,
        name="error.html",
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        context={
            "title": "Validation Error",
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid request, Please check your input and try again.",
        },
    )
