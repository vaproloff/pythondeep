# Задание No2
# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, a: float, b: float = None):
        self.a = a
        self.b = b if b is None else a

    def get_perimeter(self) -> float:
        return 2 * (self.a + self.b)

    def get_area(self) -> float:
        return self.a * self.b
