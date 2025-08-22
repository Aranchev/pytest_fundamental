countries = input().split(', ')
capitals = input().split(', ')

dicto = {x: y for x, y in zip(countries, capitals)}


for i in dicto.items():
    print(f'{i[0]}' + ' -> ' + f'{i[1]}')
