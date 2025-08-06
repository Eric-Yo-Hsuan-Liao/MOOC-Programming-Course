

def create_tuple(x: int, y: int, z: int):
    first = min(x,y,z)
    second = max(x,y,z)
    total = x + y + z
    new = (first, second, total)
    return new


if __name__ == '__main__':
    print(create_tuple(5, 3, -1))