# ['2-Walk the dog', '1-Drink coffee', '6-Dinner', '5-Work']
import sys

if __name__ == '__main__':

    note = [0] * 10
    command = input()

    while command != 'End':

        command = command.split('-')
        command1 = int(command[0]) - 1
        command2 = command[1]

        note.pop(command1)
        note.insert(command1, command2)

        command = input()

    note = [ele for ele in note if ele != 0]
    # while 0 in note:
    #     note.remove(0)
    print(note)

# The solution comes from k1lgor, which is i think just Softuni's solution


