import json

__all__ = ['num_and_names2json']


def num_and_names2json(path_nums_names: str, path_json: str) -> None:
    nums_names_dict = {}
    with open(path_nums_names, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            name_str, num_str = line.split('|')
            nums_names_dict[name_str.capitalize()] = float(num_str)

    with open(path_json, 'w', encoding='utf-8') as json_file:
        json.dump(nums_names_dict, json_file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    num_and_names2json('task_01_file.txt', 'task_01_file.json')
