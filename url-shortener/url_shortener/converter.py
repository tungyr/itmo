from string import ascii_letters, digits # импортируем буквы Aa-Zz и цифры

valid_values = list(digits + ascii_letters)
radix = len (valid_values) # основание системы


def convert(number):
    """Конвертирует из 10 в нашу"""
    result = []

    while number:
        result.insert(0, valid_values[number % radix]) # [] -допустимые значения в valid_values
        number //= radix # получаем целую часть

    return ''.join(result)


def inverse(number):
    """Переводит из нашей СС в 10"""
    result = 0

    for p, i in enumerate(reversed(number)): # переворачиваем строчку,
    #enumerate - пронумерование, p - степень, принимает значение i
        n = valid_values.index(i) # поиск индекса элемента
        result += n * radix ** p

    return result
