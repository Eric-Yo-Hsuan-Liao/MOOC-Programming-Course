

import difflib

with open('wordlist.txt') as new_file:
    words = []
    for i in new_file:
        i = i.strip()
        words.append(i)

    user = input('Write text: ')
    user = user.lower()
    parts = user.split()
    answer = ''
    for i in parts:
        if i in words:
            answer += i + ' '
        elif i not in words:
            wrong_word = i
            wrong = f"*{wrong_word}* "
            answer += wrong
    print(answer)
    print('suggestions:')
    for i in parts:
        if i not in words:
            close_words = difflib.get_close_matches(i, words)
            print(f"{i}: {', '.join(str(item) for item in close_words)}")

