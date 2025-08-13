

def matrix_sum():
    with open('matrix.txt') as new_file:
        total = 0
        for line in new_file:
            line = line.replace('\n', '')
            line = line.split(',')
            for value in line:
                value = int(value)
                total += value
    return print(total)


def matrix_max():
    with open('matrix.txt') as new_file:
        greatest = float('-inf')
        for line in new_file:
            line = line.replace('\n', '')
            line = line.split(',')
            for value in line:
                value = float(value)
                if value > greatest:
                    greatest = value
    return print(greatest)

def row_sums():
    with open('matrix.txt') as new_file:
        result = []
        for line in new_file:
            line = line.replace('\n', '')
            numbers = line.split(',')
            row_total = 0
            for i in numbers:
                row_total += int(i)
            result.append(row_total)
            #int_row = [int(x) for x in line]
            #row_sum = sum(int_row)
            #result.append(row_sum)
    return print(result)

            
row_sums()
matrix_sum()
matrix_max()