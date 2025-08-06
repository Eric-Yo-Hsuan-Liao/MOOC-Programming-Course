

def formatted(floats_list: list):
    final_list = []
    for i in floats_list:
        rounded = f"{i:.2f}"
        final_list.append(rounded)
    return final_list

my_list = [1.234, 0.3333, 0.11111, 3.446]
new_list = formatted(my_list)
print(new_list)