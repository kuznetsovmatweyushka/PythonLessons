# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def sum_pair(my_list: list) -> list:  
    mult = lambda x: my_list[x] * my_list[len(my_list) - 1 - x]
    result_list =[mult(i) for i in range((len(my_list) + 1) // 2)]
    return result_list

my_list = [2, 3, 4, 5, 6]

print(sum_pair(my_list))