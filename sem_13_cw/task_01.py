# Задание No1
# 📌 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
#    пока он не введёт целое или вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.

def ask_user_input():
    while True:
        user_input = input('Введите число: ')
        try:
            result = int(user_input)
            break
        except ValueError as e:
            print(f'{user_input} не удалось привести к целому числу')
            try:
                result = float(user_input)
                break
            except ValueError as e:
                print(f'{user_input} не удалось привести к вещественному числу')
    return result


print(ask_user_input())
