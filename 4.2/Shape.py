# Exercise

def shape(width, character, height, filler):
    tracker = 1
    while tracker < width + 1:
        print(character * tracker)
        tracker += 1
    for i in range(height):
        print(filler * (tracker - 1))


shape(5, "X", 3, "*")