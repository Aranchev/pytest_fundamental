dictionary = {}
pair = input().split(': ')
b = 0

while len(pair) > 1:

    if pair[0] in dictionary:
        dictionary[pair[0]] += int(pair[1])
    else:
        dictionary[pair[0]] = int(pair[1])

    pair = input().split(': ')

print('Products in stock:')

for values, keys in zip(dictionary.keys(), dictionary.values()):
    a = ': '.join([values, str(keys)])
    print(f'- {a}')

for i in dictionary.values():
    b += i

print(f'Total Products: {len(dictionary)}')
print(f'Total Quantity: {b}')
