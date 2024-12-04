class NotPositiveNumberError(Exception):
    """Custom exception for when a number is not positive."""
    pass

def check_positive_number(number):
    """Raises an exception if the number is not positive."""
    if number <= 0:
        raise NotPositiveNumberError("The number must be positive!")
    print(f"The number {number} is positive.")

def main():
    try:
        
        user_input = float(input("Enter a positive number: "))
        
        check_positive_number(user_input)

    except NotPositiveNumberError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
