import gui
import actions


def work():
    
    print('Это первая версия телефонного справочника. \n  \
         Для отображения всех возможностей введите "/help"')
    
    act = gui.action()
    if act == '/help':
        gui.help()
        act = gui.action()
        p = gui.path_file()
        match act:
            case '/r':
                actions.read_file(p)
            case '/w':
                actions.write_in_file(p)
            case '/f':
                actions.find_in_file(p)
            case '/d':
                actions.delete_in_file(p)

