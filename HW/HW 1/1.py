# 1.Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Введите день недели: '))
if day < 1 or day > 7:
    print('Такого дня нет!')
if 1 <= day < 6:
    print('No')
if 6 <= day <= 7:
    print('Yes')