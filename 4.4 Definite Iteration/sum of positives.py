

def sum_of_positives(int_list: list):
    total = 0
    for i in int_list:
        if i > 0:
            total = i + total
    return total

my_list = [1,-2,3,-4,5]
result = sum_of_positives(my_list)
print("The result is", result)

