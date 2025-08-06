

def first_word(sentence):
    words = sentence.split()
    return words[0]

def second_word(sentence):
    words = sentence.split()
    return words[1]

def last_word(sentence):
    words = sentence.split()
    return words[-1]

sentence = "It was a dark and stormy day"

print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence))


