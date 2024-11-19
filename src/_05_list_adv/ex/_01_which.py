def lit(a):
    return a.split(', ')

if __name__ == '__main__':
    a = lit(input())
    b = lit(input())
    c = []
    for i in a:
        for x in b:
            if i in x:
                c += [i]
    print(list(dict.fromkeys(c)))
