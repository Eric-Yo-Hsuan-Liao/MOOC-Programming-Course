

with open('course1.txt') as course:
    information = []
    for line in course:
        parts = line.split(':')
        parts[1] = parts[1].strip()
        print(parts)
        information.append(parts[1])
    print(information)

    