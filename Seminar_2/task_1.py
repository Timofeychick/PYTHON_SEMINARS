#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#- 6782 -> 23
#- 0,56 -> 11

number = float(input('Введите ваше число: '))
sum = 0
variable = 0
sum = int(sum)


if (number < 0): 
    number *= -1
    
variable = number
variable = str(variable)

timer = len(variable) - 2

number = round(number, timer)

if (number > 1):
    while (number > 0):
        sum += number % 10
        number //= 10
        
else:  
    for i in range (0, timer):
        number *= 10
        
    number = int(number)
    
    while (number > 0):
        sum += number % 10
        number //= 10    
        
print(f"Сумма цифр числа равна: {sum}")