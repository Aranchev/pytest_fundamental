def merge(a, b, c):
    if  b < 0:
        b = 0
    if c > len(a) - 1:
        c = len(a) - 1
    for index, string in enumerate(a):
        if index in range(b + 1, c + 1):
            a[b] += a[index]
    for index in range(c, b, - 1):
        a.pop(index)
    return a

def divide(a, b, c):
    d = []
    e = 0
    if len(a[b]) % c == 0:
        for i in range(c):
            d += [a[b][i + e: i + e + int(len(a[b]) / c)]]
            e += int(len(a[b]) / c) - 1
        a[b] = d
        a = a[:b] + a[b] + a[b + 1:]
        return a
    else:
        for i in range(c):
            if c - i == 1:
                d += [a[b][i + e:]]
                break
            d += [a[b][i + e: i + e + int(len(a[b]) / c)]]
            e += int(len(a[b]) / c) - 1
        a[b] = d
        a = a[:b] + a[b] + a[b + 1:]
        return a

if __name__ == '__main__':
    a = input().split(' ')
    b = input().split(' ')

    while b[0] != '3:1':
        if b[0] == 'merge':
            a = merge(a, int(b[1]), int(b[2]))
        elif b[0] == 'divide':
            a = divide(a, int(b[1]), int(b[2])) 

        b = input().split(' ')
    print(' '.join(a))
