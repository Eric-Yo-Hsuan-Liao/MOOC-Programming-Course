

def longest_series_of_neighbors(my_list: list):
    new_list = []
    max_list = []
    for i in range(len(my_list)):
        current = my_list[i]
        previous = my_list[i-1]
        if abs(current - previous) == 1:
            new_list.append(current)
        else:
            if len(new_list) > len(max_list):
                max_list = new_list
            new_list = [my_list[i]]
        if len(new_list) > len(max_list):
            max_list = new_list
    return max_list

my_list = [1,4,2,0,7,2]
print(longest_series_of_neighbors(my_list))