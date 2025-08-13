
from math import sqrt

def hypotenuse(leg1: float, leg2: float):
    leg1 = leg1 ** 2
    leg2 = leg2 ** 2
    c = sqrt(leg1 + leg2)
    return c

print(hypotenuse(3,4))

