# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

listA = ['4.93', '8.23', '3.48', '4.23', '3.23', '2.42', '9.86', '5.45', '4.39', '7.54', '8.86', '9.3', '6.09', '2.07', '3.43', '3.56', '4.4', '7.1', '4.28', '7.7', '9.29', '6.78', '5.34']


def differenceMaxMin (list):
    max_fraction_part = int(0)
    min_fraction_part = int(1)
    for i in range (0, len(list), 1):
        current_element = float(list[i])
        fraction_part = round(current_element - int(current_element), 2)
        if (fraction_part > max_fraction_part): max_fraction_part = fraction_part

        else:
            if (min_fraction_part > fraction_part): min_fraction_part = fraction_part
                
    result = round(max_fraction_part - min_fraction_part, 2)
    print(fraction_part)
    return result, max_fraction_part, min_fraction_part

result, max_, min_ = differenceMaxMin(listA)

print(f"Максимальное значение дробной части: {max_}, минимальное: {min_}, разность: {result}")