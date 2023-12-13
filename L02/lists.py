list_1 = [] # Создание пустого списка
list_2 = list() # Создание пустого списка
list_1 = [7, 9, 11, 13, 15, 17]
print(list_1[0]) # 7
print(list_1[-1]) # 17
print(list_1)
print(*list_1) #убираем квадратные скобки

#append
list_1.append(85) # add 85
print(*list_1)
print(len(list_1))

#pop - удаление элемента, по умолчанию - последнего
# print(list_1.pop())
# print(*list_1)
# print(len(list_1))
# print(list_1.pop())
# print(*list_1)
# print(len(list_1))

#или с определённым индексом
print(list_1.pop(2))
print(*list_1)
print(len(list_1))

#insert

print(list_1.insert(2,42))
print(*list_1)
print(len(list_1))

#срезы списка
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])
# 1
print(list_1[1])
# 2
print(list_1[len(list_1)-1])
# 10
print(list_1[-5])
# 6
print(list_1[:])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])
# [1, 2]
print(list_1[len(list_1)-2:])
#[9, 10]
print(list_1[2:9])
# [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])
# []
print(list_1[0:len(list_1):6])
# [1, 7]
print(list_1[::6])
# [1, 7