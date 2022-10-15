import gui
import actions
import json_actions


def work():
    gui.help()
    act = gui.action()
    p = gui.path_file()
    format = gui.format_file(p)
    if format == 'txt':
        match act:
            case '/r':
                actions.read_file(p)
            case '/w':
                actions.write_in_file(p)
            case '/f':
                actions.find_in_file(p)
            case '/d':
                actions.delete_in_file(p)
    elif format == 'json':
        match act:
            case '/r':
                print('Ваша телефонная книга: ')
                print(json_actions.read_json(p))
            case '/w':
                json_actions.write_json(p)
            case '/f':
                json_actions.find_json(p)
            case '/d':
                json_actions.delete_json(p)
            case '/add':
                p_2 = gui.path_file()
                json_actions.add_json(p, p_2)

