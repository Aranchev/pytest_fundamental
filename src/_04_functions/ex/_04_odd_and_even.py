def da(a: str):
    even = 0
    uneven = 0

    for i in a:
        if int(i) != 0:
            if int(i) % 2 == 0:
                even += int(i)
            elif int(i) % 2 != 0:
                uneven += int(i)
    return f'Odd sum = {uneven}, Even sum = {even}'

if __name__ == '__main__':
    a = input()
    b = da(a)
    print(b)


