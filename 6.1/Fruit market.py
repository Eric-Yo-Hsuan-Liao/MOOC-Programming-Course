

with open('fruits.csv') as new_file:

    def read_fruits():
        new_dict = {}
        for line in new_file:
            line = line.replace('\n', '')
            parts = line.split(';')
            name = parts[0]
            value = float(parts[1])
            new_dict[name] = value
        return print(new_dict)

    read_fruits()