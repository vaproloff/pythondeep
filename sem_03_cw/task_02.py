# Задание No3.
# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

input_text = input('Введите данные: ')
result = None

if input_text.replace('-', '', 1).isdecimal():
    result = abs(int(input_text))
elif input_text.replace('.', '', 1).replace('-', '', 1).isdecimal() and '-' not in input_text[1:]:
    result = float(input_text)
elif not input_text.islower():
    result = input_text.lower()
else:
    result = input_text.upper()

print(result, type(result))
