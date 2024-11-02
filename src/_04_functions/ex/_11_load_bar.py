def deci(a):
    b = ['.']

if __name__ == '__main__':
    a = int(input())
    b = (a // 10) * '%' 
    c = (10 - a // 10) * '.'
    if a != 100:
        print(f'{a}% [{b + c}]\nStill loading...')
    else:
        print(f'100% Complete!\n[%%%%%%%%%%]')

