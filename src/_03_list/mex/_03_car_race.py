# round(), list()
def sequence(seq):
    a = seq.split(' ')
    return a 

def racer1(a, b):
    c = []
    for i, x in enumerate(a):
        if i == b:
            break
        c += [int(x)]
    return c

def racer2(a, b):
    c = []
    for i, x in reversed(list(enumerate(a))): 
        if i == b:
            break
        c += [int(x)]
    return c

def racer_time(c):
    a = 0
    for i in c:
        if i == 0:
            a *= 0.8
        a += i
    return a

if __name__ == '__main__':
    seq = input()
    a = sequence(seq)
    b = int((len(a) - 1) / 2)
    c = racer1(a, b)
    d = racer2(a, b)
    e = racer_time(c)
    f = racer_time(d)
    if e < f:
        print(f'The winner is left with total time: {e:.1f}')
    else:
        print(f'The winner is right with total time: {f:.1f}')
