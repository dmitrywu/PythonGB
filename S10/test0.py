import random
import pandas as pd
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
#mas = [['й', 'ц', 'у'], ['к','е','н'], ['г', 'ш', 'щ']]
#datams = pd.DataFrame(mas)
data2 []
for i in lst:
    if lst(i) = robot:
        data2
print(data.head(n=20))
#print(lst)
#print(datams)
#print(data)
#dataout=pd.get_dummies(data['whoAmI'], dtype=int)
#print(dataout)
#d2=pd.DataFrame(random.sample(['robot', 'human']*10, 20) ,columns=['whoAmI'])
#print(d2)
#data['tmp'] = 1
#data.set_index([data.index, 'whoAmI'], inplace=True)
#data = data.unstack(level=-1, fill_value = 0).astype(int)
#data.columns = data.columns.droplevel()
#data.columns.name = Noneprint(data)