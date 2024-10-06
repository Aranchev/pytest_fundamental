def lst(a, b):
    c = a.split(' ')
    return c

def rot(a, b):
    c = []
    while len(a) >= 1:
        d = b
        for i, x in enumerate(a):
            d -= 1
            if d == 0:
                e = a.pop(i)
                c += [int(e)]
    return c



if __name__ == '__main__':
    a = input()
    b = int(input())

