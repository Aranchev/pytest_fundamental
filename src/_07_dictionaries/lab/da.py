inp = input().split(':')
students = {}

while len(inp) > 1:
    students[inp[0]] = {}
    students[inp[0]][int(inp[1])] = inp[2]
    inp = input().split(':')

print(students)
