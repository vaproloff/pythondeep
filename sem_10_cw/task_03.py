# Задание No3
# 📌 Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п.
# 📌 Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

from enum import Enum


class Gender(Enum):
    m = 'm'
    f = 'f'


class Person:
    def __init__(self, name: str, surname: str, patronymic: str, age: int, gender: Gender):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self._age = age
        self.gender = gender.value

    def birthday(self) -> None:
        self._age += 1

    def full_name(self) -> str:
        return f'{self.surname} {self.name} {self.patronymic}'

    def get_age(self) -> int:
        return self._age

    def get_gender(self):
        return self.gender


if __name__ == '__main__':
    man = Person('Bob', 'Johnson', 'Петрович', 27, Gender.m)
    print(f'{man.get_age()}')
    man.birthday()
    print(f'{man.get_age()}')
    print(f'{man.full_name()}')
    print(f'{man.get_gender()}')
