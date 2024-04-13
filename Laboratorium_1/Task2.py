import time
from datetime import datetime
from functools import wraps

def log_to_file(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"{current_time} - Executed {func.__name__} in {duration:.6f} seconds\n"
            with open(filename, "a") as f:
                f.write(log_message)
            return result
        return wrapper
    return decorator

@log_to_file("function_logs.log")
def test_function(x):
    return x * x

@log_to_file("function_logs.log")
def another_function(x, y):
    time.sleep(2) 
    return x + y

test_function(4)
another_function(5, 3)
