def list_transformation(a):
    a = list(map(int, a.split()))
    return a

def format_txt(b):
    b = list(map(str, b.split(' ')))
    return b

def exchange(a, b):
    try:
        if len(a) < int(b[1]) + 1 or int(b[1]) < 0:
            raise IndexError()
        c = a[:int(b[1]) + 1]
        d = a[int(b[1]) + 1:]
        e = d + c
        return e
    except IndexError:
        return 'Invalid index'

#! --

def max_odd(a):
    c = 0
    c_ = 0
    for i, x in enumerate(a):
        if x % 2 != 0:
            if x >= c:
                c = x
                c_ = i
    if c_ != 0:
        return c_
    else: 
        return 'No matches'

def max_even(a):
    c = None
    c_ = -1 
    for i, x in enumerate(a):
        if x % 2 == 0:
            if c is None or x >= c:
                c = x
                c_ = i
    if c != None:
        return c_
    else:
        return "No matches" 

#! --

def min_odd(a):
    c = None
    c_ = -1 
    for i, x in enumerate(a):
        if x % 2 != 0:
            if c is None or x <= c:
                c = x
                c_ = i
    if c != None:
        return c_
    else:
        return "No matches" 

def min_even(a):
    c = None
    c_ = -1 
    for i, x in enumerate(a):
        if x % 2 == 0:
            if c is None or x <= c:
                c = x
                c_ = i
    if c != None:
        return c_
    else:
        return "No matches" 

#! --

def first_odd(a, b):
    c = []
    d = a.copy()
    for i in range(b):
        for x, y in enumerate(d):
            if y % 2 != 0:
                c += [y]
                d.pop(x)
                break
    if b > len(a):
        return 'Invalid count'
    else:
        return c

def first_even(a, b):
    c = []
    d = a.copy()
    for i in range(b):
        for x, y in enumerate(d):
            if y % 2 == 0:
                c += [y]
                d.pop(x)
                break
    if b > len(a):
        return 'Invalid count'
    else:
        return c

#! --

def last_odd(a, b):
    c = []
    e = []
    if b > len(a):
        return 'Invalid count'
    else:
        d = a.copy()
        for i in range(b):
            for x, y in enumerate(reversed(d)):
                if y % 2 != 0:
                    c += [y]
                    d.remove(y)
                    break
        for i in reversed(c):
            e += [i]
    return e

def last_even(a, b):
    c = []
    e = []
    if b > len(a):
        return 'Invalid count'
    else:
        d = a.copy()
        for i in range(b):
            for x, y in enumerate(reversed(d)):
                if y % 2 == 0:
                    c += [y]
                    d.remove(y)
                    break
        for i in reversed(c):
            e += [i]
    return e

if __name__ == '__main__':
    a = list_transformation(input())
    b = format_txt(input())
    while b[0] != 'end':
        if b[0] == 'exchange':
            if exchange(a, b) != 'Invalid index':
                a = exchange(a, b)
            else:
                print(exchange(a, b))

        elif b[0] == 'max':
            if b[1] == 'odd':
                print(max_odd(a))
            elif b[1] == 'even':
                print(max_even(a))

        elif b[0] == 'min':
            if b[1] == 'odd':
                print(min_odd(a))
            elif b[1] == 'even':
                print(min_even(a))

        elif b[0] == 'first':
            if b[2] == 'odd':
                d = first_odd(a, int(b[1]))
                print(d)
            elif b[2] == 'even':
                d = first_even(a, int(b[1]))
                print(d)
        
        elif b[0] == 'last':
            if b[2] == 'odd':
                d = last_odd(a, int(b[1]))
                print(d)
            if b[2] == 'even':
                d = last_even(a, int(b[1]))
                print(d)

        b = format_txt(input())
    print(a)

