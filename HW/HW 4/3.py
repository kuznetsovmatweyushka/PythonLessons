# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [1, 2, 3, 4, 5]

from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]
my_lst = create_list(10, 1, 20)
new_lst = []
[new_lst.append(i) for i in my_lst if i not in new_lst]
print(my_lst)
print(new_lst)