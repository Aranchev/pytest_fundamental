def numbers_letters(a):
    numbers = []
    letters = []
    for i in a:
        if i.isdigit():
            numbers += [i]
        else:
            letters += [i]
    return numbers, letters

def take_skip_numbers(a):
    take = []
    skip = []
    for i, x in enumerate(a):
        if i % 2 == 0:
            skip.append(int(x))
        else:
            take.append(int(x))
    return take, skip

def finite(a, b, c):
    taken_string = []
    for i, x in list(zip(b, c)):
        for s in range(i):
            if len(a) > 0: 
                f = a.pop(0)
                taken_string += [f]
        for p in range(x):
            if len(a) > 0:
                f = a.remove(a[0])
    return taken_string



if __name__ == '__main__':
    a = list(input())
    numbers, letters = numbers_letters(a)
    take, skip = take_skip_numbers(numbers)
    taken_string = finite(letters, skip, take)
    print(''.join(taken_string))

