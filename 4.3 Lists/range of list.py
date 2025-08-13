

def range_of_list(my_list: list):
    range = max(my_list) - min(my_list)
    return print(f'The range of the list is {range}')

my_list = [1,2,3,4,5]
range_of_list(my_list)