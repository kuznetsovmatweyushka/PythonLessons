# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# def random(a: int,b: int) -> list:
#     the_set = set()
#     list = []
#     for i in range(a,b):
#         the_set.add(str(i))
#     for e in the_set:
#         list.append(e)
#         # break
#     print(list)

# random(5, 10)

### ИЛИ

# import datetime 

# def get_rand():
#     return datetime.datetime.now().microsecond%100000

# n = get_rand()

# print(n)

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['efg23', '79234gefg', 'sdgs', 'g53']
# '2'
# ['efg23', '79234gefg']

# def find(list: list, finddigit: str) -> str:

#     for i in range(len(list)):
#         if finddigit in list[i]:
#             print(list[i])
# list = ['efg23', '79234gefg', 'sdgs', 'g53']
# finddigit = '2'

# find(list, finddigit)

# 3. Напишите программу, которая определит позицию второго вхождения
# строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# def findstr(my_list: list, find_string: str) -> int:
#     count = 0
#     for i in range(len(my_list)):
#         if find_string == my_list[i]:
#             count += 1
#             if count == 2:
#                 return i
#     return -1

# list_find = ["йцу", "фыв", "йцу", "ячс", "цук", "йцукен"]
# find_string = "йцу"

# print(findstr(list_find, find_string))
