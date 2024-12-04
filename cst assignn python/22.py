#22. Program that takes a list of numbers and returns the biggest number.

def find_largest(numbers):
    return max(numbers)
numbers = list(map(int, input("Enter a list of numbers seperated by spaces :").split()))
print(f"The largest number in the given list is : {find_largest(numbers)}")