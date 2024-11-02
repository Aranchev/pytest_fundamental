import math

def first_fact(a):
    b = [] 
    c = 0
    for i in range(1, a+1):
        b += [int(i)]
    
    return math.prod(b)

if __name__ == '__main__':
    a = first_fact(int(input()))
    b = first_fact(int(input()))
    print(f'{a / b:.2f}')
    



