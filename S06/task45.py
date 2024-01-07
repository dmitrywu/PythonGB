def my_sum(n):
    s = 0
    for elem in range(1, n // 2 + 1):
        # вот из-за этого весь код :)
        if n % elem == 0:
            s += elem
    return s


def func(k):
    lst = []
    for n in range(1, k + 1):
        if n not in lst:
            m = my_sum(n)
            if n == my_sum(m) and m != n:
                # кортеж
                lst.append(n)
                lst.append(m)
    return lst


print(func(1000))
