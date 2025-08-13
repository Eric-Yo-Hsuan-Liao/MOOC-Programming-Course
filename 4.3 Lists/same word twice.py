
list_of_words = []
word_counter = 0

word = input('Word: ')
while word not in list_of_words:
    list_of_words.append(word)
    word_counter += 1
    word = input('Word: ')
print(f"You typed in {word_counter} different words")


