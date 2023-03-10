def read_file():
    with open('recipes.txt') as file:
        data = {}
        for line in file:
            data[line.strip()] = []
            count = int(file.readline().strip())
            for i in range(count):
                ingredient_name, quantity, measure = file.readline().strip(
                ).split(' | ')
                data[line.strip()].append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            file.readline()
    file.close()
    return data
