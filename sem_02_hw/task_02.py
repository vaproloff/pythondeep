# Задание 2.
# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions.

import fractions


def reduce_fraction(num, denom):
    max_divider = num if num <= denom else denom
    for i in range(max_divider, 0, -1):
        if num % i == 0 and denom % i == 0:
            return [int(num / i), int(denom / i)]


input_frac_1 = input('Введите первую дробь в виде “a/b”: ')
input_frac_2 = input('Введите вторую дробь в виде “a/b”: ')

frac_1 = list(map(int, input_frac_1.split('/')))
frac_2 = list(map(int, input_frac_2.split('/')))

frac_sum = [frac_1[0] * frac_2[1] + frac_2[0] * frac_1[1],
            frac_1[1] * frac_2[1]]
frac_sum = reduce_fraction(frac_sum[0], frac_sum[1])
frac_sum_str = str(frac_sum[0]) + (f'/{frac_sum[1]}' if frac_sum[1] != 1 else "")

frac_mul = [frac_1[0] * frac_2[0],
            frac_1[1] * frac_2[1]]
frac_mul = reduce_fraction(frac_mul[0], frac_mul[1])
frac_mul_str = str(frac_mul[0]) + (f'/{frac_mul[1]}' if frac_mul[1] != 1 else "")

print(f'{input_frac_1} + {input_frac_2} = {frac_sum_str}')
print(f'Проверка: {fractions.Fraction(input_frac_1) + fractions.Fraction(input_frac_2)}')

print(f'{input_frac_1} x {input_frac_2} = {frac_mul_str}')
print(f'Проверка: {fractions.Fraction(input_frac_1) * fractions.Fraction(input_frac_2)}')
