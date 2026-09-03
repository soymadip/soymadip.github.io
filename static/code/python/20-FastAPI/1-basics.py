from fastapi import FastAPI
from posts import posts

# This app object is wrapped around the FastAPI class
# The params are only for the docs (OpenAPI).
app = FastAPI(
    title="FastAPI Basics Example",
    version="1.1.0",
    description="A comprehensive example of FastAPI basics. And beginning of a journey.",
    redoc_url=None,
)


# app.get decorator defines a route.
# '/' means the root path
@app.get("/")
def home():

    # WE return a dict.
    # FastAPI converts it to JSON automatically.
    return {"message": "Hello World!"}


"""
Btw, we are not using async for now.

FastAPI handles async and sync both.
"""


@app.get("/api/posts")
def get_posts(id: int | None = None):
    if id:
        for post in posts:
            if post["id"] == id:
                return post
        return "Not Found"

    return posts


# ------------------------- Return HTML ----------------------------

# so far we were only returning JSON data.
# To return HTML, we can use the `Response` class.

from fastapi.responses import HTMLResponse


# We can use the `HTMLResponse` class to return HTML.
@app.get("/h1", response_class=HTMLResponse)
def html():
    return f"<h1>{posts[0]['title']}</h1>"


# To have several routes that return same page, we stack them
@app.get("/html", response_class=HTMLResponse)
@app.get("/hml", response_class=HTMLResponse)
def ht():
    return f"<h1>{posts[0]['title']}</h1>"


# -------------- Hiding routes from docs ------------


# We can use the `include_in_schema` parameter to hide routes from the docs.
@app.get("/hidden", include_in_schema=False)
def hidden():
    return f"<h1>{posts[0]['title']}</h1>"


#
#
#
# ============================================================
#
# To run the application, we use:
# fastapi dev main.py


# Also we can access automatic generated docs at: /docs or a newer one at /redoc
