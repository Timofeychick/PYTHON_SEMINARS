# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


user_number = int(input('Введите ваше число: '))

convert_number = int(user_number)
counter = int(0)

while (user_number > 1):
    user_number /= 2
    counter += 1

binary_number = []
variable = int(1)

for i in range (0, counter, 1):
    if (convert_number % 2 == 0):
        variable = 0
        binary_number.append(variable) 
    else:
        variable = 1
        binary_number.append(variable) 
    convert_number //= 2

binary_number.reverse()

for i in range (0, counter, 1):
    print(binary_number[i], end = '')
