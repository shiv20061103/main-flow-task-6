def word_frequency(text):
    text = text.lower()
    import string
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    freq = {}
    
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq
user_input = input("Enter a string of text: ")
result = word_frequency(user_input)

print("\nWord Frequencies:")
for word, count in result.items():
    print(f"{word}: {count}")
