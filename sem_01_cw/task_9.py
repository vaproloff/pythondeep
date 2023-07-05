# Задание 9.
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(2, 11):
    for k in range(2, 6):
        print(k, 'X', i, '=', i * k, end='\t\t')
    print()

print()

for i in range(2, 11):
    for k in range(6, 10):
        print(k, 'X', i, '=', i * k, end='\t\t')
    print()
