

def search_by_name(filename: str, word: str):
    with open(filename) as new_file:
        recipes = []
        found = []
        for i in new_file:
            parts = i.strip()
            parts = parts.lower()
            recipes.append(parts)
        recipes.append('')
        print(recipes)
        for i in recipes:
            if word.lower() in i:
                found.append(i)
    return found


found_recipes = search_by_name('recipes1.txt', 'cake')
for recipe in found_recipes:
    print(recipe)