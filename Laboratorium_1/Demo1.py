import time
import functools
import logging

logging.basicConfig(level=logging.INFO)

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        logging.info(f"Function {func.__name__} executed in {end-start} seconds")
        return result
    return wrapper

@timer
def calculation(n):
    inter=0
    for i in range(n):
        inter+=i

calculation(int(1e6))