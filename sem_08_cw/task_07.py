# Задание No7
# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.

import csv
import pickle


def csv2pickle(csv_file_path: str) -> None:
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, dialect='excel')

        data_list = []
        headers = []
        for i, row in enumerate(csv_reader):
            if not i:
                headers = row
            else:
                row_data = {key: value for key, value in zip(headers, row)}
                data_list.append(row_data)
    print(pickle.dumps(data_list))


csv2pickle('task_06_file.csv')
