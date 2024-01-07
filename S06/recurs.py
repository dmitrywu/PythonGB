def f_2(i):
    if i < 0:
        return i
    print(i)
    return f_2(i-1)

#другой вариант
def f_3(i):
    if i < 0:
        return i
    print(i)
    f_3(i-1)


f_2(5)
f_3(6)
