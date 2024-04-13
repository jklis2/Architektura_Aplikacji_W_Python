from functools import wraps

def list_count_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        for arg in args:
            if isinstance(arg, list):
                print(f"List found with {len(arg)} elements.")

        for arg in kwargs.values():
            if isinstance(arg, list):
                print(f"List found with {len(arg)} elements.")
        return func(*args, **kwargs)
    return wrapper

@list_count_decorator
def sample_function(a, b, c):
    print("Executing sample_function")

sample_function(1, [1, 2, 3], 'hello')
sample_function(a=1, b=[4, 5], c=[6, 7, 8, 9])
