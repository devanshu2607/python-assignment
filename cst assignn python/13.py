#13. Program to check if two strings are anagrams.
string1 = input("Enter the first string : ").lower()
string2 = input ("Enter the second string : ").lower()

if sorted(string1.replace(" ", "")) == sorted(string2.replace(" ", "")):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")    