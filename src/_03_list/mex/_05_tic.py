#@ list(map(int, input().split())) | This is gut 

def da(a, b, c):
    a = a.split(' ')
    b = b.split(' ')
    c = c.split(' ')
    e = []
    f = []
    g = []
    for i in a:
        e += [int(i)]
    for i in b:
        f += [int(i)]
    for i in c:
        g += [int(i)]
    return e, f, g

def player_1(a, b, c):
    a, b, c = da(a, b, c)
    if (a[0] == 1 and b[0] == 1 and c[0] == 1)\
    or (a[1] == 1 and b[1] == 1 and c[1] == 1)\
    or (a[2] == 1 and b[2] == 1 and c[2] == 1)\
    or (a[0] == 1 and a[1] == 1 and a[2] == 1)\
    or (b[0] == 1 and b[1] == 1 and b[2] == 1)\
    or (c[0] == 1 and c[1] == 1 and c[2] == 1)\
    or (a[0] == 1 and b[1] == 1 and c[2] == 1)\
    or (a[2] == 1 and b[1] == 1 and c[0] == 1):
        return 1
    elif (a[0] == 2 and b[0] == 2 and c[0] == 2)\
    or (a[1] == 2 and b[1] == 2 and c[1] == 2)\
    or (a[2] == 2 and b[2] == 2 and c[2] == 2)\
    or (a[0] == 2 and a[1] == 2 and a[2] == 2)\
    or (b[0] == 2 and b[1] == 2 and b[2] == 2)\
    or (c[0] == 2 and c[1] == 2 and c[2] == 2)\
    or (a[0] == 2 and b[1] == 2 and c[2] == 2)\
    or (a[2] == 2 and b[1] == 2 and c[0] == 2):
        return 2
    else:
        return 0


if __name__ == '__main__':
    a = input()
    b = input()
    c = input()
    d = player_1(a, b, c)
    if d == 1:
        print('First player won')
    elif d == 2:
        print('Second player won')
    else:
        print('Draw!')
