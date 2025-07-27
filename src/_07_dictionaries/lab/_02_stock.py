list = input().split()
dict = {}

for i in range(0, len(list), 2):
    key = list[i]
    value = list[i+1]
    dict.update({key: int(value)}) # same as `dict[key] = int(value)`

# it's interesting how key-value
# pairs are created and added
# to dict in 7 line
# you can also use 'thisdict.update({"color": "red"})'


print(dict)
