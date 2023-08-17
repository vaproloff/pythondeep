from typing import Callable
from functools import wraps
import random
from os.path import exists
import json


class GuessNumberException(Exception):
    pass


class OutOfRangeException(GuessNumberException):
    def __init__(self, number: int, min_num: int, max_num: int):
        self.number = number
        self.min_num = min_num
        self.max_num = max_num

    def __str__(self):
        return f'Secret number {self.number} is out of range ({self.min_num}, {self.max_num})'


class InvalidTrialsException(GuessNumberException):
    def __init__(self, trials_qty: int):
        self.trials_qty = trials_qty

    def __str__(self):
        return f'Quantity of trials should be positive number: {self.trials_qty}'


def validate(func: Callable) -> Callable[[int, int], None]:
    min_number = 1
    max_number = 100
    min_guess_trials = 1
    max_guess_trials = 10

    @wraps(func)
    def wrapper(secret_num: int, guess_qty: int, *args, **kwargs):
        if not min_number <= secret_num <= max_number:
            raise OutOfRangeException(secret_num, min_number, max_number)
        if not min_guess_trials <= guess_qty <= max_guess_trials:
            raise InvalidTrialsException(guess_qty)

        return func(secret_num, guess_qty, *args, **kwargs)

    return wrapper


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


def trials(calls_qty: int) -> Callable:
    results = []

    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(calls_qty):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return deco


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
    guess_num(100, 0)
