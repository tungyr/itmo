# Декораторы

import time
from urllib.request import urlopen  # для открытия url


def page(url):  # работает на замыкании
    def get():
        return urlopen(url).read()
    return get


python = page('http://python.org')
print(python)  # передалось в память, но ничего не загружается
print(python())  # произойдет переход на сайт http://python.org


def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

# как замерить производительность этой ф-ии:


def benchmark(func, *args, **kwargs):
    # тестирует любые ф-ии; *args, **kwargs - любое кол-во аргументов
    started = time.time()
    result = func(*args, **kwargs)
    worked = time.time() - started
    print('Функция  "{}" выполнилась за {:f} микросекунд'.format(
        func.__name__, worked * 1e6
    ))  # worked * 1e6 - перевод сек в милисек
    return result


print(benchmark(factorial, 5))
print(benchmark(python))
