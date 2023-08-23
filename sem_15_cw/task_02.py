# Задание No2
# 📌 На семинаре о декораторах был создан логирующий декоратор.
#    Он сохранял аргументы функции и результат её работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте модуль logging.

import logging
from typing import Callable

logging.basicConfig(filename='task_02.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def add_to_log(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_data = {'args': args, **kwargs, 'result': result}
        logger.info(log_data)
        return result

    return wrapper


@add_to_log
def division(a: int, b: int) -> float:
    try:
        result = a / b
    except ZeroDivisionError as e:
        result = float('inf')
    return result


if __name__ == '__main__':
    print(division(10, 2))
    print(division(10, 5))
