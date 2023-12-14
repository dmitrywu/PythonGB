def quicksort(array):
    if len(array) < 2: #базис, условие, при котором рекурсия завершает работу
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater) # помните, что при рекурсии добавляется ещё предыдущее значение
    
#print(quicksort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))
print(quicksort([10, 5 ,2]))