

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

sudoku = [
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
print(block_correct(sudoku, 0, 0))
print(block_correct(sudoku, 1, 2))