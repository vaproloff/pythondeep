# Задание No2
# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключом для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.

import os
import json


def add_data_to_json(json_file):
    user_ids = set()
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as data_file:
            data = json.load(data_file)
            for user in data.values():
                user_ids.update(user.keys())
    else:
        data = {str(access_level): dict() for access_level in range(1, 8)}

    while True:
        name = input('Введите имя: ')
        if not name:
            break
        user_id = input('Введите ID: ')
        if user_id in user_ids:
            continue
        access_level = input('Введите уровень доступа: ')
        data[access_level][user_id] = name
        with open(json_file, 'w', encoding='utf-8') as data_file:
            json.dump(data, data_file, indent=2, ensure_ascii=False)


add_data_to_json('task_02_file.json')
