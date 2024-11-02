if __name__ == '__main__':
    a = int(input())
    b = [0 for _ in range(a)]  

    while True:
        c = input()
        d = c.split()
        if d[0] == 'End':
            break
        elif d[0] == 'add':
            b[-1] += int(d[1])
        elif d[0] == 'insert' and 0 <= int(d[1]) < a:
            b[int(d[1])] += int(d[2])
        elif d[0] == 'leave' and 0 <= int(d[1]) < a:
            b[int(d[1])] -= int(d[2])

    print(b)
