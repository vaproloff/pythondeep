# Задание No5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from string import ascii_lowercase, digits
from random import choices, randint


def make_files(extension: str, min_name_len: int = 6, max_name_len: int = 30,
               min_bytes: int = 256, max_bytes: int = 4096, files_qty: int = 42) -> None:
    for _ in range(files_qty):
        file_name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name_len, max_name_len)))
        file_data = bytes(randint(0, 255) for _ in range(randint(min_bytes, max_bytes)))
        with open(rf'task_04_dir/{file_name}.{extension}', 'wb') as bin_file:
            bin_file.write(file_data)


def many_extensions(**kwargs):
    for ext, qty in kwargs.items():
        make_files(ext, files_qty=qty)


many_extensions(txt=3, jpeg=7)
