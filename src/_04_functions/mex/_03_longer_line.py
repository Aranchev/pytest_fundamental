from math import sqrt, floor

def lenght(x1, y1, x2, y2, x3, y3, x4, y4):
    line1 = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    line2 = sqrt(pow(x4 - x3, 2) + pow(y4 - y3, 2))
    return round(line1, 2), round(line2, 2)

def distance(x1, y1, x2, y2, x3, y3, x4, y4):
    a = sqrt(pow(x1, 2) + pow(y1, 2))
    b = sqrt(pow(x2, 2) + pow(y2, 2))
    c = sqrt(pow(x3, 2) + pow(y3, 2))
    d = sqrt(pow(x4, 2) + pow(y4, 2))
    return a, b, c, d

if __name__ == '__main__':
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x3 = float(input())
    y3 = float(input())
    x4 = float(input())
    y4 = float(input())
    a, b = lenght(x1, y1, x2, y2, x3, y3, x4, y4)
    c, d, e, f = distance(x1, y1, x2, y2, x3, y3, x4, y4)
    if a >= b:
        if c <= d:
            print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
        else:
            print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y2)})')
    elif e <= f:
        print(f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})')
    else:
        print(f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})')
