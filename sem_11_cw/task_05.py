# Задание No5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длину и ширину.
# 📌 При вычитании не допускайте отрицательных значений.

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


if __name__ == '__main__':
    rect_1 = Rectangle(5, 10)
    print(rect_1.get_perimeter())
    rect_2 = Rectangle(2, 5)
    rect_3 = rect_1 + rect_2
    rect_4 = rect_2 - rect_1
    print(f'{rect_3.a = }, {rect_3.b = }, {rect_3.get_perimeter()}')
    print(f'{rect_4.a = }, {rect_4.b = }, {rect_4.get_perimeter()}')
