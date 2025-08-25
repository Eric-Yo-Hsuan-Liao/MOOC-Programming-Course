

import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
    people = json.loads(data)
    for person in people:
        print(f"{person['name']} {person['age']} years ({', '.join(person['hobbies'])})")



print_persons('Handling JSON.json')