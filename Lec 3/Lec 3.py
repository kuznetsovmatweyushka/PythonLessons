# Анонимные, lambda функции

# def f(x):
#     return x ** 2

# g = f

# print(type(g))
# print(type(f))

# print(f(4))
# print(g(4))

# def calc1(x):
#     return x + 10

# #print(calc1(10))

# def calc2(x):
#     return x * 10

# #print(calc2(10))

# def math(op,x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)


# def sum(x, y):
#     return x + y

# sum = lambda x, y: x + y + 1 # то же самое, что и функция выше

# def mult(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))
#     #return op(a, b)

# calc(sum, 4, 5)

# LIST COMPREHENSION

# list = []

# for i in range(1, 101):
#     #if(i % 2 == 0):
#     list.append(i)

# print(list)

# Тоже самое что и выше

# cube = lambda x : x**3
# list = [(i,cube(i)) for i in range(1, 20) if i % 2 == 0]
# print(list)

# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# f = open('task.txt', 'r')
# data = f.read()
# f.close()

# data = data.split(' ')
# data = list(map(int, data))
# numbers = [i for i in data if i % 2 == 0]
# square = lambda x : x ** 2
# numbers_square = [(i,square(i)) for i in numbers]
# print(numbers_square)

#РЕШЕНИЕ ЛЕКТОРА


# data = '1 2 3 5 8 15 23 38'.split()

# res = list(map(int, data))
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2) ,res))
# print(res)

# Функция map
# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.

# li = [x for x in range(1,10)]
# print(li)
# li = list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int,'1 2 3'.split()))

# for e in data:
#     print(e * 10)

# print('-----')


# for e in data:
#     print(e)

# Функция filter()
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.

# data = [x for x in range(11)]

# res = list(filter(lambda x: not x % 2, data))
# print(res)

#Функция zip()
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.

# user = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# data = list(zip(user,ids,salary))
# print(data)

#Функция enumerate()
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.

# user = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]

# data = list(enumerate(user))
# print(data)
