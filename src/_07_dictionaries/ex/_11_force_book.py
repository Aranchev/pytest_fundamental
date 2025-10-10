def existance_checker(force_side, force_user, dicto):

    for x in dicto.values():
        if force_user in x:
            force_user = True
            break
    else:
        force_user = False

    for i in dicto.keys():
        if i == force_side:
            force_side = True
            break
    else:
        force_side = False

    return force_side, force_user

def ver(force, user, checker, dicto):

    if checker[1] == True:
        return dicto
    else: 
        if checker[0] == False:
            dicto[force] = [user]
            return dicto
        if checker[0] == True:
            dicto[force].append(user)
            return dicto

def arrow(force, user, checker, dicto):
    for z, x in dicto.items():
        if user in x:
            dicto[z].remove(user)
            return ver(force, user, existance_checker(force, user, dicto), dicto)
    return ver(force, user, existance_checker(force, user, dicto), dicto)




if __name__ == '__main__':

    inp = input()
    dicto = {}
    
    while 'Lumpawaroo' not in inp:
        if '|' in inp:
            b = inp.split(' | ')
            dicto = ver(b[0], b[1], existance_checker(b[0], b[1], dicto), dicto)

        elif '->' in inp:
            b = inp.split(' -> ')
            dicto = arrow(b[1], b[0], existance_checker(b[0], b[1], dicto), dicto)
            print(f"{b[0]} joins the {b[1]} side!")

        inp = input()

    for i in dicto.items():
        if len(i[1]) > 0:
            print(f"Side: {i[0]}, Members: {len(i[1])}")
            for x in i[1]:
                print(f"! {x}")


