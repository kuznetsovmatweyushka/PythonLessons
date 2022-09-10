# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def max_minus_min(my_list: list) -> float:
    res = []
    for i in range(len(my_list)):
        res.append(round((my_list[i] - int(my_list[i])),3))
    return round((max(res) - min(res)),2)

my_list = [1.1, 1.2, 3.3, 10.02]
print(max_minus_min(my_list))
