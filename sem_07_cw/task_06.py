# Задание No6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from string import ascii_lowercase, digits
from random import choices, randint
from os import path, mkdir, chdir


def make_files(extension: str, min_name_len: int = 6, max_name_len: int = 30,
               min_bytes: int = 256, max_bytes: int = 4096,
               files_qty: int = 42) -> None:
    for _ in range(files_qty):
        file_name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name_len, max_name_len)))
        file_data = bytes(randint(0, 255) for _ in range(randint(min_bytes, max_bytes)))
        with open(rf'{file_name}.{extension}', 'wb') as bin_file:
            bin_file.write(file_data)


def make_dir(dir, **kwargs) -> None:
    if not path.exists(dir):
        mkdir(dir)
    chdir(dir)
    many_extensions(**kwargs)


def many_extensions(**kwargs):
    for ext, qty in kwargs.items():
        make_files(ext, files_qty=qty)


make_dir('./task_06_dir', doc=3, jpeg=7, gif=9, txt=10)
