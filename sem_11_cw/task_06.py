# Задание No6
# 📌 Доработайте прошлую задачу.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения


class Rectangle:
    def __init__(self, a: float, b: float = None):
        self.a = a
        self.b = b if b is not None else a

    def get_perimeter(self) -> float:
        return 2 * (self.a + self.b)

    def get_area(self) -> float:
        return self.a * self.b

    def __add__(self, other):
        sum_perimeter = self.get_perimeter() + other.get_perimeter()
        k = sum_perimeter / self.get_perimeter()
        return Rectangle(self.a * k, self.b * k)

    def __sub__(self, other):
        sub_perimeter = abs(self.get_perimeter() - other.get_perimeter())
        k = sub_perimeter / self.get_perimeter()
        return Rectangle(self.a * k, self.b * k)

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()


if __name__ == '__main__':
    rect_1 = Rectangle(5, 10)
    print(rect_1.get_perimeter())
    rect_2 = Rectangle(2, 5)
    print(rect_1 == rect_2)
    print(rect_1 >= rect_2)
