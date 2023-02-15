# pеализуйте алгоритм перемешивания списка.


#import random
listA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
print (listA)
listB = []

def listRandom(list):
    timer = 75 # счетчик количества перемешиваний
    length = len(list)
    element1 = None
    element2 = None
    while (timer != 0):        
        
        if (length % 2 == 0): 
            
            for i in range (0, length, 2):
                element1 = list[i]
                element2 = list[i + 1]
                list[i + 1] = element1
                list[i] = element2

            for i in range(1, length - 1, 2):
                element1 = list[i]
                element2 = list[i + 1]
                list[i + 1] = element1
                list[i] = element2
        else:
            
            for i in range (0, length - 1, 2):
                element1 = list[i]
                element2 = list[i + 1]
                list[i + 1] = element1
                list[i] = element2

            for i in range(1, length, 2):
                element1 = list[i]
                element2 = list[i + 1]
                list[i + 1] = element1
                list[i] = element2
        
        timer -= 1

listB = listA
listRandom(listB)
#random.shuffle(listA)
print (listB)