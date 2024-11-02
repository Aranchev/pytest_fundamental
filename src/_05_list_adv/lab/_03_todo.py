# ['2-Walk the dog', '1-Drink coffee', '6-Dinner', '5-Work']
import sys

def split_str(a):
    b = [x.replace('-', ' ') for x in a]
    return b

def order(a):
    b = int(a[0][0])
    for i, x in enumerate(a):
        if int(x[0]) >= b:
            c = a.pop(i)
            a.append(c)
        else:
            b == x[0]
    return a

# остава да се подредят

# https://softuni.bg/trainings/resources/pdf/103641/presentaion-programming-fundamentals-with-python-september-2024/4693 


if __name__ == '__main__':
    b = []
    while True:
        a = input()
        if a == 'End':
            break
        b += [a]
    print(b)



