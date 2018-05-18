# Декораторы

from datetime import datetime
from functools import reduce, wraps
import pickle
import time

# todo: Простой декоратор. Как применить и где использовать?
# Декоратор - функция - обертка для другой ф-ии


def benchmark(func):
    # функция - обертка, всегда принимает только один аргумент - ссылку на оборачиваемую ф-ию, вызывает python
    @wraps(func)  # копирует аргументы из оригинальной ф-ии
    def wrapper(*args, **kwargs):
        # *args, **kwargs - аргументы оборачиваемой ф-ии, использовать всегда
        started = time.time()   # мы должны вызвать оригинальную ф-ию
        result = func(*args, **kwargs)  # вызываем func только один раз!
        worked = time.time() - started
        print('Функция  "{}" выполнилась за {:f} микросекунд'.format(
            func.__name__, worked * 1e6
        ))
        return result
    return wrapper

# Второй декоратор - декоратор кэш:


def cache(func):
    memory = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        # wrapper д-н всегда вернуть рез-т работы ориг-ой ф-ии
        key = pickle.dumps((args, sorted(kwargs.items())))

        if key not in memory:
            memory[key] = func(*args, **kwargs)

        return memory[key]
    return wrapper

# @cache
# @benchmark
@benchmark  # применеие декоратора
# @benchmark - не работает
@cache  # если 2 декоратора, то выодится wrapper, вызов происх-т сверху вниз, а выполнение снизу вверх
def factorial(n):
    return reduce(lambda f, i: f * i, range(1, n + 1)) # reduce аккумулятор для значений факториала, рез-тат б-т в f
# чем проще код, тем он быстрее работает

print(factorial(5))
print(factorial(30))


# todo: Декоратор с параметрами


"""
Общий шаблон декоратора:
def decorator_parameters(param1, ...., paramN):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            do something
            return func(*args, **kwargs)
        return wrapper
    return decorator
"""


def log(filename):
    template = '''
[{now:%Y-%m-%d %H-%M-%S}] Function: "{func}" called with:
    -> positional arguments: {args}
    -> keyword arguments:    {kwargs}
Returns: {result}
    '''

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            with open(filename, 'a') as f:
                f.write(template.format(now=datetime.now(),
                                        func='.'.join((func.__module__, func.__name__)),
                                        args=args,
                                        kwargs=kwargs,
                                        result=result))

            return result
        return wrapper
    return decorator


@log('log.txt')
def tst_func(a, b):
    return a + b


tst_func(2, 2)
tst_func(8, 10)
