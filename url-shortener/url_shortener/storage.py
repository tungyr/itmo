import os.path as Path
import sqlite3

from .converter import convert, inverse

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

def dict_factory(cursor, row): # в row всегда попадает кортеж
    d = {}

    #print(row)
    #print(cursor.description)

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


#def connect (db_name=':memory:'):
def connect(db_name=None):
    """Выполняет подключение к БД"""
    if db_name is None:
        db_name = ':memory:'   # БД прямо в памяти

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory


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

        short_url = '{}/{}'.format(domain.rstrip('/'), convert(pk)) # форматирование строчек; {} - вставка данных: {domain}{pk} - приводится к строке

        # запрос на обновление таблицы
        conn.execute(SQL_UPDATE_SHORT_URL, (short_url, pk))

        return short_url


def find_url_by_origin(conn, origin_url):
    """Возвращает URL-адрес по оригинальному URL."""
    origin_url = origin_url.rstrip('/')

    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_ORIGINAL, (origin_url,))    # url, - запятая чтобы был кортеж
        return cursor.fetchone()


def find_url_by_short(conn, short_url):
    """Возвращает URL-адрес по короткому URL"""
    short_url = short_url.rsplit('/', 1).pop()   # режет от конца строки к началу, режет только первый слэш
    # pop удаляет элемент с конца строчки
    pk = inverse(short_url)
    return find_url_by_pk(conn,pk)

def find_url_by_pk(conn, pk):
    """Возвращает URL-адрес по первичному ключу"""
    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_PK, (pk,))
        return cursor.fetchone()

def find_all(conn):
    """Возвращает все URL-адреса из БД"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()
