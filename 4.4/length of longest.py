

def length_of_longest(my_list: list):
    longest = 0
    for i in my_list:
        # string_len = len(i)
        if len(i) > longest:
            longest = len(i)
    return longest

my_list = ['first', 'second', 'fourth', 'eleventh']
result = length_of_longest(my_list)
print(result)
