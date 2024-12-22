def attacks(a):
    b = a.split(' ') 
    c = []
    for i in b:
        c += [list(map(int, i.split('-')))]
    return c

def eliminate_zeros(a):
    for i, x in enumerate(a):
        for z, y in enumerate(x):
            if a[i][z] == 0:
                a [i][z] = 'x'
    return a

def ship_wreck(a, b):
    wrecked = 0
    for i in b:
        if a[i[0]][i[1]] != 'x':
            if a[i[0]][i[1]] > 0:   
                a[i[0]][i[1]] -= 1
                if a[i[0]][i[1]] == 0:
                    wrecked += 1
    return wrecked

if __name__ == '__main__':
    rows = int(input())
    c = []
    field = []
    for i in range(rows):
        b = input()
        c += [b]
    for i in c:
        field += [list(map(int, i.split(' ')))]

    attack = attacks(input())



    field = eliminate_zeros(field)
    wreck = ship_wreck(field, attack)
    print(wreck)

