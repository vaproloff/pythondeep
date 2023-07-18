# Задание No6
# ✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного генератора,
#   где каждый элемент генератора — отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт» без перехода на новую строку.

# mul_table = (f'{i} x {j} = {i * j}' for i in range(2, 10) for j in range(2, 11))


# for i in range(2, 10):
#     for j in range(2, 11):
#         for k in range(i, i + 4):
#             if k != i + 4 - 1:
#                 print(f'{k:>2} x {j:>2} = {k * j:>2}\t')
#             elif j != 10:
#                 print(f'{k:>2} x {j:>2} = {k * j:>2}\n')
#             else:
#                 print(f'{k:>2} x {j:>2} = {k * j:>2}\n\n')
#
# mul_table = (f'\t{k:>2} x {j:>2} = {k * j:>2}\t' if k != i + 4 - 1 else
#              f'{k:>2} x {j:>2} = {k * j:>2}\n' if j != 10 else
#              f'{k:>2} x {j:>2} = {k * j:>2}\n\n'
#              for i in range(2, 10, 4)
#              for j in range(2, 11)
#              for k in range(i, i + 4))
#
# print(*mul_table)


# for i in range(2, 11):
#     for j in range(2, 6):
#         end_print = '\t\t'
#         if (j - 1) % 4 == 0:
#             end_print = '\n'
#         print(f'{j} x {i} = {i * j}', end=end_print)

mul_table = (f'\t{j:>2} x {i:>2} = {i * j:>2}' +
             ('\n\n' if i == 10 and (j - 1) % 4 == 0 else '\n' if (j - 1) % 4 == 0 else '\t')
             for k in range(4, 9, 4) for i in range(2, 11) for j in range(k - 2, 2 + k))
print(*mul_table)
