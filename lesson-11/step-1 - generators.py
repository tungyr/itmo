# todo: Итераторы,


s = 'Linus Torvalds'
lst = [1, 2, 3, 4, 5]
d = {
     'name': 'Linus Torvalds',
     'age': 47,
     'is_developer': True,
}

"""
__iter__() => return Iterator
__next__() => Iterator
"""

it = iter(s)  # calls __iter__()
print(type(it))

it = iter(lst)
print(type(it))

it = iter((1, 2))
print(type(it))

it = iter(d)  # словарь итеррир-ся по ключам
print(type(it))

print(next(it))  # calls __next__()
print(next(it))
print(next(it))

def for_emitator(seq):
    it = iter(seq)

    while 1:
        try:
            i = next(it)
            print(i)
        except StopIteration:
            break

# for_emitator(s)
# for_emitator(lst)
# for_emitator(d)


# todo: Генераторы


def generator():
    print('Шаг №1')
    yield 1  # возвращает результат, останавливается пока не будет вызван next
    print('Шаг №2')
    yield 2
    print('Шаг №3')

gen = generator()
print(type(gen))

print(next(gen))  # генератор встал на паузу после yield
print(next(gen))  # генератор встал на паузу после yield
# print(next(gen))  # StopIteration

# Если в ф-ии нет return или yield - обычная ф-ия
# yield в отличии от return - только ставит ф-ию на паузу


# генератор обратного отсчета:

def countdown(n):
    print('Герератор стартовал!')
    while n:
        yield n # когда n = 0 - пауза до следующего вызова ф-ии или next
        n -= 1

# Подсказка для домашки про генерацию пароля: у генератора нет конца

for i in countdown(3):
    print('Значение счетчика: {}'.format(i))


# todo: Генераторы списков/словарей/множеств

"""
Общий вид генераторов
[expression for item1 in iterable1 if condition1
            for item1 in iterable1 if condition1
            .......
            for item1 in iterableN if conditionN]
"""

# todo: Генераторы списков:


numbers = [1, 1, 2, 2, 3, 3]

# squares = []
# for i in numbers:
#     squares.append(i * i)

squares = [i * i for i in numbers]
odd = [i for i in numbers if i % 2]

"""
Длинный пример:

points = []
for x in range(3):
    for y in range(3):
        points.append((x,y))
"""

point = [(x, y) for x in range(3) for y in range(3)]

print(squares)
print(odd)
print(point)

# todo: Генераторы множеств:

sett = set(numbers)  # явное приведение ко множеству
print(sett)
sett = {i for i in numbers}
print(sett)

# todo: Генераторы словарей:

keys = ['id', 'original_url', 'short_url']
values = [1, 'http://profi.itmo.ru', '/1']

# data = {k: v for k in keys for v in values}  - не работает, никогда не повторять
# data = {k: v for i, k in enumerate(keys)
#              for j, v in enumerate(values) if i ==j}
# print(data)

for k, v in zip(keys, values):
    print(k, v)

print(dict(iter(zip(keys, values))))

# print(data.items())
# не имеют ничего общего с генераторами, это просто словари и списки

print(dict([('k1', 1), ('k2', 2), ('k3', 3)]))

# todo: Генераторные выражения

squares = (i * i for i in numbers)
print(squares, type(squares), tuple(squares))

with open(__file__) as f:
    lines = (line.strip() for line in f)  # удаление знаков переноса
    todos = (s for s in lines if s.startswith('# todo:'))
print('Todos:', todos, list(todos))
# если вышли изгенератора, будет ошибка что файл уже не читается- менеджер коннекта закрылся
