"""
Задача №37. Решение в группах
15 минут
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""


def func_1(n):
    if n > 0:
        x = int(input("Введите число: "))
        func_1(n - 1)
        print(x, end=" ")


func_1(2)

orig = '3 4'

print()


def func_2(str_obj):
    res = ''
    for el in reversed(str_obj):
        res += el
    return res


print(func_2(orig))


def func_3(str_obj):
    if len(str_obj) == 1:
        return str_obj
    return str_obj[-1] + func_3(str_obj[:-1])


print(func_3(orig))
