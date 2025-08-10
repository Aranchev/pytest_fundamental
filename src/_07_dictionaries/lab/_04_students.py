# capturing stdout/stderr output

def cor_course(course, my_dict):
    list_of_values = ''
    a = ' '.join(course.split('_'))

    for key, value in my_dict.items():
        for nested_key, nested_value in value.items():
            if nested_value == course or nested_value == a:
                list_of_values += f'{key} - {nested_key}\n'

    return list_of_values


if __name__ == '__main__':
    inp = input().split(':')
    students = {}

    while len(inp) > 1:
        students[inp[0]] = {}
        students[inp[0]][int(inp[1])] = inp[2]
        inp = input().split(':')

    print(cor_course(inp[0], students))
