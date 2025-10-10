def post_split_operation(inp, dicto):
    if inp[0] in dicto.keys():
        for x, y in dicto.items():
            if x == inp[0]:
                if y[0] == inp[1]:
                    if int(y[1]) < int(inp[2]):
                        dicto[x][1] = int(inp[2])
                        return dicto
    elif inp[0] not in dicto.keys():
        dicto[inp[0]] = [inp[1], int(inp[2])]

    return dicto

def counting_courses(inp):
    if inp not in courses.keys():
        courses[inp] = [inp]
    else:
        courses[inp].append(inp)
    return courses




if __name__ == '__main__':
    inp = input()
    dicto = {}
    courses = {}

    while 'exam finished' not in inp:
        if 'banned' not in inp:
            split_list = inp.split('-')
            counting_courses(split_list[1])
            post_split_operation(split_list, dicto)
        else:
            split_banned = inp.split('-')
            dicto.pop(split_banned[0])
        
        inp = input()

print('Results:')
for x, y in dicto.items():
    print(f'{x} | {y[1]}')
print('Submissions:')
for x, y in courses.items():
    print(f'{x} - {len(y)}')
