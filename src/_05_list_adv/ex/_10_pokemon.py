def increase_decrease(a, b):
    if b < 0:
        c = a.pop(0)
        if len(a) > 0:
            a.insert(0, a[-1])
            for i, x in enumerate(a):
                if x <= c:
                    a[i] = x + c
                elif x > c:
                    a[i] = x - c


    elif b > len(a) - 1:
        c = a.pop(-1)
        a.append(a[0])
        for i, x in enumerate(a):
            if x <= c:
                a[i] = x + c
            elif x > c:
                a[i] = x - c
        
    else:
        c = a.pop(b)
        if len(a) > 0:
            for i, x in enumerate(a):
                if x <= c:
                    a[i] = x + c
                elif x > c:
                    a[i] = x - c
        else:
            return [], c
    return a, c

    


if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = int(input())
    c, d = increase_decrease(a, b)
    e = []
    while len(a) > 0:
        e += [d] 
        b = int(input())
        c, d = increase_decrease(c, b)
    e += [d] 
    print(sum(e))
