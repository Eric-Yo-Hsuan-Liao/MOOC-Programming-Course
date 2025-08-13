
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

def copy_and_add(sudoku: list, row_no: int, col_no: int, number: int):
    new_copy = [row[:] for row in sudoku]
    new_copy[row_no][col_no] = number
    return new_copy

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

grid_copy = copy_and_add(sudoku, 0,0,2)
print('Original:')
print_sudoku(sudoku)
print()
print('Copy:')
print_sudoku(grid_copy)