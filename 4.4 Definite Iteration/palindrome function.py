

def palindromes(word):
    word_list = list(word)
    original = word_list.copy()
    reversed = []
    while len(word_list) != 0:
        letter = word_list.pop()
        reversed.append(letter)
    if original == reversed:
        return True
    else:
        return False

print(palindromes('civic'))
print(palindromes('python'))