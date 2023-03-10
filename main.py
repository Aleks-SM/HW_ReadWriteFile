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


def orders_ing(data, recipe, person):
    rec = data.get(recipe)
    for dict_ in rec:
        dict_['quantity'] = dict_.get('quantity') * person
    return rec


def get_shop_list_by_dishes(dishes, person_count):
    tmp = {}
    for recipe in dishes:
        list_ingridient = orders_ing(read_file(), recipe, person_count)
        for ingridient in list_ingridient:
            if ingridient.get('ingredient_name') in tmp:
                tmp[ingridient.get('ingredient_name')] = {
                'measure': ingridient.get('measure'),
                'quantity': int(ingridient.get('quantity')+int(ingridient.get('quantity')))
                }
            else:
              tmp[ingridient.get('ingredient_name')] = {
                'measure': ingridient.get('measure'),
                'quantity': ingridient.get('quantity')
                }
    return tmp


pprint(read_file(), sort_dicts=False)
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3), sort_dicts=False)
