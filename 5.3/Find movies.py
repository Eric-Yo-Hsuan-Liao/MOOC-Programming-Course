

def find_movies(database: list, search_term: str):
    new = []
    for i in database:
        name = i['name']
        name = name.lower()
        name = name.replace(' ','')
        if search_term.lower() in name:
            new.append(i)
    return new


database = [{'name': 'Gone with Python', 'director': 'Victor Pything', 'year': 2017, 'runtime': 116}, 
            {'name': 'Python is the GOAT', 'director': 'Renny Pytholin', 'year': 2001, 'runtime': 94},
            {'name': 'Herro', 'director': 'Dummy', 'year': 2000, 'runtime': 69}]
my_movies = find_movies(database, 'python')
print(my_movies)