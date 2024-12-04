def to_uppercase(string: str)-> str:
    return string.upper()

def reverse_string(string: str)-> str:
    return string[::-1]

def count_vowels(string: str)-> str:
    vowels = "aeiouAEIOU"
    return sum( 1 for char in string if char in vowels)

def remove_whitespace(string: str)-> str:
    return ''.join(string.split())

def word_count(string: str)-> int:
    return len(string.split())