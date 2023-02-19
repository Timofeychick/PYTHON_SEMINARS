# scrabble

user_word = list(input('Введите ваше слово (капсом): '))

one_point = ['A','E','I','O','U','L','N','S','T','R','А','В','Е','И','Н','О','Р','С','Т']
two_points = ['D','G','Д','К','Л','М','П','У']
three_points = ['B','M','P','Б','Г','Ё','Ь','Я']
four_points = ['F','H','V','W','Y','И','Ы']
five_points = ['K','Ж','З','Х','Ц','Ч']
eight_points = ['J','X','Ш','Э','Ю']
ten_points = ['Q','Z','Ф','Щ','Ъ']


user_list = []
variable = None
for i in range(len(user_word)):
    variable = user_word[i]
    user_list.append(variable)
    
first_letter = None
second_letter = None
points_counter = int(0)

print(user_list)

for i in range (len(user_list)):
    first_letter = user_list[i]
    for j in range (len(one_point)):
        second_letter = one_point[j]
        if (first_letter == second_letter): points_counter += 1
    for k in range (len(two_points)):
        second_letter = two_points[k]
        if (first_letter == second_letter): points_counter += 2
    for f in range (len(three_points)):
        second_letter = three_points[f]
        if (first_letter == second_letter): points_counter += 3
    for t in range (len(four_points)):
        second_letter = four_points[t]
        if (first_letter == second_letter): points_counter += 4
    for g in range (len(five_points)):
        second_letter = five_points[g]
        if (first_letter == second_letter): points_counter += 5
    for x in range (len(eight_points)):
        second_letter = eight_points[x]
        if (first_letter == second_letter): points_counter += 8
    for z in range (len(ten_points)):
        second_letter = ten_points[z]
        if (first_letter == second_letter): points_counter += 10
        
print(f"Вы заработали {points_counter} очков за свое слово!")
