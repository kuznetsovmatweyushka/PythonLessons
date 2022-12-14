# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*

# 2+2 => 4;

# 1+2*3 => 7;

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

# *Пример:*

# 1+2*3 => 7;

# (1+2)*3 => 9;


# s = '(1 + 2) * 3'
# print(eval(s))


# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:*

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

def get_unic(my_list):
    unic = [my_list[i] for i in range(len(my_list)) \
            if my_list[i] not in my_list[i+1:] and my_list[i] not in my_list[:i-1] ]
    return unic

print(get_unic(my_list))