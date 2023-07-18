# Задание No4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

# odd_num_gen = (num for num in range(0, 101, 2) if (num % 10 + num // 10) != 8)
odd_num_gen = (num for num in range(0, 101, 2) if sum(map(int, str(num))) != 8)

print(*odd_num_gen)
