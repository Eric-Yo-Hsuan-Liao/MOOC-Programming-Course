def row_correct(sudoku: list, row_no: int):
    result_row = []
    for i in sudoku[row_no]:
        if i in result_row and i != 0:
            return False
        else:
            result_row.append(i)
    return True

def column_correct(sudoku: list, column_no: int):
    result_col = []
    for row in sudoku:
        value = row[column_no]
        if value in result_col and value != 0:
            return False
        else:
            result_col.append(value)
    return True

def block_correct(sudoku: list, row_no: int, col_no: int):
    result_block = []
    for i in range(3):
        for j in range(3):
            value = sudoku[row_no + i][col_no + j]
            if value in result_block and value != 0:
                return False
            else:
                result_block.append(value)
    return True

def sudoku_grid_correct(sudoku: list):
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False
    for col_no in range(9):
        if not column_correct(sudoku, col_no):
            return False
    for row in range(0,9,3):
        for col in range(0,9,3):
            if not block_correct:
                return False
    return True

sudoku1 = [
    [9,0,0,0,8,0,3,0,0],
    [2,0,0,2,5,0,7,0,0],
    [0,2,0,3,0,0,0,0,4],
    [2,9,4,0,0,0,0,0,0],
    [0,0,0,7,3,0,5,6,0],
    [7,0,5,0,6,0,4,0,0],
    [0,0,7,8,0,3,9,0,0],
    [0,0,1,0,0,0,0,0,3],
    [3,0,0,0,0,0,0,0,2]
]

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
    [2,6,7,8,3,9,5,0,4],
    [9,0,3,5,1,0,6,0,0],
    [0,5,1,6,0,0,8,3,9],
    [5,1,9,0,4,6,3,2,8],
    [8,0,2,1,0,5,7,0,6],
    [6,7,4,3,2,0,0,0,5],
    [0,0,0,4,5,7,2,6,3],
    [3,2,0,0,8,0,0,5,7],
    [7,4,5,0,0,3,9,0,1]
]

print(sudoku_grid_correct(sudoku2))