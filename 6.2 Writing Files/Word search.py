


def find_words(search_term: str):
    words = []
    dot = '.'
    with open('words.txt') as file:
        if search_term[0] == '*':
            for word in file:
                word = word.strip()
                if word.endswith(search_term[1:]):
                    words.append(word)
        elif search_term[-1] == '*':
            for word in file:
                word = word.strip()
                if word.startswith(search_term[:-1]):
                    words.append(word)
        elif dot in search_term:
            if search_term.endswith(dot):
                length = len(search_term)
                letter = search_term[:-1]
                for word in file:
                    word = word.strip()
                    if word.startswith(letter) and len(word) == length:
                        words.append(word)
            else:
                for word in file:
                    word = word.strip()
                    if len(word) != len(search_term):
                        continue
                    checked = True
                    for i in range(len(search_term)):
                        if search_term[i] == '.':
                            continue
                        else:
                            if search_term[i] != word[i]:
                                checked = False
                                break
                    if checked:
                        words.append(word)
    return words
        
print(find_words("p.ng"))
