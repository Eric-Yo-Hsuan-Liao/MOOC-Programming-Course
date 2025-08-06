

def all_the_longest(my_list: list):
    longest_len = len(my_list[0])
    result_list = [] 
    for word in my_list:
        if len(word) > longest_len:
            longest_len = len(word)
            result_list = [word]
        elif len(word) == longest_len:
            result_list.append(word)
# original thought
#    if len(result_list[0]) < len(result_list[1]):
#        result_list = result_list[1:]
    return result_list

my_list = ['adele', 'mark', 'dorothy', 'tim', 'richard', 'hedy']
result = all_the_longest(my_list)
print(result)

