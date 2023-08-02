"""FizzBuzz game
"""

__all__ = ['fizzbuzz']

MIN_NUM = 1
MAX_NUM = 100


def fizzbuzz():
    print(f'''FizzBuzz
    Вы должны вводить числа от {MIN_NUM} до {MAX_NUM}.
    Если число кратно 3-м - напишите "Fizz",
    если кратно 5-ти - "Buzz",
    если 3-м и 5-ти одновременно - "FizzBuzz".
    Начнём!
    ''')
    for i in range(MIN_NUM, MAX_NUM + 1):
        user_input = input('Введите число или слово: ').lower()

        if i % 3 == 0 and i % 5 == 0 and user_input == 'fizzbuzz':
            continue
        elif i % 3 == 0 and user_input == 'fizz':
            continue
        elif i % 5 == 0 and user_input == 'buzz':
            continue
        elif i % 3 != 0 and i % 5 != 0 and user_input == str(i):
            continue
        else:
            print(f'Вы проиграли. Набрано очков: {i}')

    print('Абсолютная победа! Поздравляем!')


if __name__ == '__main__':
    fizzbuzz()
