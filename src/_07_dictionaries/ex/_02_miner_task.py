dicto = {}

while True:
    a = input()
    if a == 'stop':
        break
    else:
        b = input()
    if a not in dicto:
        dicto[a] = int(b)
    else:
        dicto[a] += int(b)

for i in dicto.items():
    print(f'{i[0]}' + ' -> ' + f'{i[1]}')
