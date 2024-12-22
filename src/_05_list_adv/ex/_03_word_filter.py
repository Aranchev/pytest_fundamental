if __name__ == '__main__':
    a = input().split(' ')
    b = [print(i, end='\n') for i in a if len(i) % 2 == 0]


