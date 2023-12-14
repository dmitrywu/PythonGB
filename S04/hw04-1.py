var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

# Введите ваше решение ниже


mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]
myset_1 = set()
myset_2 = set()
list_1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
    myset_1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
    myset_2.add(i)
lok = myset_1 & myset_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')