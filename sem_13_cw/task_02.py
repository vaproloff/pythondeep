# Задание No2
# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключений.

def my_get(dct: dict, key: str, default: int | float = None) -> int | float | None:
    result = default
    try:
        result = dct[key]
    except KeyError as e:
        pass
    return result


my_dict = {'a': 56, 'b': 3.4}
print(my_get(my_dict, 'a', 0))
print(my_get(my_dict, 'c', 444))
