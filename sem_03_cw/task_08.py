# Задание No8.
# ✔ Три друга взяли вещи в поход.
# Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться на любое большее количество друзей.

friends = {
    'Пётр': ('палатка', 'фонарик', 'вода', 'сухое топливо'),
    'Иван': ('палатка', 'спальный мешок', 'сухое топливо', 'вода'),
    'Андрей': ('палатка', 'котелок', 'сухое топливо', 'удочка'),
    'Антон': ('палатка', 'спальный мешок', 'вода', 'коврик', 'аккумулятор')
}

# ✔ Какие вещи взяли все три друга
common_items = set(friends[list(friends.keys())[0]])
for key, value in friends.items():
    common_items = common_items.intersection(value)
print('Общие для всех вещи:', common_items)

# ✔ Какие вещи уникальны, есть только у одного друга
# unique_items = list()
# for key in friends.keys():
#     unique_current = set(friends[key])
#     other_keys = list(friends.keys())
#     other_keys.remove(key)
#     for other_key in other_keys:
#         unique_current = unique_current - set(friends[other_key])
#     unique_items.extend(unique_current)
# print('Уникальные вещи:', unique_items)

qty_items = dict()
for value in friends.values():
    for item in value:
        item_val = qty_items.setdefault(item, 0)
        qty_items[item] += 1
unique_items = []
for key, value in qty_items.items():
    if value == 1:
        unique_items.append(key)
print('Уникальные вещи:', unique_items)

# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
absent_items = []
absent_friends = dict()
for key, value in qty_items.items():
    if value == (len(friends) - 1):
        absent_items.append(key)
for item in absent_items:
    for key,value in friends.items():
        if item not in value:
            absent_friends[key] = item
print('Друзья и вещи, которых у них нет', absent_friends)
