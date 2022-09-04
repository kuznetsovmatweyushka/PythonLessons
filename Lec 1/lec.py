# типы данный и переменные
# int, float, boolean, str, list, None
# s = 'qwerty'
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))

# print(s)  # вывод строки
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'.format(a, b, s))

# f = True
# print(f)

# списки

# list = [1, 2, 3 , 'hello']
# print(list)

# ввод и вывод данных

# print('Vvedita a')
# a = int(input())
# print('Vvedita b')
# b = int(input())
# print(a,' + ', b, ' = ' ,a + b)

# арифметические операции и сокращенные операции

# a = 1.3
# b = 3
# c = a // b
# d = round(a / b, 2)
# e = a % b
# f = round(a * b , 2)
# print(c)
# print(d)
# print(e)
# print(f)

# логические операции

# a = 1 < 4 and 5 > 2
# b = 1 < 2 or 2 < 4
# print(a)
# print(b)

# операторы if else

# a = int(input('a='))
# b = int(input('b='))
# if a > b:
#     print(a)
# else:
#     print(b)

# оператор while

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('пожалуй хватит )')
# print(inverted)

# цикл for

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

# работа со строками

# text = 'съешь еще этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #

# for c in text:
#  print(c)

# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# описание функций

# def f(x):
#     return x**2


# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return


# print(f(1))  # Целое
# print(f(2.3))  # 23
# print(f(28))  # None
# print(type(f(1)))  # str
# print(type(f(2.3)))  # int
# print(type(f(28)))  # NoneType
