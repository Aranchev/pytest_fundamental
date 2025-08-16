def cor_course(course, my_dict):
    list_of_values = ''
    a = ' '.join(course.split('_'))
    # course = course.replace("_", " ")

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

# https://github.com/k1lgor/SoftUni/blob/6991b5dabfee5907be18d6583452b8af07dcf5dc/Python%20Fundamentals/Dictionaries/Lab/students.py

# this is another really good way to do items
# as the students with common id and name 
# are stored under one key
# DICT = {"Math": {"123": "Alice", "456": "Bob"}, "Science": {"789": "Charlie"}}
