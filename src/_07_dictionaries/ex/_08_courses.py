inp = input().split(' : ')
dicto = {}

while len(inp) > 1:
    if inp[0] not in dicto:
        dicto[inp[0]] = [inp[1]]
    else:
        dicto[inp[0]] += [inp[1]]
    # name, user = command.split(" : ")
    inp = input().split(' : ')

for i in dicto.items():
    print(f"{i[0]}: {len(i[1])}")
    for x in i[1]:
        print(f"-- {x}")
