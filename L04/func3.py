def calc1(a, b):
    return a + b


def calc2(a, b):
    return a * b


def math(op, x, y):
    print(op(x, y))


calc3 = lambda a, b: a + b
math(calc1, 5, 45)
math(calc3, 5, 45)
math(lambda a, b: a + b, 5, 45)

# def f(x):
#     return x*x

# a=f
# print(f(5))
# print(type(f), type(a))
# print(a(5))
