# Задание No2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.


def text_to_uni(text: str) -> list[int]:
    uni_set = set(map(ord, text))
    return sorted(list(uni_set), reverse=True)


input_text = input('Введите текст: ')
print(text_to_uni(input_text))
