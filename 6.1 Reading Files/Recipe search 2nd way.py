

def search_by_name(filename: str, word: str):
    with open(filename) as file:
        recipe = []
        for line in file:
            line = line.strip()
            recipe.append(line)
        recipe.append("")
        print(recipe)
        all_recipe = []
        new_line = []
        for line in recipe:
            if line != "":
                new_line.append(line)
            else:
                if new_line:
                    name = new_line[0]
                    if word.lower() in name.lower():
                        all_recipe.append(name)
                    new_line = []
    return all_recipe


def search_by_time(filename: str, prep_time: int):
    with open(filename) as file:
        recipe = []
        for line in file:
            line = line.strip()
            recipe.append(line)
        recipe.append("")
        all_recipe = []
        new_line = []
        for line in recipe:
            if line != "":
                new_line.append(line)
            else:
                if new_line:
                    name = new_line[0]
                    preparation_time = int(new_line[1])
                    # for part 3 if recipe[2:] which are ingredients
                    if preparation_time <= prep_time:
                        all_recipe.append(f'{name}, preparation time {preparation_time} min')
                    new_line = []
    return all_recipe


def search_by_ingredient(filename: str, ingredient: str):
    with open(filename) as file:
        recipe = []
        for line in file:
            line = line.strip()
            recipe.append(line)
        recipe.append("")
        all_recipe = []
        new_line = []
        for line in recipe:
            if line != "":
                new_line.append(line)
            else:
                if new_line:
                    name = new_line[0]
                    preparation_time = int(new_line[1])
                    ingredients = new_line[2:]
                    # for part 3 if recipe[2:] which are ingredients
                    if ingredient in ingredients: # if ingredient is in list of ingredients
                        all_recipe.append(f'{name}, preparation time {preparation_time} min')
                    new_line = []
    return all_recipe



found_recipes = search_by_ingredient('recipes1.txt', 'eggs')
for recipe in found_recipes:
    print(recipe)