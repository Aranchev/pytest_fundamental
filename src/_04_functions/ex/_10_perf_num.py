def number(a):
    b = 0
    for i in range(1, a):
        if a % i == 0:
            b += i
    if b == a:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."

if __name__ == '__main__':
    a = int(input())
    print(number(a))


