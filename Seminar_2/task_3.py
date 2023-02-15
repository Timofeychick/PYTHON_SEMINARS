# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Введите ваше число: '))

variable = 3
one = 1
current_number = 0

for i in range (1, number + 1):
    current_number = one + i * variable
    print(current_number, end = ', ')
    
    