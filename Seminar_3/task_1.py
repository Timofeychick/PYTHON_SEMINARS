# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

listA = ['32', '80', '20', '14', '43', '21', '9', '15', '42', '76', '83', '59', '56', '72', '39', '35', '54', '78', '43', '66']

result = int(0) 

def elementSum (list):
      
    length = len(list)
    sum_from_list = int(0)
    current_element = int(0) 

    if (length % 2 == 0):
        for i in range (1, length, 2):
            current_element = int(list[i])
            sum_from_list += current_element
    else:
        for i in range (1, length - 1, 2):
            current_element = int(list[i])
            sum_from_list += current_element
    return sum_from_list
     

def output(a):
    
    print(f"Сумма чисел из списка, стоящих на нечетной позиции равна: {a}")
    

result = elementSum(listA)

output(result)