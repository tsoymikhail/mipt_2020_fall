import functools
import time


def timer(func):
    """Print runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        print("Run method: {:s}".format(func.__name__))
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("Finished {:s} in {:f} secs".format(func.__name__, run_time))
        return value
    return wrapper_timer