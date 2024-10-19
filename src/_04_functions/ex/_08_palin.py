# palindrome, zip()

def isol(a):
    b = a.split(', ')
    return b

def vrut(a):
    results = []  # Store results instead of printing
    for i in a:
        b = True
        for x, y in zip(i, reversed(i)):
            if x != y:
                b = False
        if b:
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    a = input()
    b = isol(a)
    c = vrut(b)
    for i in c:
        print(i)

'''
k1lgor:

def check():
    for element in nums:
        if element == element[::-1]:
            print('True')
        else:
            print('False')
            
nums = input().split(', ')
check()
'''
#! the function check() works without receiving any parameters because the variable nums is declared in the global scope.





