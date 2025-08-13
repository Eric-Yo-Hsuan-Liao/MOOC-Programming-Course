

def store_personal_data(person: tuple):
    with open('people.csv', 'a') as file:
        name = person[0]
        age = person[1]
        height = person[2]
        file.write(f'{name};{age};{height}')
    


store_personal_data(('Paul Paulson', 37, 175.5))
