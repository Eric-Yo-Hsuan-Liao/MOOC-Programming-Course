

def older_people(people: list, year: int):
    new = []
    for tuple in people:
        years = tuple[1]
        if years < year:
            name = tuple[0]
            new.append(name)
    return new


p1 = ('Adam', 1977)
p2 = ('Ellen', 1985)
p3 = ('Mary', 1953)
p4 = ('Ernest', 1997)
people = [p1, p2, p3, p4]

older = older_people(people, 1979)
print(older)