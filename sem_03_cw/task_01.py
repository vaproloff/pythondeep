# Задание No1.
# ✔ Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

some_list = [1, 3, 1, 3, 6, 7, 8, 5, 8]

some_list_unique = []

for item in some_list:
    if item not in some_list_unique:
        some_list_unique.append(item)

print(some_list)
print(some_list_unique)

print(list(set(some_list)))
