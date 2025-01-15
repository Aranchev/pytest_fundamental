# https://alpha.judge.softuni.org/contests/06-programming-fundamentals-mid-exam-retake/1773/practice#1

def loot(a, b):
    for i in b[1:]:
        if i not in a:
            a.insert(0, i)
    return a

def drop(a, b):
    try:
        c = a.pop(int(b[1]))
        a.append(c)
    except IndexError:
        pass
    return a

def steal(a, b):
    d = []
    try:
        for i in range(int(b[1])):
            c = a.pop()
            d.insert(0, c)
    except IndexError:
        return a, d
    return a, d

if __name__ == '__main__':
    a = input().split('|')
    b = input().split()
    d = 0
    while b[0] != 'Yohoho!':
        if b[0] == 'Loot':
            a = loot(a, b)
        elif b[0] == 'Drop':
            a = drop(a, b)
        elif b[0] == 'Steal':
            a, c = steal(a, b)
            print(', '.join(c))
        b = input().split()
    if len(a) > 0:
        for i in a:
            d += len(i) / len(a)
        print(f'Average treasure gain: {d:.2f} pirate credits.')
    else:
        print('Failed treasure hunt.')

