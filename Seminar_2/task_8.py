# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

user_number = int(input('Введите ваше число N: '))

number = 1
while (number < user_number):
    number *= 2
    if (user_number < number):
        print('')
    else:
        print(number, end = " ")
    