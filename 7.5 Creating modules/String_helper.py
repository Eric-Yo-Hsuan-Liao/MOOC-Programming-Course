
import math
import string

def change_case(orig_string: str):
    answer = ''
    for char in orig_string:
        if char.isupper():
            new_char = char.lower()
            answer += new_char
        elif char.islower:
            new_char = char.upper()
            answer += new_char
    return answer

def split_in_half(orig_string: str):
    length = len(orig_string)
    if length % 2 != 0:
        halved = math.floor(len(orig_string) / 2)
    elif length % 2 == 0:
        halved = len(orig_string) / 2
    first_half = orig_string[:halved]
    second_half = orig_string[halved:]
    answer = (first_half, second_half)
    return answer

def remove_special_characters(orig_string: str):
    answer = ''
    for char in orig_string:
        if char in string.ascii_letters or char in string.digits or char in string.whitespace:
            answer += char
    return answer

if __name__ == "__main__":
    my_string = 'Well hello there!'
    print(change_case(my_string))
    p1, p2 = split_in_half(my_string)
    print(p1)
    print(p2)
    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)