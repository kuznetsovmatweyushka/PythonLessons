# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#    Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import randint

n = int(input('Введите количество элементво: '))
randomize = lambda n: randint(-n, n)
numbers = [randomize(i) for i in range(n)]
print(f'Список заполненный числами из промежутка от [-N, N]: {numbers}')
list_index = input('Введите индексы через пробел: ').split(' ')
print(f'Ваши индексы: {list_index}')
sum = 0
for i in range(len(list_index)):
    if int(list_index[int(i)]) >= n:
        print(f'Индекса {int(list_index[int(i)])} не существует!')
    else:
        sum += numbers[int(list_index[int(i)])]
print(f'Сумма элементво стоящих на этих индексах: {sum}')