dictionary = {} 
pair = input().split(': ')
b = 0

while len(pair) > 1:

    if pair[0] in dictionary:
        dictionary[pair[0]] += int(pair[1])
    else:
        dictionary[pair[0]] = int(pair[1])

    pair = input().split(': ')

"""
while command != 'statistics':

    args = command.split(': ')
    product = args[0]
    quantity = int(args[1])

    if product not in products:
        products[product] = 0
    products[product] += quantity
"""

print('Products in stock:')

for values, keys in zip(dictionary.keys(), dictionary.values()):
    a = ': '.join([values, str(keys)])
    print(f'- {a}')

"""
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
"""

for i in dictionary.values():
    b += i

print(f'Total Products: {len(dictionary)}')
"""
print(f"Total Products: {len(products.keys())}")
"""

print(f'Total Quantity: {b}')
"""
print(f"Total Quantity: {sum(products.values())}")
"""

