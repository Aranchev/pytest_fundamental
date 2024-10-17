# list comprehension, why the split in question returns the list in question, sorted(value, reverse=True/False)
def sort(a):
    b = [int(i) for i in a.split()]
    return sorted(b)

if __name__ == '__main__':
    a = input()
    print(sort(a))

