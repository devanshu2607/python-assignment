def is_even(n):
    return n % 2 == 0

# Unit tests
assert is_even(4) == True, "Test failed: 4 is even"
assert is_even(7) == False, "Test failed: 7 is odd"
assert is_even(0) == True, "Test failed: 0 is even"
assert is_even(-2) == True, "Test failed: -2 is even"
assert is_even(-3) == False, "Test failed: -3 is odd"

print("All tests passed!")

