# max(), min()

import math

def da(a, b, c):
    d = [int(a), int(b), int(c)]
    return min(d)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = da(a, b, c)
    print(d)
