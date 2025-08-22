entry = input().split('-')
phonebook = {}

# or while not entry.isdigit():
while len(entry) > 1:
    
    # add entry
    if entry[0] not in phonebook:
        phonebook[entry[0]] = entry[1]

    # update
    if entry[0] in phonebook:
        phonebook[entry[0]] = entry[1]
    
    entry = input().split('-')

for i in range(int(entry[0])):
    check = input()
    if check not in phonebook.keys():
        print(f"Contact {check} does not exist.")
    else: print(f'{check} -> {phonebook[check]}')

