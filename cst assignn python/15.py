#15.Program to replace all occurence of a substring with another substring.
def replace_substring(original_string , old_substring , new_substring):
    return original_string.replace(old_substring , new_substring)

text = input("Enter the original string: ")
old = input("Enter the substring to replace:")
new = input ("Enter the new substring:")

result = replace_substring(text,old,new)

print(f"The modified string is : {result}")