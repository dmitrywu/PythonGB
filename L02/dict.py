d={}
d=dict()

d['q']='qwerty'
print(d)

d['w']='asdfgh'
print(d)

print(d['q'])
print(d['w'])

dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary)
# {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left'])
# ←
# типы ключей могут отличаться
print(dictionary['up'])
# ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary:
# for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →