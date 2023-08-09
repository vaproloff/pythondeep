# Задание No1
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания (time.time)

import time


class MyStr(str):
    """
    Adds creator's name and creating time to string
    """
    def __init__(self, text: str, creator: str):
        print('Init started')

    def __new__(cls, text: str, creator: str):
        instance = super().__new__(cls, text)
        instance.creator = creator
        instance.time = time.time()
        return instance


if __name__ == '__main__':
    my_string = MyStr("Hello world", 'User 1')
