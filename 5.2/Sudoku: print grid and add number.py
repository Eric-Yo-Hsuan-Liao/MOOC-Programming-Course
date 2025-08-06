

def print_sudoku(sudoku: list):
    counter = 0
    block_counter = 0
    for row in sudoku:
        for value in row:
            if value != 0:
                print(value, end=' ')
                counter += 1
                block_counter += 1
            if value == 0:
                if counter == 3 or counter == 6:
                    print(' ', end=' ')
                print('_', end=' ')
                counter += 1
                block_counter += 1

            if counter == 9:
                print()
                counter = 0

            if block_counter == 27 or block_counter == 54:
                print()


def add_number(sudoku: list, row_no: int, col_no: int, number: int):
    sudoku[row_no][col_no] = number


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
add_number(sudoku, 0,0,2)
add_number(sudoku, 1,2,7)
add_number(sudoku, 5,7,3)
print()
print('Three numbers added:')
print()
print_sudoku(sudoku)