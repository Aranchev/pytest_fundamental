def da(a, b):
    if a == 'int':
        print(int(b) * 2)
    elif a == 'real':
        print(f'{float(b) * 1.5:.2f}')
    elif a == 'string':
        print('$' + f'{b}' + '$')


if __name__ == '__main__':
    a, b = input(), input()
    da(a, b)
