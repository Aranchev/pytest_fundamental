# ','.join(map(str, d)), split(), pop(), append 
def lst(a):
    b = []
    c = a.split(' ')
    for i in c:
        b += [int(i)]
    return b

def spin(a, b):
    c = []
    d = []
    e = []
    f = []
    j = []
    k = []
    l = []
    while len(a) > 1:    
        g = b
        while g > 0: 
            for i, x in enumerate(a):
                g -= 1
                if g == 0:
                    c = a.pop(i)
                    d += [c]
                    j = a[:i]
                    k = a[i:]
                    a = k
                    a += j
                    break
            if g > 0:
                e = a[-1] 
                f = a[:-1]
                a = [e]
                a += f
                g += 1
    d += a
    m = ','.join(map(str, d)) 

    return f'[{m}]' 

if __name__ == '__main__':
    a = input()
    b = int(input())
    c = lst(a)
    d = spin(c, b)
    print(d)

'''
K1LGOR'S INSANE SOLUTION:

n = input().split()
k = int(input())
start = 0
exe = []
for _ in range(len(n)):
    start = (start + k - 1) % len(n)
    exe.append(n.pop(start))
result = '[' + ','.join(exe) + ']'
print(result, end='')
'''
