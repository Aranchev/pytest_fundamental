def fire(a, b):
    try:
        index = int(b[1])
        damage = int(b[2])
        if 0 <= index < len(a):
            a[index] -= damage
    except (IndexError, ValueError):
        pass
    return a
def defend(a, b):

    index1 = int(b[1])
    index2 = int(b[2])

    if index1 >= 0 and index1 < len(a) and index2 >= 0 and index2 < len(a):
        for i in range(index1, index2 + 1):
            a[i] -= int(b[3])
        return a
    else:
        return a

def repair(a, b, c):
    
    if int(b[1]) >= 0 and int(b[1]) < len(a):
        if a[int(b[1])] + int(b[2]) <= c:  
            a[int(b[1])] += int(b[2])
        else:
            a[int(b[1])] = c
        return a
    else:
        return a

def status(a, b):
    c = 0
    for i in a:
        if i < b * 0.2:
            c += 1
    return c


if __name__ == '__main__':
    a = list(map(int, input().split('>'))) # pirate ship
    b = list(map(int, input().split('>'))) # warship
    c = int(input())
    d = input().split()
    e = True
    f = 0
    g = 0
    
    while d[0] != 'Retire':
        if d[0] == 'Fire':
            b = fire(b, d)
            for i in b:
                if i <= 0:
                    e = False
                    print('You won! The enemy ship has sunken.')
                    break
        elif d[0] == 'Defend':
            a = defend(a, d)
            for i in a:
                if i <= 0:
                    e = False
                    print('You lost! The pirate ship has sunken.')
                    break
        elif d[0] == 'Repair':
            a = repair(a, d, c)
        elif d[0] == 'Status':
            print(f'{status(a, c)} sections need repair.')
        if e == False:
            break
        d = input().split()
    for i in a:
        f += i
    for i in b:
        g += i
    if e == True:
        print(f'Pirate ship status: {f}')
        print(f'Warship status: {g}')

