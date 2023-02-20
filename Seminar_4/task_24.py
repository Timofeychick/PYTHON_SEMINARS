# задачка про кусты и чернику в фермерском хозяйстве Карелии :)
# кусты номер:            1     2     3     4     5     6     7     8     9     10  
berries_on_the_bushes = ['40', '42', '39', '53', '54', '89', '22', '19', '74', '76']


def threeBestBushes(list):
    sum_of_berries = int(0)
    max_sum_of_berries = int(0)
    number_of_bush = int(0)

    for i in range (1, len(list) - 1, 1):
        sum_of_berries = int(list[i - 1]) + int(list[i]) + int(list[i + 1])
        if (sum_of_berries > max_sum_of_berries):
            max_sum_of_berries = sum_of_berries
            number_of_bush = i + 1
            
    sum_of_berries = int(list[len(list) - 2]) + int(list[len(list) - 1]) + int(list[0])
    if (sum_of_berries > max_sum_of_berries):
            max_sum_of_berries = sum_of_berries
            number_of_bush = len(berries_on_the_bushes)
            
    sum_of_berries = int(list[len(list) - 1]) + int(list[0]) + int(list[1])
    if (sum_of_berries > max_sum_of_berries):
            max_sum_of_berries = sum_of_berries
            number_of_bush = 1
    
    return number_of_bush

the_best_bush_ever = threeBestBushes(berries_on_the_bushes)

print(f"Больше всего ягод соберём с куста № {the_best_bush_ever} и его соседей")