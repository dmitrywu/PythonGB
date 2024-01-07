"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""


# решение 1 - через цикл
def is_prime_1(n):
    for el in range(3, n):
        if n % el == 0:
            return False
    return True


print(is_prime_1(2))


# решение 2 - через рекурсию
def is_prime_2(n, el=3):
    if el < n:
        if n % el == 0:
            return False
        return is_prime_2(n, el + 1)
    return True


print(is_prime_2(2))
