
# Original
# def transpose(matrix: list):
#     new_matrix = [[], [], []]
#     counter = 0
#     counter2 = 0
#     counter3 = 0
#     counter4 = 1
#     counter5 = 0
#     counter6 = 2
#     for row in matrix:
#         value1 = matrix[counter][counter2]
#         new_matrix[0].append(value1)
#         counter += 1
#     for row in matrix:
#         value2 = matrix[counter3][counter4]
#         new_matrix[1].append(value2)
#         counter3 += 1
#     for row in matrix:
#         value3 = matrix[counter5][counter6]
#         new_matrix[2].append(value3)
#         counter5 += 1

def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j > i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose(matrix)
print(matrix)