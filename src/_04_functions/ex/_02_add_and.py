def add_and_substract(a, b, c):

    def sum_numbers(a, b):
        return a + b
    
    def substract(d, c):
        return d - c
    
    d = sum_numbers(a, b)
    e = substract(d, c)
    
    print(e)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    add_and_substract(a, b, c)
    
