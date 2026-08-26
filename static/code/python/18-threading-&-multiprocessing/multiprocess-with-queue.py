import time
from multiprocessing import Process, process


def heavy_task() -> None:
    count = 0
    print(f"Count Started for {process.current_process().name}")

    for i in range(10**9):
        count += i
    print(f"Count Finished for {process.current_process().name}")


if __name__ == "__main__":
    p1: Process = Process(target=heavy_task, name="p1")
    p2: Process = Process(target=heavy_task, name="p2")

    start = time.perf_counter()

    for p in [p1, p2]:
        p.start()

    for p in [p1, p2]:
        p.join()

    print(f"Time Taken: {time.perf_counter() - start}")
