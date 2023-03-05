# не самый простой калькулятор с системой логирования

import math
from datetime import datetime

def addition (point):
    
    if(point == 1):
        num_one = float(input('\nПервое слагаемое: '))
        num_two = float(input('Второе слагаемое слагаемое: '))
        result = num_one + num_two
        print(f"\n{num_one} + {num_two} = {result}\n")
        direct = 1 
        
    if(point == 2):
        num_one, num_two = complex_input()
        result = num_one + num_two
        print(f"\n{num_one} + {num_two} = {result}\n")
        direct = 2
        
    with open('logic.txt', 'a', encoding='utf=8') as file:
        file.writelines(str(datetime.now()) + ': ' + str(num_one) + ' + ' + str(num_two) + ' = ' + str(result) + '\n')
    if direct == 1: main()
    if direct == 2: complex_numbers()
               
def subtraction(point):
    
    if(point == 1):
        num_one = float(input('\nПервое число: '))
        num_two = float(input('Вычитаемое: '))
        result = num_one - num_two
        print(f"\n{num_one} - {num_two} = {result}\n")
        direct = 1
        
    
    if(point == 2):
        num_one, num_two = complex_input()
        result = num_one + num_two
        print(f"\n{num_one} - {num_two} = {result}\n")
        direct = 2
        
    with open('logic.txt', 'a', encoding='utf=8') as file:
        file.writelines(str(datetime.now()) + ': ' + str(num_one) + ' - ' + str(num_two) + ' = ' + str(result) + '\n')
    
    if direct == 1: main()
    if direct == 2: complex_numbers()

def multiplication(point):
    
    if(point == 1): 
        num_one = float(input('\nПервое число: '))
        num_two = float(input('Множитель: '))
        result = num_one * num_two
        print(f"\n{num_one} * {num_two} = {result}\n")
        direct = 1
        
    if(point == 2):
        num_one, num_two = complex_input()
        result = num_one * num_two
        print(f"\n{num_one} * {num_two} = {result}\n")
        direct = 2 
        
    with open('logic.txt', 'a', encoding='utf=8') as file:
        file.writelines(str(datetime.now()) + ': ' + str(num_one) + ' * ' + str(num_two) + ' = ' + str(result) + '\n')
    
    if direct == 1: main()
    if direct == 2: complex_numbers()   

def devision(point):
    
    if(point == 1):
        num_one = float(input('\nДелимое: '))
        num_two = float(input('Делитель: '))
        result = num_one / num_two
        print(f"\n{num_one} / {num_two} = {result}\n")
        direct = 1

    if(point == 2):
        num_one, num_two = complex_input()
        result = num_one / num_two
        print(f"\n{num_one} / {num_two} = {result}\n")
        direct = 2 
    
    with open('logic.txt', 'a', encoding='utf=8') as file:
            file.writelines(str(datetime.now()) + ': ' + str(num_one) + ' / ' + str(num_two) + ' = ' + str(result) + '\n')
    
    if direct == 1: main()
    if direct == 2: complex_numbers()    
        
def exponentiation(point):
    
    if(point == 1):
        num_one = float(input('\nВаше число: '))
        num_two = float(input('Степень: '))
        result = num_one ** num_two 
        print(f"\n{num_one}^{num_two} = {result}\n")
        direct = 1
        
    if(point == 2):
        num_one, num_two = complex_input()
        result = num_one * num_two
        print(f"\n{num_one}^{num_two} = {result}\n")
        direct = 2
    
    with open('logic.txt', 'a', encoding='utf=8') as file:
        file.writelines(str(datetime.now()) + ': ' + str(num_one) + ' ^ ' + str(num_two) + ' = ' + str(result) + '\n')

    if direct == 1: main()
    if direct == 2: complex_numbers()
    
def taking_the_log():
    
    num_one = float(input('\nОснование логарифма: '))
    num_two = float(input('Ваше число: '))
    result = math.log(num_two, num_one)
    print(f"\nЛогарифм числа {num_two} по основанию {num_one} равен {result} \n")
    
    with open('logic.txt', 'a', encoding='utf=8') as file:
        file.writelines(str(datetime.now()) + ': логарифм числа ' + str(num_one) + ' по основанию ' + str(num_two) + ' равен ' + str(result) + '\n')
    
    main()
    
def taking_the_root():
    
    num_one = float(input('\nВаше число: '))
    num_two = float(input('Показатель корня: '))
    result = num_one ** (1 / num_two) 
    print(f"\n{num_one} ^(1 /{num_two}) = {result}\n")
    
    with open('logic.txt', 'a', encoding='utf=8') as file:
        file.writelines(str(datetime.now()) + ': корень числа ' + str(num_one) + ' с показателем ' + str(num_two) + ' равен ' + str(result) + '\n')
    
    main()
    
def complex_numbers():
    
    print('Комплексное число представляет собой сумму действительной и мнимой частей и имеет вид: a + ib\nДля работы нужно ввести два числа\nКомплексная часть может быть равна 0')
    print('Выберите действие:\n\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Возведение в степень\n6. Вернуться в главное меню\n')
    user_choice = int(input('Действие: '))
    if user_choice == 1 : addition(2)
    if user_choice == 2 : subtraction(2)
    if user_choice == 3 : multiplication(2)
    if user_choice == 4 : devision(2)
    if user_choice == 5 : exponentiation(2)
    if user_choice == 6 : main()
    if user_choice > 6: print('Нет такого действия, повторите'), complex_numbers()
    
def complex_input():
    
    print('Введите первое комплексное число:')
    one_valid = float(input('\nДействительная часть: '))
    one_image = float(input('Мнимая часть: '))
    print('Введите второе комлпексное число:')
    two_valid = float(input('\nДействительная часть: '))
    two_image = float(input('Мнимая часть: '))
    num_one = complex(one_valid, one_image)
    num_two = complex(two_valid, two_image)
    return num_one, num_two

def main():
    
    print('\nВыберите действие:\n \n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Взятие логарифма\n6. Возведение в степень\n7. Нахождение квадратного корня\n8. Работа с комплексными числами\n9. Выход из программы')
    user_choice = int(input('\nДействие №: '))
    if user_choice == 1 : addition(1)
    if user_choice == 2 : subtraction(1)
    if user_choice == 3 : multiplication(1)
    if user_choice == 4 : devision(1)
    if user_choice == 5 : taking_the_log()
    if user_choice == 6 : exponentiation(1)
    if user_choice == 7 : taking_the_root()
    if user_choice == 8 : complex_numbers()
    if user_choice == 9 : program_stop(3), 
    if user_choice > 9  : print('\nНекоректный ввод, повторите'), main()
        
def program_start():
    
    with open('logic.txt', 'a', encoding='utf=8') as file:
        file.writelines(str(datetime.now()) + ': старт работы программы\n')
    main()

def program_stop(point):
    
    while True:
        if (point == 3):
            print("\nРабота программы завершена\nДосвидания!\n")
            
            with open('logic.txt', 'a', encoding='utf=8') as file:
                file.writelines(str(datetime.now()) + ': работа программы была завершена\n')
        break
        
program_start()