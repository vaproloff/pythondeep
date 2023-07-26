# Задание No3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.
from typing import TextIO


def process_names_and_nums():
    with (
        open('task_01_file.txt', 'r', encoding='utf-8') as num_file,
        open('task_02_file.txt', 'r', encoding='utf-8') as names_file,
        open('task_03_file.txt', 'a', encoding='utf-8') as res_file
    ):
        len_nums = len(num_file.readlines())
        len_names = len(names_file.readlines())
        for _ in range(max(len_names, len_nums)):
            cur_name = read_or_begin(names_file)
            cur_num_1, cur_num_2 = map(float, read_or_begin(num_file).split('|'))
            mul_nums = cur_num_1 * cur_num_2
            if mul_nums > 0:
                res_file.write(f'{cur_name.upper()} {round(mul_nums)}')
            else:
                res_file.write(f'{cur_name.lower()} | {abs(mul_nums)}\n')


def read_or_begin(file_io: TextIO) -> str:
    text = file_io.readline()
    if not text:
        file_io.seek(0)
        text = file_io.readline()

    return text[:-1]


process_names_and_nums()
