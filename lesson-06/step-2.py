# Форматы данных

import pickle
import json
import csv

data = {
    'users': [
        {
            'id': 1,
            'name': 'Linus Torvalds',
            'skills': ('C', 'C++', 'Linux'),
            'is_developer': True,
        },
        {
            'id': 2,
            'name': 'Richard Stallman',
            'skills': ('C', 'C++', 'GNU'),
            'is_developer': True,
        },

    ]
}

# Pickle

with open('users.pickle', 'wb') as f:  # wb - запись в двоичном (бинарном) режиме
    pickle.dump(data, f)        # создание файла и запись в него

with open('users.pickle', 'rb') as f:
    readed_data = pickle.load(f)    # в pickle file нельзя ничего дописать, можно только полностью перезаписать
    print('PICKLE:{}'.format(readed_data))


# JSON - Java Script Object Notation

with open('users.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('users.json') as f: # режим чтения указывать не надо
    readed_data = json.load(f)      # в pickle и json используем только load
    print('JSON: {}'.format(readed_data))

# CSV

"""
Можно открывать в excel
Идентификаторы:
id;name;skills;is_developer # необязательный заголовок
1; Linus Torvalds; C++, C, Linux; 1
2; Richard Stallman; C, GNU; 1  # разделитель ; может быть любой
"""
# запись файла:

with open('users.csv', 'w') as f:
    users = data.get('users', [])
    #выбираем ключи из словарей
    fieldnames = users[0].keys()    # if empty list => Exceptions

    if users:
        fieldnames = users[0].keys()

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # записываем заголовок:
        writer.writeheader()


    # записываем данные в CSV:
        for user in users:
            writer.writerow(user)


# читаем файл:

with open('users.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print('CSV: {}'.format(row))

# INI (conf, cnf) формат
"""
конфигурационные файлы
нет однозначного формата как должны храниться данные в файлах
[db]
username = root
password = toor
"""

# XML -Extended Markup Language (старый, заменяется json)
# lxml - библеотека для использования, ставится через pip
"""
внутри используются тэги <   >:

<data>
    <users>
        <user>
        <id>1</id>
        <name>Linus Torvalds</name>
        <is_developer>1</is_developer>
        <skills>
            <skill>C++</skill>
            <skill>C</skill>
            <skill>Linux</skill>
        </user>
    </users>
</data>

Или по другому:

<user id="2" name="Richard Stallman"
"""


# Yaml (yml) => Ruby - как и в Python все на отступах
"""
service:
    nginx:
        target: ./Dockerfile.prod
"""
