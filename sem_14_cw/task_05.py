# Задание No5
# 📌 На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
#    площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.

import unittest


class TestRect(unittest.TestCase):
    def setUp(self) -> None:
        self.rect_1 = Rectangle(2, 4)
        self.rect_2 = Rectangle(7)
        self.rect_3 = Rectangle(10, 5)
        self.rect_4 = Rectangle(1, 1)

    def test_creating(self):
        self.assertEqual(self.rect_1, Rectangle(2, 4))

    def test_perimeter(self):
        self.assertEqual(self.rect_2.get_perimeter(), 28)

    def test_area(self):
        self.assertEqual(self.rect_3.get_area(), 50)

    def test_not_eq(self):
        self.assertNotEqual(self.rect_1, self.rect_3)

    def test_sum(self):
        self.assertEqual(self.rect_2 + self.rect_4, Rectangle(8))

    def test_sub(self):
        self.assertEqual(self.rect_2 - self.rect_4, Rectangle(6))


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
    unittest.main(verbosity=2)
