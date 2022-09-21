# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n: int) -> int:
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def negative_fib(k: int) -> list:

    # обычный ряд Фибоначчи

    list = []
    list.append(0)
    list = [fib(e) for e in range(1, k + 1)]

    # копируем обычный ряд и умножаем все элементы на -1

    negative_list = list[1:]
    for i in range(len(negative_list)):
        negative_list[i] *= -1
        
    # добавляем в новый список положительный и отрицательный ряд
    
    negative_fib_list = [negative_list[i] for i in range(len(negative_list))]

    for j in range(len(list)):
        negative_fib_list.append(list[j])

    # сортируем полученный список

    negative_fib_list.sort()

    # перемножаем на (-1) каждый нечетный элемент 
    
    if k % 2 != 0:    
        for i in range(0,len(negative_fib_list) // 2, 2):
            if negative_fib_list[i] == 0:
                break
            negative_fib_list[i] *= -1
            
    else:
        for i in range(1,len(negative_fib_list) // 2, 2):
            negative_fib_list[i] *= -1
            if negative_fib_list[i] == 0:
                break

    return negative_fib_list

k = int(input('Введите число: '))
print(negative_fib(k))