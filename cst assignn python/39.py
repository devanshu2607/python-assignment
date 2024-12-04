
def safe_divide():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

       
        result = numerator / denominator

        
        print(f"The result of {numerator} / {denominator} is: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"Unexpected error: {e}")

safe_divide()
