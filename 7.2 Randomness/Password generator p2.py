
from string import ascii_lowercase
import random

def generate_strong_password(pass_len: int, nums: bool, special: bool):
    chars = ascii_lowercase
    password = ''
    for i in range(pass_len):
        if nums:
            answer = random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
        elif special:
            answer = random.choice('abcdefghijklmnopqrstuvwxyz!?=+-()#')
        else:
            answer = random.choice(chars)
        password += answer
    return password



for i in range(10):
    print(generate_strong_password(8, True, True))