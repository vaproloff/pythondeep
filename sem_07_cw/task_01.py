# Задание No1
# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random

MIN_NUM = -1000
MAX_NUM = 1000


def fill_file(file_name='names.txt', limit=1000):
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(limit + 1):
            first_int = random.randint(MIN_NUM, MAX_NUM)
            second_float = random.uniform(MIN_NUM, MAX_NUM)
            file.write(f'{first_int}|{second_float}\n')


fill_file('task_01_file.txt')
