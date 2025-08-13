

import string

def separate_characters(my_string: str):
    part1 = ''
    part2 = ''
    part3 = ''
    for char in my_string:
        if char in string.ascii_letters:
            part1 += char
    for char in my_string:
        if char in string.punctuation:
            part2 += char
    for char in my_string:
        if char not in string.ascii_letters and char not in string.punctuation:
            part3 += char
    parts = (part1, part2, part3)
    return parts


parts = separate_characters('Hello!!! Höŵ are you????')
print(parts[0])
print(parts[1])
print(parts[2])