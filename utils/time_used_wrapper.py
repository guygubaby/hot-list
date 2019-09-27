from functools import wraps
import time


def time_used(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print('{} seconds used '.format(time.time() - start))
    return wrapper
