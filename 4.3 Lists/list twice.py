

original_list = []

value = int(input('New item: '))
while value != 0:
    original_list.append(value)
    print(f"The list now: {original_list}")
    ordered = sorted(original_list)
    print(f"The list in order: {ordered}")
    value = int(input('New item: '))
print('Bye!')


