# Задание No3
# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

class FactorialRange:
    def __init__(self, stop: int, start: int = 1, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    @staticmethod
    def calc_factorial(number: int):
        mul_num = 1
        for i in range(2, number + 1):
            mul_num *= i
        return mul_num

    def __next__(self):
        if self.start < self.stop:
            result = self.calc_factorial(self.start)
            self.start += self.step
            return result
        raise StopIteration


if __name__ == '__main__':
    fact_range = FactorialRange(20, 10)
    for i, item in enumerate(fact_range, start=10):
        print(i, item)
    print(next(fact_range))
