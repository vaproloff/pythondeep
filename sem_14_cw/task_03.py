# Задание No3
# 📌 Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from string import ascii_letters
import unittest


class TestFilterLower(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual(filter_lower('hello world'),
                         'hello world')

    def test_lower(self):
        self.assertEqual(filter_lower('Hello World'),
                         'hello world')

    def test_symbols(self):
        self.assertEqual(filter_lower('hello, world!'),
                         'hello world')

    def test_foreign_letters(self):
        self.assertEqual(filter_lower('helloпривет worldмир'),
                         'hello world')

    def test_mixed(self):
        self.assertEqual(filter_lower('Hello! Привет,Worldмир!'),
                         'hello world')


def filter_lower(text: str) -> str:
    return (''.join(char for char in text if char in ascii_letters or char == ' ')).lower()


if __name__ == '__main__':
    unittest.main(verbosity=2)
