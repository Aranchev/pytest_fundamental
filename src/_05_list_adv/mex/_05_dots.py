def localize_dot(a):
    dot_location = []
    
    for b, c in enumerate(a):
        for e, f in enumerate(c):
            if f == '.':
                dot_location = [b, e]
                break
        else:
            continue
        break
    
    return dot_location

def check_sides(a, b):
    U = True 
    D = True 
    L = True 
    R = True

    if b[0] >= 1:
        try:
            if a[b[0] - 1][b[1]] in ['-', 'x']:
                U = False
        except IndexError:
            U = False
    else:
        U = False

    try:    
        if a[b[0] + 1][b[1]] in ['-', 'x']:
            D = False
    except IndexError:
        D = False
    if b[1] >= 1:
        try:
            if a[b[0]][b[1] - 1] in ['-', 'x']:
                L = False
        except IndexError:
            L = False
    else:
        L = False
    try:
        if a[b[0]][b[1] + 1] in ['-', 'x']:
            R = False
    except IndexError:
        R = False
     
    z = [x for x, y in enumerate((U, D, L, R)) if y == True]
    
    a[b[0]][b[1]] = 'x'

    return z, a

#! тази cont() функция трябва да работи с множество от параметри

def cont(a, b):
    e = []

    for i in b:
        if i == 0:
            e += [[a[0] - 1, a[1]]]
        elif i == 1:
            e += [[a[0] + 1, a[1]]]
        elif i == 2:
            e += [[a[0], a[1] - 1]]
        elif i == 3:
            e += [[a[0], a[1] + 1]]

    return e


def check_sides_two(a, b):
    d = [] 
    e = []
    f = []
    for i in b:
        c, o = check_sides(a, i)
        d += [c]
    return d, a

def zipidi(a, b, c):
    e = []
    f = []
    d = list(zip(a, b))

    for i in d:
        for x in i[1]:
            if x == 0:
                e += [[i[0][0] - 1, i[0][1]]]
            elif x == 1:
                e += [[i[0][0] + 1, i[0][1]]]
            elif x == 2:
                e += [[i[0][0], i[0][1] - 1]]
            elif x == 3:
                e += [[i[0][0], i[0][1] + 1]]

    for i in e:
        if i not in f:
            f.append(i)

    for i in f:
        c[i[0]][i[1]] = 'x'

    return f, c


if __name__ == '__main__':
    a = int(input())
    b = [input().split(' ') for i in range(a)]
    c = localize_dot(b)
    d, e = check_sides(b, c)
    f = cont(c, d)
    g, h = check_sides_two(e, f) 
    i = zipidi(f, g, h)
    print(i)
    
