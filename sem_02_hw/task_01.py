# Задание 1.
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX_DIGITS = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def convert_to_hex(dec_num):
    result: str = ''
    while dec_num > 0:
        remainder = dec_num % 16
        if remainder > 9:
            remainder = HEX_DIGITS[remainder]
        result = f'{str(remainder)}{result}'
        dec_num //= 16
    return result or '0'


input_num = int(input('Введите целое число: '))
print(f'Шестнадцатеричное представление: {convert_to_hex(input_num)}')
