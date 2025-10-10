inp = input().split(' -> ')
dicto = {}

while 'End' not in inp:
    if inp[0] not in dicto:
        dicto[inp[0]] = [inp[1]]
    elif inp[1] in dicto[inp[0]]:
        pass
    else:
        dicto[inp[0]] += [inp[1]]
    inp = input().split(' -> ')

"""
Alternative:
if ID not in user[company] and company in user:
    user[company].append(ID)
"""
for i in dicto.items():
    print(i[0])
    for x in i[1]:
        print(f"-- {x}")
