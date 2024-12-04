import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_function_call(func):
    """Decorator to log function calls and their parameters."""
    def wrapper(*args, **kwargs):
        
        logging.info(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        
        result = func(*args, **kwargs)
        
        logging.info(f"Function '{func.__name__}' returned: {result}")
        
        return result
    return wrapper

@log_function_call
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

@log_function_call
def multiply(a, b, factor=1):
    """Multiplies two numbers with an optional factor."""
    return a * b * factor

@log_function_call
def greet(name, greeting="Hello"):
    """Generates a greeting message."""
    return f"{greeting}, {name}!"
def main():
    add(3, 5)
    multiply(4, 6, factor=2)
    greet("Alice", greeting="Hi")
if __name__ == "__main__":
    main()
