

dict = {}
command = True

user = int(input('command(1 search, 2 add, 3 quit): '))

while command == True:
    if user == 3:
        command = False
        print('quitting...')
        break
    if user == 2:
        name = str(input('name: '))
        number = str(input('number: '))
        dict[name] = number
        print('ok!')
    if user == 1:
        search = str(input('name: '))
        if search not in dict:
            print('no number')
        else:
            value = dict[search]
            print(value)
    user = int(input('command(1 search, 2 add, 3 quit): '))

print(dict)