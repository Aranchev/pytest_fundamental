def pos(a, b, c, d, e):
    x = [a, b, c, d, e]
    y = []
    z = []
    for i in x:
        if int(i) >= 0:
           y += [i]
    return len(y) 

def neg(a, b, c, d, e):
    x = [a, b, c, d, e]
    y = []
    for i in x:
        if int(i) < 0:
           y += [i]
    return len(y) 

def count(a, b, c, d, e):
    x = [a, b, c, d, e]
    y = 0
    for i in x:
        y += 1
    return y

def sum_neg(a, b, c, d, e):
    x = [a, b, c, d, e]
    y = 0
    for i in x:
        if int(i) < 0:
            y += int(i)
    return y




if __name__ == '__main__':
    a = int(input())
    c = []
    pos = []
    neg = []
    c_neg = 0
    for i in range(int(a)):
        b = int(input())
        c += [b]

    for i in c:
        if int(i) > 0:
            pos += [i]
        elif int(i) < 0:
            neg += [i]
    for i in neg:
        c_neg += int(i)



    print(pos)
    print(neg)
    print('Count of positives:' + ' ' + f'{len(pos)}')
    print(f'Sum of negatives: {c_neg}')
    
