#11. Program to count vowels in a string .
text = input("Enter a string:")

vowel = "aeiouAEIOU"

count = 0 
for char in text:
    if char in vowel:
        count+= 1

print(f"The number of vowels in given string is : {count} ")        