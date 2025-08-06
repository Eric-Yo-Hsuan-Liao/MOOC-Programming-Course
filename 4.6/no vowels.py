

def no_vowels(word):
    vowels = ['a','e','i','o','u']
    for i in word:
        if i in vowels:
            word = word.replace(i,'')
    return word



my_string = 'this is an example'
print(no_vowels(my_string))