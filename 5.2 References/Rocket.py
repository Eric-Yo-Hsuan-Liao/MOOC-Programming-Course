
size = 5

#def main():
def head():
    for i in range(size):
        for j in range(size - i):
            print(' ', end='')
        for k in range(i+1):
            print('/', end='')
        for l in range(i+1):
            print('\\', end='')
        print()

def belt():
    for i in range(1):
        print('+' + ('=' * size * 2) + '+')

def upper():
    counter = size - 1
    for i in range(size):
        print('|' + ('.' * counter) + ('/\\' * (i + 1)) + ('.' * counter) + '|')
        counter -= 1

def lower():
    counter2 = size
    counter3 = 0
    for i in range(size):
        print('|' + ('.' * counter3) + ('\\/' * counter2) + ('.' * counter3) + '|')
        counter2 -= 1
        counter3 += 1

#if __name__ == "_main_":
#    main()
def main():
    head()
    belt()
    upper()
    lower()
    belt()
    head()
main()