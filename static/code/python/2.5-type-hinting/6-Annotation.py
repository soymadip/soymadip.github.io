"""
In python, Annotated is used to attach metadata to type hints without changing how type checkers evaluate actual type.
"""

from typing import Annotated

# Example
Age = Annotated[int, "must be an positive", lambda x: x > 0]  # pyright: ignore[reportUnknownLambdaType]

# To type checkers, it's just an int.
# The extra metadata is ignored by them but can be read & used by runtime libraries / code

from typing import get_args, get_origin

print(get_origin(Age))  # typing.Annotated

print(get_args(Age))
# (<class int>, "must be an positive", <function <lambda> at 0x7fd39d9a3270>)


# ------------------------ Using Annotated metadata --------------------


# Create a class for rule
class MinVal:
    def __init__(self, limit: int):
        self.limit: int = limit


# create Annotated type
Adult = Annotated[int, MinVal(18)]


def validate_age(value: int, target_type) -> bool:

    # get_args(target_type) returns a tuple: (int, MinVal(18))
    metadata = get_args(target_type)[1:]

    for rule in metadata:
        if isinstance(rule, MinVal) and value < rule.limit:
            print(f"Rejected: {value} is under the limit of {rule.limit}.")
            return False

    print(f"Approved: {value} meets all rules.")
    return True


_ = validate_age(12, Adult)
