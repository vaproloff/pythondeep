# Задание No1
# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдоименами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.

import json


def process_num_and_names(path_nums_names: str, path_json: str) -> None:
    nums_names_dict = {}
    with open(path_nums_names, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            name_str, num_str = line.split('|')
            nums_names_dict[name_str.capitalize()] = float(num_str)

    with open(path_json, 'w', encoding='utf-8') as json_file:
        json.dump(nums_names_dict, json_file, ensure_ascii=False, indent=2)


process_num_and_names('task_01_file.txt', 'task_01_file.json')
