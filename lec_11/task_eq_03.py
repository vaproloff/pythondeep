class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other._a, other._b, other._c))
        return first == second


one = Triangle(3, 4, 5)
two = one
three = Triangle(3, 4, 5)
four = Triangle(4, 3, 5)
print(one == two)
print(one == three)
print(one == four)
print(one != one)
