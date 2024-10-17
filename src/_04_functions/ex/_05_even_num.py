# filter(), list comprehension (k1lgor)
def even(a):
    if a % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    a = input().split(' ')
    b = []
    d = []
    for i in a:
        b += [int(i)]
    c = filter(even, b)
    for i in c:
        d += [i]
    print(d)

'''
k1lgor:
nums = [int(num) for num in input().split()]
List = []

def even_filter(x):
    return x % 2 == 0
    
even = filter(even_filter, nums)

for x in even:
    List.append(x)
    
print(List)
'''
