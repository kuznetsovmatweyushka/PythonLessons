# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from itertools import groupby

txt = input('Введите текст: ')
def coding(text: str):
    res = ''
    for i, j in groupby(txt):
        x = list(j)
        res = res + str(len(x)) + x[0]
    return res
    
def decoding(code_txt: str):
    res = ''
    lst = [*code_txt]
    lst2 = [lst[i] for i in range(len(lst)) if i % 2 !=0]
    lst3 = [lst[i] for i in range(len(lst)) if i % 2 ==0]
    for i in range(len(lst) // 2):
        res += int(lst3[i]) * lst2[i]
    return res

print(f"Текст после сжатия: {coding(txt)}")
print(f"Текст после восстановления: {decoding(coding(txt))}")