# Задание 3.
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
#  from random import randint
#  num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

MIN_NUM = 0
MAX_NUM = 1000
TRIES = 10

secret_num = randint(MIN_NUM, MAX_NUM)

for i in range(TRIES):
    input_num = int(input(f'Осталось {TRIES - i} попыток. Введите число: '))
    if input_num == secret_num:
        print(f'Вы угадали с {i + 1} раза. Поздравляем!')
        break
    elif input_num < secret_num:
        print(f'Число {input_num} меньше загаданного')
    else:
        print(f'Число {input_num} больше загаданного')
else:
    print('Попыток не осталось. Вы не угадали.')
