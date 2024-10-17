def da(a: float):
    if 2.00 <= a <= 2.99:
        return 'Fail'
    elif 3.00 <= a <= 3.49:
        return 'Poor'
    if 3.50 <= a <= 4.49:
        return 'Good'
    if 4.50 <= a <= 5.49:
        return 'Very Good'
    if 5.50 <= a <= 6.00:
        return 'Excellent'

if __name__ == '__main__':
    a = float(input())
    print(da(a))






