# Задание No5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длину и ширину.
# 📌 При вычитании не допускайте отрицательных значений.

# Задание No6
# 📌 Доработайте прошлую задачу.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения

class Rectangle:
    """
    Rectangle class representation.
    """

    def __init__(self, a: float, b: float = None):
        """
        Takes rectangle sides. Adds then to class instance.
        If only one provided, a square assumed.
        """
        self.a = a
        self.b = b if b is not None else a

    def get_perimeter(self) -> float:
        """Returns perimeter (sum of all sides) of rectangle/square."""
        return 2 * (self.a + self.b)

    def get_area(self) -> float:
        """Returns area (product of two sides) of rectangle/square."""
        return self.a * self.b

    def __add__(self, other):
        """
        Allows to add one Rectangle instance to another by their perimeters.
        Returns new class instance with new sides.
        """
        sum_perimeter = self.get_perimeter() + other.get_perimeter()
        k = sum_perimeter / self.get_perimeter()
        return Rectangle(self.a * k, self.b * k)

    def __sub__(self, other):
        """
        Allows to subtract one Rectangle instance to another by their perimeters.
        Returns new class instance with new sides.
        """
        sub_perimeter = abs(self.get_perimeter() - other.get_perimeter())
        k = sub_perimeter / self.get_perimeter()
        return Rectangle(self.a * k, self.b * k)

    def __eq__(self, other):
        """Returns is Rectangle instance equal to another by its areas or not"""
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        """Returns is Rectangle instance area less than other's"""
        return self.get_area() < other.get_area()

    def __le__(self, other):
        """Returns is Rectangle instance area less or equal than other's"""
        return self.get_area() <= other.get_area()

    def __repr__(self):
        return f'Rectangle({self.a}, {self.b})'

    def __str__(self):
        if self.a == self.b:
            return f'Square with side {self.a}'
        else:
            return f'Rectangle with sides {self.a} and {self.b}'


if __name__ == '__main__':
    rect_1 = Rectangle(5, 10)
    rect_2 = Rectangle(10, 20)
    rect_3 = rect_1 + rect_2
    rect_4 = rect_2 - rect_1

    print(f'{rect_3.a = }, {rect_3.b = }, {rect_3.get_perimeter()}')
    print(f'{rect_4.a = }, {rect_4.b = }, {rect_4.get_perimeter()}')

    print(rect_1 < rect_2)
    print(rect_1 >= rect_2)

    print(rect_1)
