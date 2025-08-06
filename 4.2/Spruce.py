# Exercise

def spruce(tree):
    print('a spruce!')
    tracker = 1
    for i in range(tree):
        whitespace = tree - i - 1
        print(' ' * whitespace + '*' * tracker)
        tracker += 2
    print(' ' * (tree - 1) + '|')

spruce(3)
        