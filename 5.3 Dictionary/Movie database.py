

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {'name': name, 'director': director, 'year': year, 'runtime': runtime}
    database.append(movie)
    return database






database = []
add_movie(database, "Gone", "Victor Pything", 2017, 116)
add_movie(database, "Python", "Renny Pytholin", 2001, 94)
print(database)