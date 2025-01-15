if __name__ == '__main__':
    a = input().split('|')
    b = 100 # initial health
    c = 0  # bitcoin
    d = [x.split() for x in a]
    o = 0
    
    for i in d:
        o += 1
        if i[0] == 'potion': 

            if b + int(i[1]) < 100:
                b += int(i[1])
                print(f'You healed for {int(i[1])} hp.')
            else:
                print(f'You healed for {100 - b} hp.')

                b = 100
            print(f'Current health: {b} hp.')

        elif i[0] == 'chest':
            try:
                c += int(i[1])
                print(f'You found {i[1]} bitcoins.')
            except IndexError:
                pass
        else:
            if b - int(i[1]) > 0:
                b -= int(i[1])
                print(f'You slayed {i[0]}.')
            else:
                b -= int(i[1])
                print(f'You died! Killed by {i[0]}.')
                print(f'Best room: {o}')
                break
    if b > 0:
        print(f"You've made it!")
        print(f'Bitcoins: {c}')
        print(f'Health: {b}')
