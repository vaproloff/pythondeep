# Задание 8.
# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

rows = int(input('Введите количество рядов ёлки: '))
width = rows

for i in range(MIN_ROWS, rows + 1):
    print(' ' * (rows - i) * 2 + '* ' * ((i - 1) * 2 + 1))
