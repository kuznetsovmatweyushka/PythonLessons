# 3.Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

n = int(input('Введите количество чисел в последовательности: '))

lst = [round((1+1/k)**k,2) for k in range(1,n+1)]
print(f'Ваша последовательность: {lst}')
sum = 0
for i in range(len(lst)):
    sum += lst[i]
print(f'Сумма последовательности : {round(sum,2)}')