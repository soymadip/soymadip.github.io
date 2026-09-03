"""
Instead of raw html strings, we can use Jinja2 templates.

Jinja2 templates are HTML files with placeholders
that are replaced with actual values at runtime.

This is more manageable than raw html strings.
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from posts import posts  # pyright: ignore[reportImplicitRelativeImport]

app = FastAPI(redoc_url=None)


# Templates Directory
templates = Jinja2Templates(directory="templates")

# Mount static dir as /static
# The name is optional and for using in templates
app.mount(path="/static", app=StaticFiles(directory="static"), name="static-files")


cntxt = {"posts": posts}


@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html", context=cntxt)


# When using url_for('home'), it gives /post as it is after home decorator.
# We can use name prop to eliminate this.

"""
In templates, we can use url_for('name', path='path')

By default, the name is taken from function name. but we can pass name param manually to decorator
This name is picked by docs too.

"""


@app.get("/test", name="testing")
def test(request: Request):
    return {
        "user_agent": request.headers.get("user-agent"),
        "cookies": request.cookies,
        "host_ip": request.client.host,
        "endpoint": request.url,
    }
