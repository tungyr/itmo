import sys

from url_shortener import storage

get_connection = lambda: storage.connect('shortener.sqlite') # прячем название БД в анонимную ф-ию
# вызывает .connect с именем БД ('shortener.sqlite')

def action_add():
    """Добавить URL-адрес"""
    url = input ('\nВведите URL-адрес: ')

    with get_connection() as conn:              # менеджер коннекта с названием соединения conn
        short_url = storage.add_url(conn, url)  # в файл storage закидывает (add) 
        
def action_find():
    """Найти оригинальный URL-адрес"""

def action_find_all():
    """Вывести все URL-адреса"""

def action_show_menu():
    """Показать меню"""
    print('''
1. Добавить URL-адрес
2. Найти оригинальный URL-адрес
3. Вывести все URL-адреса
m. Показать меню
q. Выйти
''')

def action_exit():
    """Выйти"""
    sys.exit(0)      # завершает с 0-вым кодом - все хорошо


def main():
    with get_connection() as conn:
        storage.initialize(conn)
        
    action_show_menu()

    actions = {
        '1': action_add,
        '2': action_find,
        '3': action_find_all,
        'm': action_show_menu,
        'q': action_exit,
        }


    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)   # возвращает значение словаря по ключу, значение по умолчанию возвращает только если нет ключа словаря

        if action:
            action()                # проверка false/true значения в словаре
        else:
            print('Неизвестная команда')
            
