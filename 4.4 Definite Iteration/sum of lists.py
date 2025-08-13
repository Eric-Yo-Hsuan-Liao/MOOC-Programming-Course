

def list_sum(list1: list, list2: list):
    list_sum = []
    length = len(list1) - 1
    i = 0
    while i <= length:
        new_value = list1[i] + list2[i]
        list_sum.append(new_value)
        i += 1
    return list_sum

a = [1,2,3]
b = [7,8,9]
print(list_sum(a, b))