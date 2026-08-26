"""
In Pydantic, Field (imported from pydantic) is used to:
    add validation rules,
    default values,
    metadata,
    custom behavior

to individual model attributes.

"""

from datetime import UTC, datetime
from typing import Literal

from pydantic import BaseModel, Field

#
#
# -------------- Giving Default values -----------------


class BlogPost(BaseModel):
    title: str
    content: str
    view_count: int = 0
    is_published: bool = False

    # default_factory takes a function that is called when creating objects
    tags: list[str] = Field(default_factory=list)  # create new list

    # we need to pass a callable instead of executing now.
    # so we use lambds.
    # functools.partial works too
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # We use Literal type to restrict to a set of values
    status: Literal["draft", "published", "on_hold"]


# creating a new post
my_post = BlogPost(
    title="My Post",
    content="google is shit",
    tags=["google", "shit", "now-shit", "garbage"],
    status="published",
)


print(my_post.tags)


#
# --------------------- Adding Constraints -----------------

from typing import Annotated
