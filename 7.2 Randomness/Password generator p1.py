
from string import ascii_lowercase
import random


def generate_password(pass_len: int):
    chars = ascii_lowercase
    password = ''
    for i in range(pass_len):
        char = random.choice(chars)
        password += char
    return password



for i in range(10):
    print(generate_password(8))

