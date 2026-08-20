"""
Watchdog is a python library to monitor filesystem events. like files/dirs are created, modified, or deleted.

THIS IS NOT IN STDLIB, INSTALL WITH PIP/UV
"""

from typing import override

from watchdog.events import (
    DirCreatedEvent,
    DirDeletedEvent,
    DirModifiedEvent,
    DirMovedEvent,
    FileCreatedEvent,
    FileDeletedEvent,
    FileModifiedEvent,
    FileMovedEvent,
    FileSystemEventHandler,
)
from watchdog.observers import Observer


class Handler(FileSystemEventHandler):
    @override
    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        print("Created:", event.src_path, event.dest_path, event.event_type)

    @override
    def on_deleted(self, event: DirDeletedEvent | FileDeletedEvent) -> None:
        return super().on_deleted(event)

    @override
    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        return super().on_modified(event)

    @override
    def on_moved(self, event: DirMovedEvent | FileMovedEvent) -> None:
        return super().on_moved(event)


observer = Observer()

observer.schedule(  # pyright: ignore[reportUnusedCallResult]
    Handler(),
    ".",
    recursive=True,
)

observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()
