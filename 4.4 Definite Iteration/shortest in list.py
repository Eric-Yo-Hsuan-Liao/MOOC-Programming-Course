

def shortest(my_list: list):
    shortest_len = len(my_list[0])
    shortest_word = my_list[0]
    for word in my_list:
        if len(word) < shortest_len:
            shortest_len = len(word)
            shortest_word = word
    return shortest_word

my_list = ['tim', 'adele', 'mark', 'dorothy']
result = shortest(my_list)
print(result)