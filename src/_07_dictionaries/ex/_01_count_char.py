a = input().replace(' ', '')
b = {}

for i in a:
    if i not in b:
        b[i] = 1
    elif i in b:
        b[i] += 1


for i in b.items():
    print(f'{i[0]}' + ' -> ' + f'{i[1]}')
