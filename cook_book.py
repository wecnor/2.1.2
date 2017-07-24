def read_json():
    import json
    with open('cook_book.json', encoding='utf8') as f:
        cook_book = json.load(f)
    return cook_book


def read_yaml():
    import yaml
    with open('cook_book.yml', encoding='utf8') as f:
        cook_book = yaml.load(f)
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, people_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= people_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print ('{ingredient_name} {quantity} {measure}'.format(**shop_list_item))


def main():
    type_of_file = input('Выберите:\n'
                             '0 - Чтение файла YAML\n'
                             '1 - Чтение файла JSON\n')
    if type_of_file == '0':
        cook_book = read_yaml()
    elif type_of_file == '1':
        cook_book = read_json()
    else:
        print ('Неверный выбор')
        exit(0)
    people_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, people_count)
    print_shop_list(shop_list)

main()