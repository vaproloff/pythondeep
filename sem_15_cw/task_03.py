# Задание No3
# 📌 Доработаем задачу 2.
# 📌 Сохраняйте в лог файл раздельно:
#    ○ уровень логирования,
#    ○ дату события,
#    ○ имя функции (не декоратора),
#    ○ аргументы вызова,
#    ○ результат.

import logging
from typing import Callable

FORMAT = '{levelname} - {asctime} - {msg}'

logging.basicConfig(filename='task_03.log', encoding='utf-8', level=logging.INFO,
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def add_to_log(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_dct = {'args': args, **kwargs}
        log_msg = f'{func.__name__}: {log_dct}. Result: {result}'
        logger.info(log_msg)
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
