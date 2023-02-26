# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.


number = int(input("Введите ваше число: ")) 
grade = int (input("В какую стпень возвести ваше число: "))

def exponentiation(num , grd):
    
    if grd == 1:
        return num
    return num * exponentiation(num, grd - 1)


print(exponentiation(number, grade))