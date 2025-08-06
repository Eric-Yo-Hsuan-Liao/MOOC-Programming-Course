

def no_shouting(string_list: list):
    non_cap = []
    for i in string_list:
        if i.isupper() == False:
            non_cap.append(i)
    return non_cap
        
my_list = ['ABC','def','UPPER','ANOTHERUPPER','lower','another lower','Capitalized']
pruned_list = no_shouting(my_list)
print(pruned_list)
