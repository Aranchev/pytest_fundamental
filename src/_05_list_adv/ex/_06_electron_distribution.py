if __name__ == '__main__':
    a = int(input())
    b = []
    c = 1
    
    while a > 0 and a > 2 * c ** 2:
        a -= 2 * c ** 2
        b += [2 * c ** 2]
        c += 1
    if a > 0:
        b += [a]
    print(b)

