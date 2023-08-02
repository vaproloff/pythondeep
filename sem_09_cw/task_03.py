# Задание No3
# 📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции
# и результат, который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой функции.

from functools import wraps
from typing import Callable
import json
from os.path import exists


def add_param_to_json(func: Callable) -> Callable[[list, dict], int]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_path = f'{func.__name__}.json'
        data = []

        if exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

        result = func(*args, **kwargs)
        cur_data = {
            'args': args,
            **kwargs,
            'result': result
        }
        data.append(cur_data)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)

        return result

    return wrapper


@add_param_to_json
def sum_nums(*args, **kwargs) -> int:
    return sum(args)


@add_param_to_json
def concat_str(*args, **kwargs) -> str:
    return ''.join(args)


if __name__ == '__main__':
    sum_nums(1, 8, 5, a=2, b=10, c=0)
    concat_str('sd', 'fgfd', 'dfds', word='hello', word2='bye')
