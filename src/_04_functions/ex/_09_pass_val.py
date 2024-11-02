def lenght(a):
    if 6 > len(a) or len(a) > 10:
        return 'Password must be between 6 and 10 characters'

def let_num(a):
    b = 0
    for i in a:
        if i.isalnum():
            b += 1
    if b != len(a):
        return 'Password must consist only of letters and digits' 

def at_least(a):
    b = 0
    for i in a:
        if i.isdigit():
            b += 1
    if not b >= 2:
        return 'Password must have at least 2 digits'

if __name__ == '__main__':
    a = input()

    if lenght(a) != None:
        print(lenght(a))
    if let_num(a) != None:
        print(let_num(a))
    if at_least(a) != None:
        print(at_least(a))

    if lenght(a) == None and let_num(a) == None and at_least(a) == None:
        print('Password is valid')




