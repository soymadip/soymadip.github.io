"""
A helpful analogy is to think of yield from like forwarding calls:
    - imported_chai() is another vendor.
    - full_menu() is the manager who says, "First serve everything from the local vendor, then everything from the imported vendor," without manually listing each tea.
    - local_chai() is one tea vendor.
"""


def local_chai():
    yield "Masallla Chai"
    yield "ginger chai"


def imported_chai():
    yield "Macha"
    yield "Ollong"


def full_menu():
    yield from local_chai()  # "Take every value produced by local_chai generator and yield it as if it came from this generator."
    yield from imported_chai()


def chai_stall():
    try:
        while True:
            yield "waiting for chai order"
    except GeneratorExit:
        print("stall closed, No more chai")


stall = chai_stall()

print(next(stall))

stall.close()  #  When close() is called, Python raises a special exception called GeneratorExit inside the generator.
