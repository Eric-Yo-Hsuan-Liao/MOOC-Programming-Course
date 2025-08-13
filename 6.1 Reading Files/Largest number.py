

def largest():
    with open('numbers.txt') as numbers:

        max = float('-inf')

        for i in numbers:
            num = int(i.strip())
            if num > max:
                max = num
    
    return print(max)

largest()