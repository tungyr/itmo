# Классы и объекты

# В ООП код второстепенен, главное это объекты

# Тема лекции: Синтаксис языка Питон для ООП

# Класс - это ничто, просто шаблон.

# todo: Как как объявить/создаnm класс?

# Зачем нужен конструктор? (Нужен чтобы проинициализировать экземпляр)


'''  название класса с большой буквы, нужно описать что это за класс;
    пока что это только шаблон
    Свойства - это просто переменные на основе класса
    Свойства/атрибуты/данные - члены/ данные
    В свойствах храним данные объекта
    Методы - поведение объекта, обычная функция
    '''

class Person(object):   # создали новый тип данных Person

    #__slots__ = ('__firstname', '__lastname')
    # :выйдет ошибка, если будут задаваться имена отличные от '__firstname', '__lastname', как на строчке 50
    def __init__(self, firstname, lastname): # __init__ - конструктор,
    # self -ссылка на текущий экземпляр; конструктор м/б только один
        self.__firstname = firstname # лучше свойства (self.firstname) и аргументы (firstname) называть одинаково
        self.__lastname = lastname  # присвоили св-во firstname

    def get_full_name(self):
        return '{} {}'.format(self.get_firstname, self.get_lastname)


# Для работы со свойствами всегда пользоваться методами:

def get_firstname(self):
    """Метод получатель, getter"""
    return self.__firstname


def get_lastname(self):
    return self.__laststname

#def set_firstname(self, firstname):
#    """Метод установщик, setter"""
#    self.firstname = firstname


linus.firstname = 'dlsjaf'   # добавится новое св-во, так делать нельзя
print(linus.__dict__)

# todo: Как создать обьект/экземпляр?

linus = Person('Linus', 'Torvalds')    # создается объект на основе класса Person
# linus.firstname = 'Linus' # присвоили св-во firstname
# linus.lastname = 'Torvalds'
# print(linus.firstname, linus.lastname)  # чтение св-ва
print(linus.get_full_name())    # get_full_name() не принимает аргументов, мы вызываем метод объекта

stallman = Person('Richard', 'Stallman')  # 'Richard', 'Stallman' автоматом отправляется в __init__
# print(stallman.firstname, stallman.lastname)
print(stallman.get_full_name())


# print(Person, linus)
# print(type(Person), type(linus))
