

def oldest_person(people: list):
    oldest = people[0][1]
    name = ''
    for tuple in people:
        years = tuple[1]
        if years < oldest:
            oldest = years
            name = tuple[0]
    return name


p1 = ('Adam', 1977)
p2 = ('Ellen', 1985)
p3 = ('Mary', 1953)
p4 = ('Ernest', 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))