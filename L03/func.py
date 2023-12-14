def sum_numbers(n, y="Hello"): # y= аргумент по умолчанию
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += 1
    return summa
    
a = sum_numbers(5, "privet")
print(a)
