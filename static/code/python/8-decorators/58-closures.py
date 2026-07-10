from functools import wraps


def cache_results(func):
    cache = {}

    @wraps(func)
    def cacher(a: int, b: int):
        key = (a, b)

        if key in cache:
            return f"From Cache: {cache[key]}"

        result = func(a, b)
        cache[key] = result
        return f"Computed: {result}"

    return cacher  # This is a closure


## Why don't we need to define the operation in the dict's key?

# Each decorated function gets its own `cacher` function.
#
# Think of it like this:
#
# @cache_results
# def multiply(a, b):
#     ...
#
# is equivalent to:
#
# multiply = cache_results(multiply)
#
# Every call to cache_results() creates a NEW `cacher` function object.
#
# Since `cache` is a default argument of `cacher`,
# Each `cacher` gets its own dictionary.
#
# So:
#
# multiply -> cacher #1 -> cache {(2, 3): 6}
# add      -> cacher #2 -> cache {(2, 3): 5}
#
# The caches are already separated by function, so the key only
# needs to identify the arguments:
#
#     key = (a, b)
#
# We don't need:
#
#     key = (func, a, b)
#
# because multiply() and add() never share the same cache.


## CAll
@cache_results
def multiply(a: int, b: int) -> int:
    return a * b
