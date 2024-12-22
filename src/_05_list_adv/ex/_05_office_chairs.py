if __name__ == '__main__':
    n = int(input())  # the number of room
    c = 0
    d = 0
    for i in range(1, n+1):
        b = input().split(' ')
        c += len(b[0])
        d += int(b[1])
        if len(b[0]) < int(b[1]):
            print(f'{int(b[1]) - len(b[0])} more chairs needed in room {i}')
    if c >= d:
        print(f'Game On, {c - d} free chairs left')
