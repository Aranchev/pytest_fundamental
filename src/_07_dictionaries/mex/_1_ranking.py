import sys

def checker(contest, user, points, dicto):
    if contest not in contest_points.keys():
        dicto[contest] = {user: int(points)}
    else:
        if user not in dicto[contest]:
            dicto[contest][user] = int(points)
        elif user in dicto[contest]:
            if points > dicto[contest][user]:
                dicto[contest][user] = points
    return dicto

"""
checkout the draft
"""

if __name__ == '__main__':
    inp = input().split(':')
    contest_passwords = {}
    contest_points = {}

    while 'end of contests' not in inp:
        contest_passwords[inp[0]] = inp[1]
        inp = input().split(':')

    inp2 = input().split('=>')

    while 'end of submissions' not in inp2:
        contest, user, points = inp2[0], inp2[2], int(inp2[3])
        if inp2[0] in contest_passwords.keys():
            if contest_passwords[inp2[0]] == inp2[1]:
                contest_points = checker(contest, user, points, contest_points)

        inp2 = input().split('=>')

    # from here on

    members = []

    for key, value in contest_points.items():
        for nested_key, nested_value in value.items():
            members += [nested_key]

    no_duplicates_members = set((members))

    points = {}

    for i in no_duplicates_members:
        for key, value in contest_points.items():
            for nested_key, nested_value in value.items():
                if i == nested_key:
                    if i not in points:
                        points[i] = int(nested_value)
                    else:
                        points[i] += int(nested_value)

    biggest = max(points, key=points.get)

    print(f"Best candidate is {biggest} with total {points[biggest]} points.")
    
    print('Ranking:')

    members_points = {}

    for i in sorted(no_duplicates_members):
        members_points[i] = {}

    for i in sorted(no_duplicates_members):
        for key, value in contest_points.items():
            for nested_key, nested_value in value.items():
                if i == nested_key:
                    members_points[i][key] = nested_value



    a = sys.maxsize

    b = sys.maxsize


    print(list(members_points)[0])

    while len(members_points) > 0:

        if a != b:

            print(list(members_points)[0])

        a = b
        for i in range(len(list(members_points)[0])):
            o = max(
                    members_points[list(members_points)[0]],
                    key=members_points[list(members_points)[0]].get
                )
            g = members_points[list(members_points)[0]][o]
            # ValueError: max() iterable argument is empty

            print(f'#  {o} -> {g}')


            del members_points[list(members_points)[0]][o]


            break

        if len(members_points[list(members_points)[0]]) < 1:
            del members_points[list(members_points)[0]]
            b -= 1


