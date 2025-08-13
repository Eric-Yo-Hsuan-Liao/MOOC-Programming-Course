

def even_numbers(int_list: list):
    new_list = []
    for i in int_list:
        if i % 2 == 0: # even
            new_list.append(i)
    return new_list

my_list = [1,2,3,4,5]
newest_list = even_numbers(my_list)
print('original', my_list)
print('new', newest_list)

