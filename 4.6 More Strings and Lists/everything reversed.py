

def everything_reversed(string_list: list):
    reverse_list = []
    for i in string_list[::-1]:
        reversed = i[::-1]
        reverse_list.append(reversed)
    return reverse_list


my_list = ['Hi', 'there', 'example', 'one more']
new_list = everything_reversed(my_list)
print(new_list)