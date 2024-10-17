def da(a, b):
    if a == 'coffee':
        return b * 1.50
    elif a == 'water':
        return b * 1.00
    elif a == 'coke':
        return b * 1.40
    elif a == 'snacks':
        return b * 2.00

if __name__ == '__main__':
    a = input()
    b = int(input())
    c = da(a, b)
    print(f'{c:.2f}')



