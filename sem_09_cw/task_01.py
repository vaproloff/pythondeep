# Задание No1
# 📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток.
# 📌 Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
from typing import Callable


def func_guess_num(secret_num: int, guess_qty: int) -> Callable[[], None]:
    def wrapper():
        for i in range(1, guess_qty + 1):
            answer = int(input(f'Номер попытки: {i}. Угадайте число от 1 до 100: '))
            if answer == secret_num:
                print('Вы угадали!')
                return
            elif answer > secret_num:
                print('Меньше')
            else:
                print('Больше')

    return wrapper


if __name__ == '__main__':
    game = func_guess_num(15, 4)
    game()
