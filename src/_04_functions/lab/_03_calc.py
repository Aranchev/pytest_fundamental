def add(c, d: int):
    return c + d

def subtract(c, d: int):
    return c - d

def multiply(c, d):
    return c * d

def divide(c, d):
    return c / d

if __name__ == '__main__':
    a = str(input())
    b = int(input())
    c = int(input())
    
    if a == 'add':
        print(int(add(b, c)))
    elif a == 'subtract':
        print(int(subtract(b, c)))
    elif a == 'multiply':
        print(int(multiply(b, c)))
    elif a == 'divide':
        print(int(divide(b, c)))

