

def most_common_character(word):
    word_list = list(word)
    most = 0
    for i in word_list:
        most_chars = word.count(i)
        if most_chars > most:
            most = most_chars
            most_characters = i
    return most_characters



first_string = 'abcdbde'
print(most_common_character(first_string))

second_string = 'exemplaryelementary'
print(most_common_character(second_string))