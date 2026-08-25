"""
 Challenge: Real-Time System Resource Monitor

Goal:
- Monitor your system's CPU, RAM, and Disk usage
- Print updates every few seconds
- Warn user if CPU or RAM usage exceeds 80%
- Runs in terminal as a live dashboard

Teaches: psutil, formatting, real-time monitoring, conditional logic
Tools: psutil, time
"""

import os
import shutil
import subprocess
import sys
import time

import psutil


def clear():
    subprocess.run(["cls" if os.name == "nt" else "clear"], check=True)  # pyright: ignore[reportUnusedCallResult]


try:
    while True:
        clear()
        print("*" * shutil.get_terminal_size().columns)

        print(
            f"RAM:  {psutil.virtual_memory().used / (1024**3):.2f} GB used of {psutil.virtual_memory().total / (1024**3):.2f} GB"
        )
        print(
            f"Swap: {psutil.swap_memory().used / (1024**3):.2f} GB used of {psutil.swap_memory().total / (1024**3):.2f} GB"
        )
        print(
            f"Disk: {psutil.disk_usage('/').used / (1024**3):.2f} GB used of {psutil.disk_usage('/').total / (1024**3):.2f} GB"
        )
        print(f"CPU:  {psutil.cpu_percent(interval=0.1)}%")

        time.sleep(3)
except KeyboardInterrupt:
    clear()
    sys.exit(1)
