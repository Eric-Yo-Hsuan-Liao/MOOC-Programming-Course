

def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for i in my_matrix:
        for j in i:
            if element == j:
                count += 1
    return count

m = [[1,2,1], [0,3,4], [1,0,0]]
print(count_matching_elements(m,1))