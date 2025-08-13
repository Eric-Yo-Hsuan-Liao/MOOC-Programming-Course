

def anagrams(string1, string2):
    word1 = sorted(string1)
    word2 = sorted(string2)
    if word1 == word2:
        return True
    return False

print(anagrams('tame','meta'))
print(anagrams('python','java'))