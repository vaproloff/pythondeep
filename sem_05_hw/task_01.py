# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def parse_link(link: str) -> tuple[str, str, str]:
    *path, file = link.split('/')
    *file_name, file_extension = file.split('.')
    return '/'.join(path), '.'.join(file_name), file_extension


print(parse_link('/Users/xvp/Documents/Обучение GeekBrains/3. Технологическая специализация/'
                 '1. Погружение в Python/pythonDeep/sem_05_hw/task_01.py'))
