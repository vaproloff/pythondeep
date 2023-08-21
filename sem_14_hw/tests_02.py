import pytest


class QuadraticEquation:
    def __init__(self, a: float = 0, b: float = 0, c: float = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = self.get_d()

    def get_d(self) -> float:
        return self.b ** 2 - 4 * self.a * self.c

    def get_roots(self) -> float | tuple[float, float] | None:
        if self.d == 0:
            return -self.b / (2 * self.a)
        elif self.d > 0:
            return (-self.b + self.d ** 0.5) / (2 * self.a), (-self.b - self.d ** 0.5) / (2 * self.a)
        else:
            return None

    def __str__(self):
        res_str = ''
        if self.a:
            res_str += f'{self.a}x²'
        if self.b:
            res_str += f' + {self.b}x' if self.b > 0 else f' - {abs(self.b)}x'
        if self.c:
            res_str += ' + ' if self.c > 0 else ' - '
            res_str += str(abs(self.c))
        res_str += ' = 0'
        return res_str


def test_print():
    assert str(QuadraticEquation(4, 2, -3)) == f'4x² + 2x - 3 = 0'


def test_one_root():
    qe = QuadraticEquation(1, -4, 4)
    assert qe.get_roots() == 2


def test_two_roots():
    qe = QuadraticEquation(1, 3, -4)
    assert qe.get_roots() == (-4, 1) or qe.get_roots() == (1, -4)


def test_no_roots():
    qe = QuadraticEquation(1, -5, 9)
    assert qe.get_roots() is None


if __name__ == '__main__':
    pytest.main(['-vv'])
