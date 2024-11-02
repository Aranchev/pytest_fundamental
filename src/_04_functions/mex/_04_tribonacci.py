def number(a):
    if a == 1:
        b = [1]
        return b
    elif a == 2:
        b = [1, 1]
        return b
    elif a >= 3:
        b = [1, 1, 2]
        while len(b) < a:
            b += [sum(b[-3:])] 
        return b

if __name__ == '__main__':    
    a = int(input())
    b = list(map(str, number(a)))
    c = ' '.join(b)
    print(c)



