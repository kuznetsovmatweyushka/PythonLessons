# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary_converter(n: int) -> str:
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b
n = 45
print(f'Binary number: {binary_converter(n)}')
