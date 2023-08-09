# Задание No2
# 📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков - архивов
# 📌 list-архивы также являются свойствами экземпляра

class Archive:
    """Singleton class. Keeps only one instance of the class. Saves previous arguments to lists.
    """
    _instance = None

    def __init__(self, num: int, text: str):
        """Takes integer num and string text"""
        print('init')
        self.num = num
        self.text = text

    def __new__(cls, *args, **kwargs):
        """Saves new instance to previous instead of creating"""
        print('new')
        print(cls.__name__)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nums = []
            cls._instance.texts = []
        else:
            cls._instance.nums.append(cls._instance.num)
            cls._instance.texts.append(cls._instance.text)
        return cls._instance


if __name__ == '__main__':
    elem_1 = Archive(34, 'text_1')
    elem_2 = Archive(56, 'text_2')
    help(Archive)
