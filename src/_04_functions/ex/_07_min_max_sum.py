#! This solution is exemplatory of multipline strings, list comprehension, and to remind myself on what exactly min(), max(), sum() works.

def find_min_max(a):
    numbers = [int(i) for i in a.split()]

    return f"""
The minimum number is {min(numbers)}
The maximum number is {max(numbers)}
The sum number is: {sum(numbers)}
"""

if __name__ == '__main__':
    a = input()
    print(find_min_max(a))
