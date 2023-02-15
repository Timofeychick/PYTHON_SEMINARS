# задачка про загадку чисел Пети для Кати

summ = int(input('Введите сумму ваших чисел: '))
mult = int(input('Введите произведение ваших чисел: '))

def findNumbers(x, y):
    diskr = x**2 - 4 * y
    if (diskr > 0):
        x1 = (x + diskr**0.5) / 2
        x2 = (x - diskr**0.5) / 2
        print (f" Ваши числа: {x1}, {x2}")
    elif (diskr == 0):
        x3 = x / 2
        print (f"Вы загадали, каким-то образом, одно число: {x3}")
    else:
        print('404')
        return 0
        

findNumbers(summ,mult)

