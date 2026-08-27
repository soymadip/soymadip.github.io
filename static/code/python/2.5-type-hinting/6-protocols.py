"""
In languages like java, we have interfaces. We use them to define a contract for a class.

Protocols are similar to interfaces, but they are more flexible.
"""

import time
from typing import Protocol


class Drivable(Protocol):
    speed: float

    # we use ... to indicate a method signature
    def accelerate(self, ammount: int) -> None: ...

    def stop(self) -> None: ...


# Any class that defines the speed attributes, implements accelerate and stop methods
# automatically satisfies the Drivable protocol
class Car:
    def __init__(self):
        self.speed: float = 0

    def accelerate(self, ammount: int) -> None:
        self.speed += ammount

    def stop(self) -> None:
        self.speed = 0


# We can use the protocol as an accept type to indicate that a function expects a Drivable object
#
def test_vehicle(vehicle: Drivable) -> None:
    vehicle.accelerate(10)

    time.sleep(5)
    vehicle.stop()


test_vehicle(Car())


# -------------------------- Read Only Properties ---------------------------
#
# If an object should expose an attribute that can be read but shouldn't be overwritten directly,
# use @property inside the protocol definition:


class Identifiable(Protocol):
    @property
    def id(self) -> str: ...


class User:
    def __init__(self, user_id: str) -> None:
        self._id: str = user_id

    @property
    def id(self) -> str:
        return self._id


def log_id(item: Identifiable) -> None:
    print(item.id)


# --------------------- Combining Protocols ---------------------------


class Readable(Protocol):
    def read(self) -> str: ...


class Writable(Protocol):
    def write(self, data: str) -> None: ...


# Combines both into a single requirement:
class ReadWriter(Protocol):
    def read(self) -> bytes: ...
    def write(self, data: bytes) -> int: ...


# ---------------------- Protocol Inheritance with extra methods ---------------------------
#
# A class can satisfy a protocol while having extra methods or parameters
# as long as required parameters match


class Logger(Protocol):
    def log(self, message: str) -> None: ...


class AdvancedLogger:
    def log(self, message: str) -> None:
        print(f"AdvancedLogger: {message}")

    def clear_log(self) -> None:
        pass


def run_task(logger: Logger) -> None:
    logger.log("Task started")


run_task(AdvancedLogger())
