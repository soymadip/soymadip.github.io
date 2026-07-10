"""
Infinite generator that simulates a token dispenser.

- Yields incrementing token numbers starting from `start`.
- Accepts input via `send()` to optionally reset the counter to a new value.
- Gracefully stops if `close()` is called.
"""


def token_dispenser(start: int = 1):
    try:
        while True:
            new_start = yield start  # when first next(token) is called, execution starts here. it first sends start value to user then pauses. The new_start doesn't have value yet. Then in next next(token), the new_start gets None.
            if new_start is not None:
                start = new_start
            else:
                start += 1
    except GeneratorExit:
        print("Dispenser closed.")


token = token_dispenser()
