# while (i:=input('-> ')) != '2':
#     print('NO')
# else:
#     print('Good')

# 1. Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов.
    
#     *Пример:*

    
#     - Для N = 5: 1, -3, 9, -27, 81

# n = 5
# x = 1
# print(x, end= ", ")
# for i in range(n - 1):
#     x = x * (- 3)
#     print(x, end = ', ')

# ИЛИ

# user_number = int(input("Введите число: "))
# number = 1

# for i in range(1, user_number + 1):
#     if i != 1:
#         number *= -3
#     print(number, end = " ")




# 2. Для натурального n создать, состоящий из 
# элементов последовательности 3n + 1.
    
#     *Пример:*


#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = 6 
# i = 1 
# while i <= n:
#     print(f"{i}: {3 * i +1}")
#     i += 1

# ИЛИ

# user_number = int(input("Введите число: "))

# for i in range(1, user_number +1):
#     print(f"{i} : {3 * i + 1}")


# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# string = 'Я люблю питон'
# counter = string.count('лю')
# print(counter)

# СРЕЗЫ

# string_1 = "Я люблю питон!"
# string_find = "пи"
# count = 0
# for i in range(len(string_1)):
#     if string_1[i:i + len(string_find)] == string_find:
#         count += 1
# print(count)

# SPLIT

# str1 = input('Введите строку 1: ')
# str2 = input('Введите строку 2: ')

# print(len(str1.split(str2)) - 1)
