
import random

die_A = '333336'
die_B = '222555'
die_C = '144444'

def roll(die: str):
    if die == "A":
        sides = random.choice(die_A)
    elif die == "B":
        sides = random.choice(die_B)
    elif die == "C":
        sides = random.choice(die_C)
    return int(sides)


for i in range(20):
    print(roll("A"), " ", end = "")
print()
for i in range(20):
    print(roll("B"), " ", end = "")
print()
for i in range(20):
    print(roll("C"), " ", end = "")
print()

def play(die1: str, die2: str, times: int):
    wins = 0
    loss = 0
    draw = 0
    for i in range(times):
        result1 = roll(die1)
        result2 = roll(die2)
        if result1 > result2:
            wins += 1
        elif result1 < result2:
            loss += 1
        elif result1 == result2:
            draw += 1
    final = (wins, loss, draw)
    return final


result = play('A', 'C', 1000)
print(result)
result = play('B', 'B', 1000)
print(result)