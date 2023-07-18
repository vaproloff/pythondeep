# Задание No2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

text = 'Hello, world!'

# res_dict = {}
# for char in text:
#     res_dict[char] = ord(char)

my_dict = {char: ord(char) for char in text}

print(my_dict)
