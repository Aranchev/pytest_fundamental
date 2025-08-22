entry = input().lower().split()

materials = {'shards': 0, 'fragments': 0, 'motes': 0}

for x, y in enumerate(entry, 1):
    
    if x % 2 == 0:
        if y in materials.keys():
            materials[y] += int(entry[x-2])
        if y not in materials.keys():
            materials[y] = int(entry[x-2])
    if materials['shards'] >= 250:
        print(f"Shadowmourne obtained!")
        materials[y] -= 250
        break
    elif materials['fragments'] >= 250:
        print(f"Valanyr obtained!")
        materials[y] -= 250
        break
    elif materials['motes'] >= 250:
        materials[y] -= 250
        print('Dragonwrath obtained!')
        break

for key, value in materials.items():
    print(f"{key}: {value}")
