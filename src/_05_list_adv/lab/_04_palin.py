def da(a):
    b = a.split()
    return b

def find_pa(a):
    b = []
    for i in a:
        if i == i[::-1]:
            b += [i]
    return b

def find_occ(a, b):
    return a.count(b)


if __name__ == '__main__':
    a = input()
    b = input()
    c = a.split()
    d = find_pa(c)
    e = find_occ(d, b)
    print(d)
    print(f'Found palindrome {e} times')



