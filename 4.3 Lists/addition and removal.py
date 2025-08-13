
user_list = []
counter = 1

print(f"The list is now {user_list}")
question = input("a(d)d, (r)emove or e(x)it: ")

while question != 'x':
    if question == 'd':
        user_list.append(counter)
        counter += 1
        print(f"The list is now {user_list}")
        question = input("a(d)d, (r)emove or e(x)it: ")
    elif question == 'r':
        user_list.pop()
        counter -= 1
        print(f"The list is now {user_list}")
        question = input("a(d)d, (r)emove or e(x)it: ")
print('Bye!')

