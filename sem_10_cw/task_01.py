# Задание No1
# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi


class Circle:
    def __init__(self, r: float):
        self.r = r

    def get_length(self) -> float:
        return 2 * pi * self.r

    def get_area(self) -> float:
        return pi * self.r ** 2
