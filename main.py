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


def input_orders():
    data = read_file()
    order = []
    tmp = {}
    for i, j in enumerate(data):
        tmp[i] = j
        print(f"{i+1} {j}")
    for i in range(len(data) + 1):
        s = input('Введите номер блюда из списка или "e" для завершения\n')
        if s == 'e':
            break
        elif 1 <= int(s) <= len(data):
            order.append(tmp.get(int(s) - 1))
        else:
            print(f'Номер {s} блюда введен неверно')
    print('Ваш заказ:', ', '.join(order))
    return order


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


#pprint(read_file(), sort_dicts=False)
#pprint(orders_ing(read_file(), 'Омлет',3), sort_dicts=False)
#input_orders()
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3), sort_dicts=False)
