def da(a):
    b = a.split(', ')
    c = []
    for i, x in enumerate(b):
        if int(x) % 2 == 0:
            c += [i]
    return c

if __name__ == '__main__':
    a = input()
    print(da(a))
