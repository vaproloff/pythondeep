from typing import Callable


def deco_a(func: Callable):
    def wrapper_a(*args, **kwargs):
        print('старт декоратора А')
        print(f'Запускаю {func.__name__}')
        result = func(*args, **kwargs)
        print('Завершение декоратора А')
        return result

    print('Возвращаем декоратор А')
    return wrapper_a


def deco_b(func: Callable):
    def wrapper_b(*args, **kwargs):
        print('старт декоратора B')
        print(f'Запускаю {func.__name__}')
        result = func(*args, **kwargs)
        print('Завершение декоратора B')
        return result

    print('Возвращаем декоратор B')
    return wrapper_b


def deco_c(func: Callable):
    def wrapper_c(*args, **kwargs):
        print('старт декоратора C')
        print(f'Запускаю {func.__name__}')
        result = func(*args, **kwargs)
        print('Завершение декоратора C')
        return result

    print('Возвращаем декоратор C')
    return wrapper_c


@deco_c
@deco_b
@deco_a
def main():
    print('Старт основной функции')


if __name__ == '__main__':
    print('>>> Запуск main()')
    main()
    print('>>> Завершение main()')
