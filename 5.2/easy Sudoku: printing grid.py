

def print_sudoku(sudoku: list):
    for i in range(9):
        if i == 3 or i == 6:
            print()
        for j in range(9):
            if j == 3 or j == 6:
                print(' ', end='')
                print('_', end = ' ')
            else:
                print('_', end = ' ')
        print()

sudoku = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
print_sudoku(sudoku)