import inspect

def log_params(func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        params = sig.parameters
        
        param_types = {}
        
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        for name, value in bound_args.arguments.items():
            param_types[name] = type(value).__name__
        
        print(f"Parameters for function '{func.__name__}': {param_types}")
        
        return func(*args, **kwargs)
    
    return wrapper

@log_params
def example_function(a, b, c='default'):
    return str(a) + str(b) + c

example_function(1, 2, c='test')
