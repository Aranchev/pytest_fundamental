def number(a, b, c):
    d = 0
    for i in [a, b, c]:
        if i == 0:
            return 'zero'
    for i in [a, b, c]:
        if i > 0:
            d += 1
    if d % 2 == 0:
        return 'negative'
    elif d % 2 != 0:
        return 'positive'


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(number(a,b,c))
