

def invert(dictionary: dict):
   new_dict = {}
   for key, value in dictionary.items():
       new_dict[value] = key
   return new_dict


s = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth'}
inverted = invert(s)
print(inverted)
