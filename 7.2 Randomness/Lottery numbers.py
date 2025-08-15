

from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    nums = list(range(lower, upper + 1))
    draw = sample(nums, amount)
    draw.sort()
    return draw

for number in lottery_numbers(7, 1, 40):
    print(number)