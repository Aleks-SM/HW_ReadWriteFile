from pprint import pprint
from HW_1_ReadFile import get_shop_list_by_dishes
from HW_2_ReadFile import read_from_file

if __name__ == '__main__':
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    read_from_file()
