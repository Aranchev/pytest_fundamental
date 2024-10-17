def da(a, b):
    c = '' 
    for i in range(ord(a) + 1, ord(b)):
        c += f'{chr(i)} '
    return c 

if __name__ == '__main__':
    a = input()
    b = input()
    c = da(a, b)
    print(c)
