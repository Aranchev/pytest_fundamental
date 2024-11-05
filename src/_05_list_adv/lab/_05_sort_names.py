def sp_l(a):
    b = a.split(', ')
    c = sorted(b, key=lambda x: (-len(x), x))
    return c

if __name__ == '__main__':
    a = input()
    print(sp_l(a))

