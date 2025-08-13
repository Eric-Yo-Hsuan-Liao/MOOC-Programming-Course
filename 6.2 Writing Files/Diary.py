
with open('diary.txt', 'a') as my_file:
    tracker = True
    while tracker:
        print('1 - add an entry, 2 - read entries, 0 - quit')
        user = int(input('Function: '))
        if user == 1:
            with open('diary.txt', 'a') as my_file:
                adding = input('Diary entry: ')
                my_file.write(f'{adding}\n')
                print('Diary saved')
                print()
        elif user == 2:
            with open('diary.txt') as my_file:
                print('Entries:')
                for line in my_file:
                    print(line)
                print()
        elif user == 0:
            print('Bye now!')
            tracker = False



