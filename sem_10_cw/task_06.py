# Задание No6
# 📌 Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name: str, color: str, size: float):
        self.name = name
        self.color = color
        self.size = size

    def show_unique(self):
        pass


class Fish(Animal):
    def __init__(self, name: str, color: str, size: float, max_depth: float):
        super().__init__(name, color, size)
        self.max_depth = max_depth

    def show_unique(self):
        print(f'Max depth: {self.max_depth}')


class Bird(Animal):
    def __init__(self, name: str, color: str, size: float, max_height: float):
        super().__init__(name, color, size)
        self.max_height = max_height

    def show_unique(self):
        print(f'Max height: {self.max_height}')


class Cat(Animal):
    def __init__(self, name: str, color: str, size: float, hairy: bool):
        super().__init__(name, color, size)
        self.hairy = hairy

    def show_unique(self):
        print(f'Is hairy: {self.hairy}')


if __name__ == '__main__':
    fish_1 = Fish('Petushok', 'gray', 10.0, 756)
    bird_1 = Bird('Chirik', 'blue', 17.3, 2300)
    cat_1 = Cat('Matroskin', 'red', 23.5, True)

    animals = (fish_1, bird_1, cat_1)
    for animal in animals:
        animal.show_unique()
