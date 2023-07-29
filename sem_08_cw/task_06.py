# Задание No6
# 📌 Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# 📌 Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import pickle
import csv


def pickle2csv(pickle_file_path: str, csv_file_path: str) -> None:
    with open(pickle_file_path, 'rb') as pickle_file:
        data = pickle.load(pickle_file)
    headers = data[0].keys()
    with open(csv_file_path, 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers, dialect='excel',
                                    quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)


pickle2csv('task_02_file.pickle', 'task_06_file.csv')
