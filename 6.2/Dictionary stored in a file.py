
try:
    open('dictionary.txt', 'r')
except FileNotFoundError:
    open('dictionary.txt', 'w')

check = True
while check:
    user = int(input('1 - Add word, 2 - Search, 3 - Quit\nFunction: '))
    if user == 3:
        check = False
        print('Bye!')
        break
    elif user == 1:
        with open('dictionary.txt', 'a') as file:
            word1 = input('The word in English: ')
            word2 = input('The word in Spanish: ')
            file.write(f"{word1}:{word2}")
            file.write('\n')
            print('Dictionary entry added')
    elif user == 2:
        with open('dictionary.txt', 'r') as file:
            question = input('Search term: ')
            for line in file:
                line = line.strip()
                parts = line.split(':')
                for word in parts:
                    if question in word:
                        print(f"{parts[0]} - {parts[1]}")
                
