# Задание No6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

input_text = input('Введите текст: ')
input_list = sorted(input_text.split())

max_len = 0
for word in input_list:
    if len(word) > max_len:
        max_len = len(word)

for num, word in enumerate(input_list, start=1):
    print(f'{num}. {word:>{max_len}}')
