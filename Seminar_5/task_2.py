# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))

def summation(a, b):
    if b == 0:
        return a
    return summation(a + 1, b - 1)

print(summation(number_one, number_two))