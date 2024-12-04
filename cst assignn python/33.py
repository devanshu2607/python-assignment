def apply_function_to_list(func, lst):
    """A higher-order function that applies a given function to each element of the list."""
    return [func(x) for x in lst]

def add_five(x):
    """Adds 5 to the given number."""
    return x + 5


def main():
    numbers = [1, 2, 3, 4, 5]
    
    print("Original list:", numbers)
    
    
    modified_list = apply_function_to_list(add_five, numbers)
    
    print("Modified list after applying add_five:", modified_list)


if __name__ == "__main__":
    main()
