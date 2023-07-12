# Задание No3.
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где: ключ — тип элемента,
# значение — список элементов данного типа.

some_tuple = ('Hello', 232, 324.23, False, None, -4, True, 'string', 0.0035)
some_dict = dict()

for item in some_tuple:
    # if type(item) in some_dict.keys():
    #     some_dict[type(item)].append(item)
    # else:
    #     some_dict[type(item)] = [item]

    key = some_dict.setdefault(type(item), [])
    key.append(item)

print(some_dict)
