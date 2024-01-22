import random
import pandas as pd
import numpy as np


def one_hot_encode(arr):
    # Определяем размерность нового массива
    rows = 20
    cols = 2
    #print(arr)
    print(rows,cols)

    # Создаем новый двумерный массив
    #matrix = [[0 for _ in 20] for _ in 2]
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Заполняем новый массив значениями из старого массива
    for i in range(rows):
        print(i, " : ", arr[i])
        if arr[i] == 'robot':
            matrix[i][0] = 1
        else:
            matrix[i][1] = 1
#        for j in range(cols):
#            if arr[i][j] == 'r':
#                matrix[i][j] = 1
#            elif:
#            else:
#                matrix[i][j] = 0

    # Возвращаем новый массив
    return matrix

# Пример использования функции
lst = ['robot']  *  10
lst += ['human']  *  10
random.shuffle(lst)
matrix = one_hot_encode(lst)
m2=pd.DataFrame(matrix, columns=['robot', 'human'])
print(m2)
