stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# #stroka = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'
#stroka = 'Пух'

def space(text):
    if ' ' in text:
        return True
    else: return False

def rhythm(str):
    str = str.lower().split()
    list = []
    for word in str:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        list.append(result)
    return len(list) == list.count(list[0])

if space(stroka) == False:
    print('Количество фраз должно быть больше одной!')
elif rhythm(stroka):
    print('Парам пам-пам')
else:
    print('Пам парам')


#if space(stroka) == False: print ('есть чё!')

# if 'Пух' in stroka: 
#     print('Количество фраз должно быть больше одной!')

# stroka = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'

# song = stroka
# volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
# parts = song.split()
# itog = list()
# for item in parts:
#     k = 0
#     for letter in item:
#         if letter in volwes:
#             k += 1
#     itog.append(k)
# if len(set(itog)) == 1:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')