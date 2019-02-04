# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
#[-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
#По возможности доработайте алгоритм (сделайте его умнее).

import random

def selection_sort(array):
    list = len(array) - 1
    for z in range(0, list):
        for i in range(0,list - z):
            #print(array)
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            
    

array = [random.randrange(-100, 100) for i in range(20)]
print(array)
selection_sort(array)    
print(array)
