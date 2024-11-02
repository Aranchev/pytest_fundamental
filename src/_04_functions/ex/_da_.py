def rem(a, b):
    c = a.split(' ')
    d = b.split('|')
    d.pop(int(c[1]))
    return ' '.join(d)

def add(a, b):
    c = a.split(' ')

if __name__ == '__main__':
    a = input()
    b = a.split('|')
    c = input()
    
    while c != 'Done':
        e = []
        g = ''
        f = c.split(' ')
        try:
            if f[0] == 'Remove':
                b.pop(int(f[1]))
        except IndexError:
            pass
        if f[0] == 'Add' and len(f) >= int(f[2]):
            b.insert(int(f[2]), f[1])
        if f[0] == 'Check':
            if f[1] == 'Even':
                for i,x in enumerate(b):
                    if i % 2 == 0:
                        e += [x]
                e = ' '.join(e)
                print(e)
            elif f[1] == 'Odd':
                for i, x in enumerate(b):
                    if i % 2 != 0:
                        e += [x]
                e = ' '.join(e)
                print(e)
        c = input()

    g = ''.join(b)
    

print(f'You crafted {g}!')

                  
    
    


