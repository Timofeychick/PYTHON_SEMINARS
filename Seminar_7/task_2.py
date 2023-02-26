# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows = 6, num_columns = 6):
    for i in range(1, num_rows + 1):
        matrix = []
        for j in range(1, num_columns + 1):
            matrix.append(str(operation(i, j)))
        print(''.join(f'{e:<4}' for e in matrix))
 
 
lines = int(input('Строк: '))
colums = int(input('Столбцов: '))
print_operation_table(lambda lines, colums: lines * colums, lines, colums)