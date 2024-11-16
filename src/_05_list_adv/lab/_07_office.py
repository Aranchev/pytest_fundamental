

if __name__ == '__main__':
    a = input()
    b = int(input())

    c = list(map(int, a.split(' ')))
    d = list(map(lambda x: x * b, c))
    e = list(map(str, d))
    f = list(filter(lambda x: x >= sum(d)/len(d), d))
    if len(f) < len(d) / 2:
        print(f'Score: {len(f)}/{len(d)}. Employees are not happy!')
    else:
        print(f'Score: {len(f)}/{len(d)}. Employees are happy!')

