# Задание No3
# 📌 Создайте класс с базовым исключением и дочерние классы-исключения:
#       ○ ошибка уровня,
#       ○ ошибка доступа.

# Задание No6
# 📌 Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# 📌 Передавайте необходимые данные из основного кода проекта.

from task_04 import User


class MyException(Exception):
    pass


class LevelException(MyException):
    def __init__(self, level: int, user: User):
        self.level = level
        self.user = user

    def __str__(self):
        return f'Нельзя добавить пользователя с уровнем {self.level}.' \
                f'Вы вошли как {self.user.name} с уровнем {self.user.user_level}.'


class AccessException(MyException):
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f'Отказано в доступе! ' \
                f'Пользователь с именем {self.name} и ID {self.user_id} не найден'
