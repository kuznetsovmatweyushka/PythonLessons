# 2.Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите X(1 или 0): '))
y = int(input('Введите Y(1 или 0): ' ))
z = int(input('Введите Z(1 или 0): ' ))

if x == 1: x = True
elif x == 0: x = False 
if y == 1: y = True
elif y == 0: y = False
if z == 1: z = True
elif z == 0: z = False
    
left = not(x or y or z)
right = not x and not y and not z
print(f'Левая часть: {left}')
print(f'Правая часть: {right}')
if left == right:
    print('Выражение истинно!')