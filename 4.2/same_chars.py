


def same_chars(word, index1, index2):
    if word[index1] == word[index2]:
        return True
    return False

print(same_chars('programmer', 6, 7))
print(same_chars('programmer', 0, 4))