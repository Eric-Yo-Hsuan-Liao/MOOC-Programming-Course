

num_items = int(input('How many items: '))
items = []

for i in range(num_items):
    answer = int(input(f"Item {i+1}: "))
    items.append(answer)
print(items)