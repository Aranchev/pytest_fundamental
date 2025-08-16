number_of_inputs = int(input())
dicto = {}

for i in range(number_of_inputs):
    word = input()
    if word not in dicto.keys():
        dicto[word] = []
    dicto[word] += [input()]

for i in dicto.items():
    print(f"{i[0]} - {', '.join(i[1])}")
