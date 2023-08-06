class QuadraticEquation:
    def __init__(self, a: float = 0, b: float = 0, c: float = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = self.get_d()

    def get_d(self) -> float:
        return self.b ** 2 - 4 * self.a * self.c

    def get_roots(self) -> float | tuple[float | complex, float | complex]:
        if self.d == 0:
            return -self.b / (2 * self.a)
        elif self.d > 0:
            return (-self.b + self.d ** 0.5) / (2 * self.a), (-self.b - self.d ** 0.5) / (2 * self.a)
        else:
            complex_d = complex(self.d, 0)
            return (-self.b + complex_d ** 0.5) / (2 * self.a), (-self.b - complex_d ** 0.5) / (2 * self.a)

    def pretty_print_equation(self) -> None:
        res_str = ''
        if self.a:
            res_str += f'{self.a}x²'
        if self.b:
            res_str += f' + {self.b}x' if self.b > 0 else f' - {abs(self.b)}x'
        if self.c:
            res_str += ' + ' if self.c > 0 else ' - '
            res_str += str(abs(self.c))
        res_str += ' = 0'
        print(res_str)


if __name__ == '__main__':
    quadratic_equation = QuadraticEquation(-10, 17, -18)
    quadratic_equation.pretty_print_equation()
    print(quadratic_equation.get_roots())
