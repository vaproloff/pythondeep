# Задание No4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
#    ○ шестизначный идентификационный номер
#    ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from random import randint
from task_03 import Person, Gender


class Employee(Person):
    __min_id = 100000
    __max_id = 999999
    __max_level = 7

    def __init__(self, name: str, surname: str, patronymic: str, age: int, gender: Gender, id_num: int):
        super().__init__(name, surname, patronymic, age, gender)
        self.id_num = id_num if self.__min_id <= id_num <= self.__max_id else randint(self.__min_id, self.__max_id)
        self.access_level = self._get_level()

    def _get_level(self):
        return sum(int(char) for char in str(self.id_num)) % self.__max_level


if __name__ == '__main__':
    bob_1 = Employee('Bob', 'Bobor', '', 34, Gender.m, 213123)
    bob_2 = Employee('Bob', 'Bobor', '', 34, Gender.m, 213123)

    print(hash(bob_1))
    print(hash(bob_2))
