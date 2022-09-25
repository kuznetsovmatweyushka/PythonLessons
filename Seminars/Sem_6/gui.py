def add_contact():
    name = input('Введите имя контакта: ')
    about = input('Введите описание контакта: ')
    number = input('Введите номер контакта: ')
    col = name + ', ' + about + ', ' + number + ';'
    return col

def find_contact():
    name = input('Введите имя контакта: ')
    return name

def action():
    act = input('Введите действие: ')
    return act

def path_file():
    path = input('Введите путь: ')
    return path

def help():
    print('Справочник работает с ".txt" форматом. Для работы укажите путь к файлу и выберете действие: \n \
        "/r" - чтение \n \
            "/w" - запись \n \
                "/f" - поиск по справочнику \n \
                    "/d" - удаление из справочника')