# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_uneven_index(my_list: list) -> int:
    sum = 0
    for i in range(len(my_list)):
        sum = sum + my_list[i] 
    return sum
my_list = list(enumerate(range(10)))
print(f'Ваш список: {my_list}')
my_uneven_list = [my_list[i][1] for i in range(len(my_list)) if my_list[i][0] % 2 != 0]
print(f'Элементы на нечетных позициях: {my_uneven_list}')
print(f'Сумма элементов на нечетных позициях: {sum_uneven_index(my_uneven_list)}')