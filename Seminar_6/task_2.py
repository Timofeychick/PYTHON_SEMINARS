# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

minNumber = int(input('Минимальное значение = '))
maxNumber = int(input('Максимальное значение = '))

list = [random.randint(-10, 10) for i in range(20)]
print(list)

for i in range(len(list)):
    if minNumber <= list[i] <= maxNumber:
        print(f" Индекс элемента: {i}, позиция в списке: {i + 1} ")
        