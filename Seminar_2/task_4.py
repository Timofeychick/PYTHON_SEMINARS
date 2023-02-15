# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

user_number = int(input('Введите ваше число N: '))

result = 0
result = int(result)
number = -user_number

for i in range (-user_number, user_number + 1):
    result = number * number * (-1)
    print(number, ' -N * N = ',result)
    number += 1
    
