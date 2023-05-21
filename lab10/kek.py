import json

with open('products.json', 'r', encoding='utf-8') as fl:
    txt = json.load(fl)

for t in txt['products']:
    print('Название:', t['name'])
    print('Цена:', t['price'])
    print('Вес: ', t['weight'])
    if t['available']:
        print('В наличии')
    else:
        print('Нет в наличии')

name = input()
price = input()
weight = input()
available = input()

txt['products'].append(
    {'name': f'{name}', 'price': f'{price}', 'weight': f'{weight}', 'available': f'{available}'}
)

print(txt)