# list() function is used to convert an iterable (such as a string, tuple or dictionary) into a list

# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

def da(a):
    b = list(map(float, a.split())) 
    c = []
    for i in b:
        c += [abs(i)]
    return c



if __name__ == '__main__':
    a = input()
    b = da(a)
    print(b)
