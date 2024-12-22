if __name__ == '__main__':
    a = list(map(int, input().split(', ')))
    b = int(input())
    c = True
    
    if len(a) * b > sum(a):
        print('No equal distribution possible')

    else:
        for i, x in enumerate(a):
            if a[i] < b:
                d = a.index(max(a)) 
                while a[i] != b:
                    a[d] -= 1
                    a[i] += 1

        print(a)
