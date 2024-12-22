if __name__ == '__main__':
    a = list(map(int, input().split(', ')))
    b = 10

    while len(a) > 0:
        d = [x for x in a if x <= b]
        a = [x for x in a if x > b]
        print(f"Group of {b}'s: {d}")
        b += 10
