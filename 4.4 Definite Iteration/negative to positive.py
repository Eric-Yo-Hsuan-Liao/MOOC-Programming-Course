

prompt = int(input('Please type in a positive integer: '))

#for i in range(prompt, 0, -1):
#    print(-i)
#for i in range(prompt):
#    print(i + 1)

for i in range(-prompt, prompt + 1):
    if i != 0:
        print(i)
