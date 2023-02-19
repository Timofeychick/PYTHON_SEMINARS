# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

listA = ['4', '8', '3', '4', '3', '2', '9', '5', '4', '7', '8', '9', '6', '2', '3', '3', '4', '7', '4', '7', '9', '6', '5']

def multPairsOfElements(list):  
    listB = list
    pairs_counter = int(0)
    
    if (len(listA) % 2 == 0):
        length = int(len(listA) / 2)
        
    else:
        length = int((len(listA) - 1) / 2)
        
    for i in range (0, length, 1):
        first_element = int(listA[i])
        second_element = int(listA[len(listA) - 1 - i])
        multiple_result = first_element * second_element
        listB[i] = multiple_result
        pairs_counter += 1
        
    listC = listB[:pairs_counter]  
    
    return listC

def output(list): 
    print(f"Попарное произведение пар чисел из списка равна: {list}")


result_list = multPairsOfElements(listA)

output(result_list)