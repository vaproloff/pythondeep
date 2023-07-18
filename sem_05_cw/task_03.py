# Задание No3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итератор.
# ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

ITERATIONS = 5

text = 'Hello, world!'

my_dict = {char: ord(char) for char in text}

my_dict_iter = iter(my_dict.items())

for _ in range(ITERATIONS):
    print(next(my_dict_iter))
