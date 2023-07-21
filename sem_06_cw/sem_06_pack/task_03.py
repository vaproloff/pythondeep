# Задание №3.
# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from random import randint
from sys import argv

"""Guess number game
"""

__all__ = ['guess']

MAX_NUM = 0
MIN_NUM = 100
TRIALS = 3


def guess(min_num: int = MIN_NUM, max_num: int = MAX_NUM, tries: int = TRIALS):
    secret_num = randint(min_num, max_num)
    while tries > 0:
        user_number = int(input(f'Осталось попыток: {tries}. Угадайте число от {min_num} до {max_num}: '))
        if user_number == secret_num:
            print('Вы угадали!')
            return True
        elif user_number > secret_num:
            print('Меньше.')
        else:
            print('Больше.')
        tries -= 1
    else:
        print('Не угадали. Попыток не осталось.')
        return False


if __name__ == '__main__':
    name, *args = argv
    print(guess(*(int(arg) for arg in args)))
