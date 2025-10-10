
inp = input().split()
dicto = {}

while inp[0] != 'buy':
    if inp[0] not in dicto:
        dicto[inp[0]] = [float(inp[1]), int(inp[2])]
    elif inp[0] in dicto:
        dicto[inp[0]][0] = float(inp[1])
        dicto[inp[0]][1] += int(inp[2])
    
    inp = input().split()


for i, x in dicto.items():
    print(f"{i} -> {x[0] * x[1]:.2f}")





