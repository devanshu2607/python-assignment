#14. Program to count the frequency of words.
sentence = input("Enter a sentence:")

words = sentence.split()

word_count = {}
for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word,0)+1
print("Word frequencies :")
for word, count in word_count.items():
    print(f"{word}: {count}")