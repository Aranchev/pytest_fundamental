def first_input(a, b, c):
    return [b, c]


if __name__ == '__main__':
    a = int(input())
    c = []
    for i in range(a):
        b = input()
        c += [b]
    print(c)
