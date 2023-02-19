#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

user_number = int(input("Введите ваше число: "))
#user_number += 1
first_number = int(0)
second_number = int(1)
fibonachi_list_p = [first_number, second_number]
fibonachi_list_m = [first_number, second_number]
variable = int(0)

for i in range (0, user_number - 1, 1):
    variable = int (fibonachi_list_m[i]) - int(fibonachi_list_m[i + 1])
    fibonachi_list_m.append(variable)

for i in range (0, user_number + 1, 1):
    variable = int(fibonachi_list_p[i]) + int(fibonachi_list_p[i + 1])
    fibonachi_list_p.append(variable) 

fibonachi_list_m.reverse()

for i in range (0, user_number, 1):
    print(fibonachi_list_m[i], end = ' ')
    
for i in range (0, user_number + 1, 1):
    print(fibonachi_list_p[i], end = ' ')
    
    
    