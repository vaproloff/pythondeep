# Задание No5
# 📌 Создайте три (или более) отдельных классов животных. Например: рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Fish:
    def __init__(self, name: str, color: str, size: float, max_depth: float):
        self.name = name
        self.color = color
        self.size = size
        self.max_depth = max_depth

    def show_max_depth(self):
        print(self.max_depth)


class Bird:
    def __init__(self, name: str, color: str, size: float, max_height: float):
        self.name = name
        self.color = color
        self.size = size
        self.max_height = max_height

    def show_max_height(self):
        print(self.max_height)


class Cat:
    def __init__(self, name: str, color: str, size: float, hairy: bool):
        self.name = name
        self.color = color
        self.size = size
        self.hairy = hairy

    def show_hairy(self):
        print(self.hairy)


if __name__ == '__main__':
    fish_1 = Fish('Petushok', 'gray', 10.0, 756)
    fish_1.show_max_depth()

    bird_1 = Bird('Chirik', 'blue', 17.3, 2300)
    bird_1.show_max_height()

    cat_1 = Cat('Matroskin', 'red', 23.5, True)
    cat_1.show_hairy()
