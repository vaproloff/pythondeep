# Задание No4.
# ✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

import math
import decimal

decimal.getcontext().prec = 42
PI = decimal.Decimal(math.pi)

diameter = -1
while diameter < 0 or diameter > 1000:
    diameter = decimal.Decimal(input('Введите диаметр (от 0 до 1000): '))

square: decimal.Decimal = PI * (diameter / 2) ** 2
length: decimal.Decimal = PI * diameter

print(f'Площадь круга: {square}. Длина окружности: {length}')
