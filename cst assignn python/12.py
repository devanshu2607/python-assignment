#12. Program to remove all whitespace from a string.
def remove_whitespace(text):
    return text.replace(" ", "")

user_input = input("Enter a string :")

result = remove_whitespace(user_input)

print(f"String without whitespace : {result}")
