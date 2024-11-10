def sp_l(a):
    b = a.split(', ')
    c = sorted(b, key=lambda x: (-len(x), x))
    return c

if __name__ == '__main__':
    a = input()
    print(sp_l(a))

'''
Softuni:
strings = input().split(" ")
searched_palindrome = input()
palindromes = []
for word in strings:
    if word == "".join(reversed(word)):
        opalindromes.append(word)
print(f"{palindromes}")
print(f"Found palindrome{palindromes.count(searched_palindrome)} times")
'''
