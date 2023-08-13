# Задание No6
# 📌 Изменяем класс прямоугольника.
# 📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Descr:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.name, value)
        else:
            raise ValueError('Отрицательные и нулевое значения недопустимы')


class Rectangle:
    """
    Rectangle class representation.
    """
    a = Descr()
    b = Descr()

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
    print(rect_1.a)
    rect_2.b = 0
