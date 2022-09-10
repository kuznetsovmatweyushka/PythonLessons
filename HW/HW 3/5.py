# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, -1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n: int) -> int:
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def negative_fib(k : int) -> list:
    #обычный ряд Фибоначчи
    list = []
    list.append(0)
    for e in range(1, k + 1):
        list.append(fib(e))
    #копируем обычный ряд и умножаем все элементы на -1
    negative_list = list[1:]
    for i in range(len(negative_list)):
        negative_list[i] *= -1
    #добавляем в новый список положительный и отрицательный ряд
    negative_fib_list = []
    for i in range(len(negative_list)):
        negative_fib_list.append(negative_list[i])
    for j in range(len(list)):
        negative_fib_list.append(list[j])
    #сортируем итоговый список
    negative_fib_list.sort()
    return negative_fib_list

k = int(input('Введите число: '))
print(negative_fib(k))