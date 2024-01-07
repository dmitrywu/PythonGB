"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

# решение 1 - встроенные функции
lst = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(lst)))

# решение 2 - традиционный итератор с ф-цией append
lst = [1, 1, 2, 0, -1, 3, 4, 4]
count_unic = []
for el in lst:
    if el not in count_unic:
        count_unic.append(el)
print(len(count_unic))
