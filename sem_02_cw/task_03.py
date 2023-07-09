# Задание No3.
# ✔ Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

BIN_DIVIDER = 2
OCT_DIVIDER = 8


def convert_num(number, divider):
    result: str = ''
    while number > 0:
        result = f'{str(number % divider)}{result}'
        number //= divider
    return result or '0'


dec_num = int(input('Введите целое число: '))
print(f'Двоичное представление: {convert_num(dec_num, BIN_DIVIDER)}')
print(f'Восьмеричное представление: {convert_num(dec_num, OCT_DIVIDER)}')
