##66.	Write a function that converts a number to its binary string representation.

def to_binary(n):
    return bin(n)[2:]

print(to_binary(13))