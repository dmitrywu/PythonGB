import random
import pandas as pd

lst = ['robot']  *  10
lst += ['human']  *  10
random.shuffle(lst)
rows = 20
cols = 2
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
for i in range(rows):      
    if lst[i] == 'robot':  
        matrix[i][0] = 1   
    else:                  
        matrix[i][1] = 1
print(pd.DataFrame(matrix, columns=['robot', 'human']))