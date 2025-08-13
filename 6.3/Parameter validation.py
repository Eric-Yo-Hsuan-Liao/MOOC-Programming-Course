

def new_person(name: str, age: int):
    new = (name, age)
    parts = name.split(' ')
    name = name.replace(' ','')
    name_chars = 0
    for char in name:
        name_chars += 1
    if name == '':
        raise ValueError('Invalid name, empty string found')
    if len(parts) < 2:
        raise ValueError('Invalid name, needs to be two words')
    if name_chars > 40:
        raise ValueError('Invalid name, has to be shorter than 40 characters')
    if age < 0:
        raise ValueError('Invalid age, cannot be negative')
    if age > 150:
        raise ValueError('Invalid age, needs to be less than 150')
    return print(new)


new_person('Eric Lio',22)
