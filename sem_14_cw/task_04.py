# Задание No4
# 📌 Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from string import ascii_letters

import pytest


def filter_lower(text: str) -> str:
    return (''.join(char for char in text if char in ascii_letters or char == ' ')).lower()


def test_no_change():
    assert filter_lower('hello world') == 'hello world', 'Произошли непредвиденные ошибки'


def test_lower():
    assert filter_lower('Hello World') == 'hello world', 'Ошибка преобразования к нижнему регистру'


def test_symbols():
    assert filter_lower('hello, world!') == 'hello world', 'Ошибка удаления знаков пунктуации'


def test_foreign_letters():
    assert filter_lower('helloпривет worldмир') == 'hello world', 'Ошибка удаления символов других языков'


def test_mixed():
    assert filter_lower('Hello! Привет,Worldмир!') == 'hello world', 'Какая-то ошибка'


if __name__ == '__main__':
    pytest.main(['-vv'])
