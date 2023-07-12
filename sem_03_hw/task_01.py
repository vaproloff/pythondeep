# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

some_list = [1, 3, 1, 3, 6, 7, 8, 5, 8, 1, 6, 5, 5, 9]
doubles = set()

for item in some_list:
    if some_list.count(item) > 1:
        doubles.add(item)

print('Список:', some_list)
print('Повторяющиеся элементы:', list(doubles))
