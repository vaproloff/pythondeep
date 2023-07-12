# Задание No4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

from collections import defaultdict

DUBLICATES = 3

some_list = [1, 3, 1, 3, 6, 7, 8, 5, 8, 1, 6, 5, 5, 7, 9]
# qty_dict = {}
qty_dict = defaultdict(int)

# for item in some_list:
#     value = qty_dict.setdefault(item, 0)
#     qty_dict[item] += 1

for item in some_list:
    qty_dict[item] += 1

print(qty_dict)

for key, value in qty_dict.items():
    if value == DUBLICATES:
        for _ in range(DUBLICATES):
            some_list.remove(key)

print(some_list)
