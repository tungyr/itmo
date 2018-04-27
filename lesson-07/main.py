import sqlite3
# 1. Подключение к БД

conn = sqlite3.connect('db.sqlite') #нужно всегда закрывать файлы самому

# 2. Создание объекта курсора
cursor = conn.cursor() # чз cursor все обращения к БД

# 3. Выполнить SQL запрос (обновление, создание таблицы - запрос)
sql = '''
CREATE TABLE IF NOT EXISTS shortener (
    id INTEGER PRYMARY KEY AUTOINCREMENT,             
    original_url TEXT NOT NULL,
    short_url TEXT NOT NULL DEFAULT '',
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
'''

conn.commit

# id - первичный ключ, идентификатор всегда 1 или больше;

# Как выполнить sql запрос?

cursor.execute(sql) 

# если программа не упала, значит все хорошо, запрос прошел

# запрос на вставку данных

sql = '''

    INSTER INTO shortener (original_url) VALUES (?)          
        
'''

# колонки, к-е хотим заполнить перечис - ся чз запятую, вместо ? вставляем ссылку
#Пример запроса на вставку:
 
cursor.execute(sql, ('http://profi.itmo.ru',))             
 
# запятая в конце если одно значение обязательна, принимает только кортеж

# запрос на выборку данных

sql = '''
    SELECT 
        id, original_url, short_url, created         
    FROM
        shortener                                   
    '''
    
# id, original_url, short_url, created - перечисляем поля откуда хотим выбрать

# shortener   - откуда выбираем
 
cursor.execute(sql)                                  

# execute ничего не возвращает

# 3.2. Если запрос на выборку данных (SELECT), то:

result = cursor.fetchall()
print(result)

# . Закрываем соединние с БД

conn.close()

# Контекстный менеджер!!!
"""
try:
    ...
finally:
    ...
"""

# Делает все описанное выше с начала файла (все запросы), но код короче:

with sqlite3.connect('db.sqlite') as conn:
    sql = 'SELECT * FROM shortener'
    cursor = conn.execute()
    print(cursor.fetchall())