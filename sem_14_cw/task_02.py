# Задание No2
# 📌 Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from string import ascii_letters


def filter_lower(text: str) -> str:
    """
    >>> filter_lower('hello world')
    'hello world'
    >>> filter_lower('Hello World')
    'hello world'
    >>> filter_lower('hello, world!')
    'hello world'
    >>> filter_lower('helloпривет worldмир')
    'hello world'
    >>> filter_lower('Hello! Привет,Worldмир!')
    'hello world'
    """
    return (''.join(char for char in text if char in ascii_letters or char == ' ')).lower()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
