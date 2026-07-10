"""
Make a decorator that takes a role and check if user is authorized to execute the function
"""

from functools import wraps


def require_admin(func):

    @wraps(func)
    def wrapper(role):
        if role.lower() != "admin":
            print("you are not authorized to access.")
        else:
            return func(role)

    return wrapper


@require_admin
def access_inventory(role):
    print("Access to inventory Granted")


access_inventory("user")
access_inventory("admin")
