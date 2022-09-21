# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def read_file(path : str) -> list:
    f = open(path, 'r', encoding='utf-8')
    data = f.read()
    f.close()
    data = list(map(str,data.split(' ')))
    return data
def redact(text: list) -> str:
    text = [i for i in text if 'абв' not in i]
    return ' '.join(text)
def write_in_file(text : str):
    new_file = open('C:\\Users\\ukeuk\\Desktop\\Учеба\\Знакомство с Python\\Seminars\\Sem 4\\3\\new_text.txt', 'w', encoding='utf-8')
    new_file.write(text)
    new_file.close()

file_path = "C:\\Users\\ukeuk\\Desktop\\Учеба\\Знакомство с Python\\Seminars\\Sem 4\\3\\text.txt"
print(f'Текст отредактирован! Путь к файлу {file_path}',write_in_file(redact(read_file(file_path))))