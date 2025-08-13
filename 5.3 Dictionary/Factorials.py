

def factorials(n: int):
    new_dict = {}
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        new_dict[i] = fact
    return new_dict


k = factorials(5)
print(k[1])
print(k[3])
print(k[5])
