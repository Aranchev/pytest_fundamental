# round()

def da(a):
    b = a.split(' ')
    c = []
    for i in b:
        c += [round(float(i))]
    return c

if __name__ == '__main__':
    a = input()
    b = da(a)
    print(b)


