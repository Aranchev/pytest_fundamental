a = input()
b = a.lower()
c =  b.split(' ')
d = {}
o = []
for i in c:
    if i not in d:
        d[i] = 0
for i in c:
    for x in d.keys():
        if i == x:
            d[x] +=1

for (key, value) in d.items():
    if value % 2 != 0:
        o += [key]

print(' '.join(o))
