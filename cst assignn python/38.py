def get_positive_integer():
    try:
        user_input = input("Please enter a positive integer: ")

        number = int(user_input)
        assert number > 0, "The number must be positive!"

        print(f"Thank you! You entered a valid positive integer: {number}")

    except ValueError:
        print("Error: Please enter a valid integer.")
    except AssertionError as e:
        print(f"Error: {e}")
get_positive_integer()
