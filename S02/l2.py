lst_obj = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"},
]

my_set = set()

for elem in lst_obj:
    for val in elem.values():
        my_set.add(val)

print(my_set)
