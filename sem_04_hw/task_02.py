# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хэшируем, используйте его строковое представление.

def get_args_dict(**kwargs):
    return {(val if val.__hash__ else str(val)): key for key, val in kwargs.items()}


print(get_args_dict(num1=123, str2='hello', bool3=False, list4=[1, 2, 3], set5={'a', 'b', 'c'}))
