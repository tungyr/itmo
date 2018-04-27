import os.path as Path
import sqlite3

SQL_INSERT_URL = 'INSERT INTO shortener (original_url) VALUES (?)'  # все что на капсе - константы
SQL_UPDATE_SHORT_URL = '''
    UPDATE shortener SET short_url=? WHERE id=? # set устанавливает значение в таблице
'''
SQL_SELECT_ALL ='''
    SELECT
        id, original_url, short_url, created
    FROM
        shortener
        '''
SQL_SELECT_URL_BY_ORIGINAL = SQL_SELECT_ALL + ' WHERE original_url=?'
SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'

#def connect (db_name=':memory:'):
def connect(db_name=None):
    """Выполняет подключение к БД"""
    if db_name is None:
        db_name = ':memory:'   # БД прямо в памяти

    conn = sqlite3.connect(db_name)
    # Магия!!!


    return conn

def initialize(conn):
    script_path = Path.join(Path.dirname(__file__), 'schema.sql')  # отбрасывает последний элемент в пути файла "storage.py"; join склеивает пути через разделитель
                                        # В винде в адресах ставится \\ для разделения

    with conn, open(script_path) as f:
        conn.executescript(f.read())
        
    
    
def add_url(conn, url, domain=''):
    """Добавляет URL-адрес в БД и возвращает короткий"""
    url = url.rstrip('/')       # отрезает / с правого (r) конца

    if not url:
        raise RuntimeError("URL can't be empty.")

    with conn:                                              # запуск контекстного менеджера
        found = find_url_by_origin(url, conn)               # проверка на наличие вводимого url - избежание дублирования
        if found:
            return found[2]                                 # [] - кортеж с данными short url
        
        cursor = conn.execute(SQL_INSERT_URL, (url,))

        pk = cursor.lastrowid                               # получение первичного ключа
        # Магия по сокращению!!!

        short_url = '{}/{}'.format(domain.rstrip('/'), pk) # форматирование строчек; {} - вставка данных: {domain}{pk} - приводится к строке

        # запрос на обновление таблицы
        conn.execute(SQL_UPDATE_SHORT_URL, (short_url, pk))

        return short_url


def find_url_by_origin(conn, origin_url):
    """Возвращает URL-адрес по оригинальному URL."""
    origin_url = origin_url.rstrip('/')

    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_ORIGINAL, (origin_url,))    # url, - запятая чтобы был кортеж
        return cursor.fetchone()
        
