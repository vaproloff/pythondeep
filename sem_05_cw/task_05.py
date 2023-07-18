# Задание No5
# ✔ Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

# for i in range(1, 101):
#     result = None
#     if i % 3 == 0:
#         result = 'Fizz'
#         if i % 5 == 0:
#             result = 'FizzBuzz'
#     elif i % 5 == 0:
#         result = 'Buzz'
#     else:
#         result = i
#     print(result)

fizz_buzz = ('FizzBuzz' if i % 15 == 0 else
             ('Fizz' if i % 3 == 0 else
              ('Buzz' if i % 5 == 0 else i))
             for i in range(1, 101))
print(*fizz_buzz, sep='\n')
