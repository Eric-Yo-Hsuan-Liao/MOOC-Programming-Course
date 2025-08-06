

def distinct_numbers(my_list: list):
    new_list = set()
    for i in my_list:
        if i not in new_list:
            new_list.add(i)
    return new_list

my_list = [3,2,2,1,3,3,1]
print(distinct_numbers(my_list))