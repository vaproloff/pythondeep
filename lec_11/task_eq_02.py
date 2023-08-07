class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'

    def __eq__(self, other):
        """True if id(self) == id(other) else False"""
        return self is other


one = Triangle(3, 4, 5)
two = one
three = Triangle(3, 4, 5)
print(one == two)
print(one == three)
