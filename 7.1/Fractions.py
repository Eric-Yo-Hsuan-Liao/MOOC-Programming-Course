

import fractions

def fractionate(amount: int):
    all = []
    for i in range(amount):
        answer = fractions.Fraction(f'1/{amount}')
        all.append(answer)
    return all

for p in fractionate(3):
    print(p)

print()

print(fractionate(5))