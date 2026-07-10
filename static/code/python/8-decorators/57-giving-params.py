from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result

    return wrapper


@log_activity
def brew_chai(type):
    print(f"Brewing {type} chai")


brew_chai("masalla")


## We can add as many params as we need
@log_activity
def greet(name, age):
    print(f"Welcome {name}: {age}")


greet("Soumadip Das", age=12)
