"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0 = 0, a1 = 1,
ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""

# 1, 2, 3, 5, 8, 13, 21, ...

n = 7

# решение 1 - через цикл
fib1, fib2 = 0, 1

for _ in range(0, n):
    fib1, fib2 = fib2, fib1 + fib2
print(f"{n}-е число Фибоначчи равно {fib2}")


# решение 2 - через рекурсию
def fibo(n):
    if n < 3:
        return n
    return fibo(n - 1) + fibo(n - 2)


print(f"{n}-е число Фибоначчи равно {fibo(n)}")
