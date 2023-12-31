# Задание No5.
# ✔ Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# ✔ Используйте комплексные числа для извлечения квадратного корня.

a, b, c = map(int, input('Введите коэффициенты a, b, c через пробел: ').split())
result = ''

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    result = f'x1: {x1}, x2: {x2}'
elif d == 0:
    x = -b / (2 * a)
    result = f'x: {x}'
else:
    d = complex(d, 0)
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    result = f'x1: {x1}, x2: {x2}'

print(result)
