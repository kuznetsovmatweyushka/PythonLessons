# import os
# import time
# import zipfile
# # 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
# source = ['"C:\\Users\\ukeuk\\Desktop\\5.py"']
# # Заметьте, что для имён, содержащих пробелы, необходимо использовать
# # двойные кавычки внутри строки.
# # 2. Резервные копии должны храниться в основном каталоге резерва.
# target_dir = 'C:\\Users\\ukeuk\\Desktop\\' # Подставьте ваш путь.
# # 3. Файлы помещаются в zip-архив.
# # 4. Именем для zip-архива служит текущая дата и время.
# today = target_dir + os.sep + time.strftime('%d.%m.%Y') + '.zip'
# # 5. Используем команду "zip" для помещения файлов в zip-архив
# now = time.strftime('%H%M%S')
# # Создаём каталог, если его ещё нет
# if not os.path.exists(today):
#     os.mkdir(today) # создание каталога
#     print('Каталог успешно создан', today)
# # Имя zip-файла
# target = today + os.sep + now + '.zip'


# zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
# # Запускаем создание резервной копии
# if os.system(zip_command) == 0:
#     print('Резервная копия успешно создана в', target)
# else:
#     print('Создание резервной копии НЕ УДАЛОСЬ')


# def compare_files(path_file_1, path_file_2):
#     """ Функция сравнивает размеры двух файлов. Эта функция принимает на вход
#     пути к двум файлам. Возвращает True,  если файлы одинакового размера.
#     False, если файлы отличаются по размеру. """
#     size_file_1 = os.path.getsize(path_file_1)
#     size_file_2 = os.path.getsize(path_file_2)
#     if size_file_1 == size_file_2:
#         return True
#     else:
#         return False

# for dirs, folder, files in os.walk(source):
#         """ Пройтись по всем файлам в папке """
#         print(dirs)
#         print(folder)
#         print(files)


import os
import zipfile
import time
from pathlib import Path



source = Path(os.getcwd())
copy_path = 'C:\\Users\\ukeuk\Desktop\\' + time.strftime('%d.%m') + '\\'
# files = []
# for all_path in source.rglob("*"):
#         files.append(all_path)
# files = list(map(str,files))

# тоже самое что и выше

files = list(map(str,[file for file in source.rglob("*")]))

files = [i.rpartition("HW 4\\")[-1] for i in files]

if not os.path.exists(copy_path):
        os.mkdir(copy_path)
        print('Каталог создан: ', copy_path)

for file in files:
        with zipfile.ZipFile(copy_path + time.strftime('%d.%m') + '.zip', mode='a', \
                                compression=zipfile.ZIP_DEFLATED) as zf:
                zf.write(file)
print('КОПИЯ СОЗДАНА УСПЕШНО',copy_path)



