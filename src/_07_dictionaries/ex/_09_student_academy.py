dicto = {}

for i in range(int(input())):
    student = input()
    grade = float(input())
    if student not in dicto:
        dicto[student] = [grade]
    else:
        dicto[student] += [grade]

for i in dicto.items():
    if sum(i[1]) / len(i[1]) >= 4.5:
        print(f"{i[0]} -> {sum(i[1]) / len(i[1]):.2f}")
