# 0. Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# 6

# 1. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# a, b, c, d, e = 78, 55, 36, 90, 2
# max = a
# if a > max:
#     max = a
# if b > max:
#     max = b
# if c > max:
#     max = c
# if d > max:
#     max = d
# if e > max:
#     max = e
# print(max)


# 2. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# *Примеры:*

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# a = 5
# for i in range(-a, a + 1):
#     print(i, end = ' ')

# 3. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# x = float(input("Введите число: "))
# print(int(x * 10) % 10)

# или
# x = input("Введите число: ")
# print(int(x.split('.')[1][0]))

# 4. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30).

# a = int(input("Введите число: "))

# if ((a % 5 == 0) and (a % 10 == 0)) or ((a % 15 == 0) and (a % 30 != 0)):
#     print(f"Число {a} кратно 5, 10, 15, но не кратно 30 ")
# else: print(f"Число {a} не кратно 5, 10, 15, но не кратно 30, условие не выполняется. ")