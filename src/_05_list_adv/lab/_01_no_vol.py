def da(b):
    return ''.join([i for i in b if i not in ['a', 'o', 'u', 'e','i', 'A', 'O', 'U', 'E', 'I']])

if __name__ == '__main__':
    a = da(input())
    print(a)

