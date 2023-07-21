# Задание No2.
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint

"""Guess number game
"""

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
    print(guess(0, 100, 5))
