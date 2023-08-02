# Задание No6
# 📌 Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.

from task_02 import deco as validate
from task_03 import add_param_to_json
from task_04 import param_deco as trials


@trials(3)
@validate
@add_param_to_json
def guess_num(secret_num: int, guess_qty: int):
    """Guess number game"""
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
    guess_num(15, 3)
    print(f'{guess_num.__name__ = }')
    print(f'{guess_num.__doc__ = }')
