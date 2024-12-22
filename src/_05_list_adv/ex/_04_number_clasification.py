def trans(a):
    return list(map(int, a.split(', ')))

def positive(a):
    b = [i for i in a if i >= 0]
    c = ', '.join(list(map(str, b)))
    return c

def negative(a):
    b = [i for i in a if i < 0]
    c = ', '.join(list(map(str, b)))
    return c

def even(a):
    b = [i for i in a if i % 2 == 0]
    c = ', '.join(list(map(str, b)))
    return c

def odd(a):
    b = [i for i in a if i % 2 != 0]
    c = ', '.join(list(map(str, b)))
    return c


if __name__ == '__main__':
    a = input()
    b = trans(a)
    c = positive(b)
    d = negative(b)
    e = even(b)
    f = odd(b)
    print(f'Positive: {c}')
    print(f'Negative: {d}')
    print(f'Even: {e}')
    print(f'Odd: {f}')
    
