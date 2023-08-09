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
        """Prints starting log to console"""
        print('Init started')

    def __new__(cls, text: str, creator: str):
        """Adding new attributes - creator's name and creating time - to new class instance"""
        instance = super().__new__(cls, text)
        instance.creator = creator
        instance.time = time.time()
        return instance

    def __str__(self):
        """User string output method"""
        return f'"{super().__str__()}" (creator: {self.creator}, created at: {self.time})'

    def __repr__(self):
        """Developer string representation method. Shows creating instance instruction."""
        return f'MyStr("{super().__str__()}", "{self.creator}")'


if __name__ == '__main__':
    my_string = MyStr("Hello world", 'User 1')
    print(my_string)
    print(repr(my_string))
