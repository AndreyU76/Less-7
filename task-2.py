#Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#заданный случайными числами на промежутке [0; 50).
#Выведите на экран исходный и отсортированный массивы.

import random

def Sort(list):
    #print(list)
    #print("Разьединение ",list)
    if len(list)>1:
        midl = len(list)//2
        left = list[:midl]
        right = list[midl:]

        Sort(left)
        Sort(right)

        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
            k=k+1

        while i<len(left):
            list[k]=left[i]
            i=i+1
            k=k+1

        while j<len(right):
            list[k]=right[j]
            j=j+1
            k=k+1
    #print("Объединение ",list)

list = [random.randrange(0, 50) for i in range(15)]
print(list)
Sort(list)
print(list)
