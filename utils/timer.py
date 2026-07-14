"""
Performance Timer Utilities
"""

import time
from functools import wraps


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        if self.start_time is None:
            raise RuntimeError("Timer has not been started.")

        elapsed = time.perf_counter() - self.start_time
        self.start_time = None
        return elapsed


class TimerContext:
    def __init__(self, name="Execution"):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"{self.name} completed in {elapsed:.4f} seconds")


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} executed in {elapsed:.4f} seconds")
        return result
    return wrapper