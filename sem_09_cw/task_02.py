# Задание No2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.

import random
from typing import Callable
from functools import wraps


def deco(func: Callable) -> Callable[[int, int], None]:
    min_number = 1
    max_number = 100
    min_guess_trials = 1
    max_guess_trials = 10

    @wraps(func)
    def wrapper(secret_num: int, guess_qty: int, *args, **kwargs):
        if not min_number <= secret_num <= max_number:
            secret_num = random.randint(min_number, max_number)
        if not min_guess_trials <= guess_qty <= max_guess_trials:
            guess_qty = random.randint(min_guess_trials, max_guess_trials)

        return func(secret_num, guess_qty, *args, **kwargs)

    return wrapper


@deco
def guess_num(secret_num: int, guess_qty: int):
    for i in range(1, guess_qty + 1):
        answer = int(input(f'Номер попытки: {i}. Угадайте число от 1 до 100: '))
        if answer == secret_num:
            print('Вы угадали!')
            return
        elif answer > secret_num:
            print('Меньше')
        else:
            print('Больше')


if __name__ == '__main__':
    guess_num(15, 4)
