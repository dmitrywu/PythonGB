# def find_farthest_orbit():


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# print(max(orbits))
new_orbits = []
# for item in orbits:
#     if item[0] != item[1]:
#         new_orbits.append(item)
#print(new_orbits)
#print(max(new_orbits, key=lambda x: 3.14 * x[0] * x[1]))
print(max([item for item in orbits if item[0] != item[1]], key=lambda x: 3.14 * x[0] * x[1]))
