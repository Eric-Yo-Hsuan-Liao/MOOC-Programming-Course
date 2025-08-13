

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

layers = int(input('Layers: '))
width = (layers * 2) - 1

for i in range(width):
    line = ''
    for j in range(width):
        for k in range(layers):
            if i == k or k == j or i == width - 1 - k or j == width - 1 - k:
                line += alphabet[layers - 1 - k]
                break

    print(line)

