

import random


def words(n: int, beginning: str):
    valid_words = []
    final_words = []
    with open('words.txt', 'r') as file:
        try:
            for word in file:
                word = word.strip()
                if word.startswith(beginning):
                    valid_words.append(word)
            for i in range(n):
                final_word = random.choice(valid_words)
                final_words.append(final_word)
        except:
            raise ValueError(f'There are no words that start with {beginning}')
    return final_words


word_list = words(3, "ca")
for word in word_list:
    print(word)