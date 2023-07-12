# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Верните все возможные варианты комплектации рюкзака.

import copy

COMBINATIONS_QTY = 100
SHOW_ONLY_BEST = True

camp_items = {
    'палатка': 3.5,
    'фонарик': 0.5,
    'вода': 1.0,
    'спальный мешок': 1.2,
    'котелок': 0.8,
    'удочка': 1.1,
    'коврик': 1.3,
    'аккумулятор': 1.3,
    'нож раскладной': 0.3,
    'горелка': 1.0,
    'палки для трекинга': 1.2,
    'стул раскладной': 2.7,
    'набор посуды': 1.4,
    'термос': 0.6,
    'газовый балон': 0.8
}

bag_capacity = int(input('Грузоподъемность рюкзака: '))

bags = []
max_weight = 0
for item, weight in camp_items.items():
    if weight <= bag_capacity:
        current_bags = []
        for bag in bags:
            current_weight = round(weight + bag['weight'], 1)
            if current_weight <= bag_capacity:
                temp_bag = copy.deepcopy(bag)
                temp_bag['weight'] = current_weight
                temp_bag['items'].append(item)
                current_bags.append(temp_bag)
                max_weight = max(max_weight, current_weight)
        if len(current_bags) > 0:
            for bag in current_bags:
                bags.append(bag)
        if bag_capacity > weight:
            bags.append({'items': [item], 'weight': round(weight, 1)})
            max_weight = max(max_weight, weight)

if SHOW_ONLY_BEST:
    best_bags = filter(lambda bag: bag['weight'] == max_weight, bags)
    print('Максимальные комплектации:')
    for bag in best_bags:
        print(f'Вес: {bag["weight"]}. Вещи: {", ".join(bag["items"])}')
else:
    sorted_bags = sorted(bags, key=lambda bag: bag['weight'], reverse=True)
    if len(sorted_bags) > COMBINATIONS_QTY:
        print(f'{COMBINATIONS_QTY} лучших комплектаций:')
    else:
        print(f'{len(sorted_bags)} комплектаций:')
    for bag in sorted_bags[:min(COMBINATIONS_QTY, len(sorted_bags))]:
        print(f'Вес: {bag["weight"]}. Вещи: {", ".join(bag["items"])}')
