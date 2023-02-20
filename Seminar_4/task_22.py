#Задача 22:
#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

user_number_n = int(input("Введите размер первого множества (N): "))
user_number_m = int(input("Введите размер второго множества (M): "))

list_n = [] # первый набор (N)
list_m = [] # второй набор (M)
sort_list = [] # отсортированный набор элементов, встречающихся в обоих массивах
general_list = [] # итоговый набор отсортированных по порядку элементов без повторений

print('Введите ваши числа в набор N')

for i in range (0, user_number_n, 1): # заполнение первого набора
    variable_n = int(input())
    list_n.append(variable_n) 
    
print('Введите ваши числа в набор M')

for i in range (0, user_number_m, 1): # заполнение второго набора
    variable_m = int(input())
    list_m.append(variable_m) 

for i in range (0, user_number_n, 1): # заполнение массива sort_list элементами изначальных массивов
    for j in range(0, user_number_m, 1):
        element_n = int(list_n[i])
        element_m = int(list_m[j])
        if (element_n == element_m): 
            sort_list.append(element_n)
        
counter = int(0)
while (counter != (user_number_n * user_number_n) * 3): # сортировка элементов по возрастанию в массиве sort_list
    for i in range (0, len(sort_list) - 1, 1): 
        element_one = int(sort_list[i])
        element_two = int(sort_list[i + 1])
        if (element_one > element_two):
            sort_list[i] = element_two
            sort_list[i + 1] = element_one
            
    counter += 1

         
general_list.append(sort_list[0]) # первый (опорный) элемент итогового массива

for i in range (0, len(sort_list) - 1 , 1): # заполнение массива general_list элементами из массива sort_list без повторяющихся элементов
    element_one = int(sort_list[i])
    element_two = int(sort_list[i + 1])
    if (element_two != element_one):
        general_list.append(element_two)
            
print(general_list)