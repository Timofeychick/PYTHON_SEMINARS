# задачка про монетки
listA = ['1', '1', '0', '1', '0', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1', '0', '0', '1', '0', '1']
# listB = ['101010101']

output = 0

def coinCounter(list):
    length = len(list)
    element = None
    counter0 = 0
    counter1 = 0
    result = 0
    for i in range (0, length, 1):
        element = list[i]
        number = int(element)
        if (number == 0):
            counter0 += 1
        else:
            counter1 += 1
    
    if (counter0 > counter1):
        result = counter1
    else:
        result = counter0
        
    return result
    
output = coinCounter(listA)    

print(f"нужно перевернуть {output}, монет")
    
