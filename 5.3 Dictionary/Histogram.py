

def histogram(word: str):
    dict = {}
    for letter in word:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    
    for key, value in dict.items():
        print(key, value * '*')


histogram('statistically')