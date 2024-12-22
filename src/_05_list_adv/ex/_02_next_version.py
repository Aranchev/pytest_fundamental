def da(a):
    return list(map(int, a.split('.')))

if __name__ == '__main__':
    a = da(input())
    
    if a[2] != 9:
        a[2] += 1
    elif a[1] != 9:
        a[1] += 1
        a[2] = 0
    elif a[0] != 9:
        a[0] += 1
        a[1] = 0
        a[2] = 0
    print('.'.join(map(str, a)))

'''
k1lgor's:

version = list(str(int(''.join(input().split('.'))) + 1))
print(f'{version[0]}.{version[1]}.{version[2]}')

'''
