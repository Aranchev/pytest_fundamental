if __name__ == '__main__':
    a = input().split(' ')
    b = []
    d = []
    e = []
    f = []
    for i in a:
        c = [chr(int(''.join(filter(str.isdigit, i))))]
        b += c
        d += [''.join(filter(str.isalpha, i))]
    for i in d:
        if len(i) > 1:
            e += [i[-1] + i[1:-1] + i[0]]
        else:
            e += [i]

    for i in range(len(b)):
        f.append(b[i] + e[i])
    
    print(' '.join(f))
