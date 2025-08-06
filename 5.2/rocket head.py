
size = 3

def head():
    for i in range(size):
        for j in range(size - i):
            print(' ', end='')
        for k in range(i+1):
            print('/', end='')
        for l in range(i+1):
            print('\\', end='')
        print()

                
head()