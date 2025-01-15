if __name__ == '__main__':
    a = input().split(', ')
    b = input().split(' - ')
    while b[0] != 'Craft!':
        if b[0] == 'Collect':
            if b[1] not in a:
                a += [b[1]]
        elif b[0] == 'Drop':
            if b[1] in a:
                a.remove(b[1])
        elif b[0] == 'Combine Items':
            c = b[1].split(':')
            if c[0] in a:
                a.insert(a.index(c[0]) + 1, c[1])
            else:
                pass
        elif b[0] == 'Renew':
            if b[1] in a:
                g = a.pop(a.index(b[1]))
                a.append(g)
        b = input().split(' - ')
    print(', '.join(a))
