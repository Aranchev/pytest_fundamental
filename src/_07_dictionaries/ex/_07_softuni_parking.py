inp = int(input())
dicto = {}

for i in range(inp):
    inp2 = input().split(' ')
    if inp2[0] == 'register':
        if inp2[1] not in dicto:
            dicto[inp2[1]] = inp2[2]
            print(f"{inp2[1]} registered {inp2[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {inp2[2]}")
    elif inp2[0] == 'unregister':
        if inp2[1] not in dicto:
            print(f"ERROR: user {inp2[1]} not found")
        else:
            dicto.pop(inp2[1])
            print(f"{inp2[1]} unregistered successfully")

for x, y in dicto.items():
    print(f"{x} => {y}")
