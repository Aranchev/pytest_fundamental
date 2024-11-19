def da(a):
    return list(map(int, a.split('.')))

if __name__ == '__main__':
    a = da(input())
    b = True 


    for i in range(a[0], 10):
        for x in range(a[1], 10):
            for y in range(a[2], 10):


