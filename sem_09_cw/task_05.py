# Задание No5
# 📌 Объедините функции из прошлых задач.
# 📌 Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# 📌 Выберите верный порядок декораторов.

from task_02 import deco as validate
from task_03 import add_param_to_json
from task_04 import param_deco as trials


@trials(3)
@validate
@add_param_to_json
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
    guess_num(15, 3)
