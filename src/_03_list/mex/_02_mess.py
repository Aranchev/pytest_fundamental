def char_string(string):
    b = []
    for i in string:
        b += i
    return b 

def num_sum(num):
    a = num.split(' ')
    z = []
    for i in a:
        y = 0
        for x in i:
            y += int(x)
        z += [y]
    return z

def vurtalejka(num, string):
    a = num_sum(num)  
    b = char_string(string)
    k = ''
    for i in a:
        z = int(i)
        while z != -1:
            for i, x in enumerate(b): 
                z -= 1    
                if z == -1:
                    j = b.pop(i)     
                    k += f'{j}' 
                    break
    return k           
if __name__ == '__main__':
    #@ char_string
    num = input()
    string = str(input())
    b = char_string(string)
    c = num_sum(num)
    d = vurtalejka(num, string)
    print(d)
    
    
