# ----------------------- Any Type ------------------
import random
from typing import Any

# For indicating that a value can be of any type


def random_choose(mp: list[Any]) -> Any:
    return random.choice(mp)  # pyright: ignore[reportAny]


# But this has a problem.
# With Any, IDE auto-completion doesn't work as expected

# --------------------- TypeVars ------------------

# To handle this, we can use TypeVars


# So we are saying that T can be any type, and the function returns a T type


def random_chose[T](mp: list[T]) -> T:
    return random.choice(mp)


ss: int = random_chose([1, 2, 3, 4, 5])  # Returns an int
sd: str = random_chose(["a", "b", "c", "d", "e"])  # Returns a str

# IDE completion works as expected

# NOTE: in python <3.12, this syntax is not supported.
# Instead, use `from typing import TypeVar` and `T = TypeVar("T")`
