def f(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / f(a, -b)
    else:
        return a * f(a, b - 1)

a = 3
b = 5
print(f(a, b))
result = f(a,b)
print(result)