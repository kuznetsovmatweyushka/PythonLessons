# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#    Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import randint

n = int(input('Введите количество элементво: '))
list = []
for i in range(n):
    list.append(randint(-n, n))
print(f'Список заполненный числами из промежутка от [-N, N]: {list}')
list_index = []
index = input('Введите индексы через пробел: ')
print(index)
for i in index:
    if i != ' ':
        list_index.append(int(list[int(i)]))
print(f'Числа из массива хранящиеся на введёных вами индексах: {list_index}')
sum = 0
for i in range(len(list_index)):
    sum += list_index[i]
print(sum)
