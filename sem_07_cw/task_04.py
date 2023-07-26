# Задание No4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from string import ascii_lowercase, digits
from random import choices, randint


def make_files(extension: str, min_name_len: int = 6, max_name_len: int = 30,
               min_bytes: int = 256, max_bytes: int = 4096, files_qty: int = 42) -> None:
    for _ in range(files_qty):
        file_name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name_len, max_name_len)))
        file_data = bytes(randint(0, 255) for _ in range(randint(min_bytes, max_bytes)))
        with open(rf'task_04_dir/{file_name}.{extension}', 'wb') as bin_file:
            bin_file.write(file_data)


make_files('bin')
