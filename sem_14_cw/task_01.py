# Задание No1
# 📌 Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.

from string import ascii_letters


def remove_chars(text: str) -> str:
    return (''.join(char for char in text if char in ascii_letters or char == ' ')).lower()


if __name__ == '__main__':
    s = 'Hellok2f09ij30 xf.34c.ct45, t345'
    print(remove_chars(s))
